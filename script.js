const fs =require('fs');
const axios=require('axios')
const path =require('path');

const { Configuration, OpenAIApi } = require('openai');


const API_KEY = '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';
const INPUT_FOLDER = 'bot_for_recruiters/datas/datas_json/';
const OUTPUT_FOLDER = 'bot_for_recruiters/';
const TARGET_FILE = 'data.json';


if (!fs.existsSync(OUTPUT_FOLDER)) {
  fs.mkdirSync(OUTPUT_FOLDER);
}

async function processJSONFile(filePath) {

  const configuration = new Configuration({
    organization: "org-pVhorJhu0akomR958gyPlGJw",
    apiKey: API_KEY,
});

const openai = new OpenAIApi(configuration);

  const response = await openai.listEngines();
  console.log(response)
  try {
    console.log('try')
    const jsonData = JSON.parse(fs.readFileSync(filePath, 'utf8')); // Read and parse JSON data

    for (let i = 0; i < jsonData.length; i++) {
      const question = `kun je 10 hard skills geven die je leert per studie ${jsonData[i].study}`;

      const response = await axios.post('https://api.openai.com/v1/chat/completions', {
        prompt: question,
        max_tokens: 500,
      }, {
        headers: {
          Authorization: `Bearer ${API_KEY}`,
          'Content-Type': 'application/json',
        },
      });
      // Assign the response to the corresponding keyword
      const keyword = `keyword${i + 1}`;
      const resultObject = {};
      resultObject[keyword] = response.data; // Assuming you want to save the response text

      // Save the API response to the results folder
      const resultFileName = `result_${path.basename(filePath, '.json')}_${i}.json`;
      const resultFilePath = path.join(OUTPUT_FOLDER, resultFileName);
      fs.writeFileSync(resultFilePath, JSON.stringify(resultObject, null, 2));

      console.log(`Processed ${keyword} for ${jsonData[i].study}`);
    }

    console.log(`Processing complete for file: ${path.basename(filePath)}`);
  } catch (error) {
    console.error('Error processing file:', filePath, error);
  }
}

async function processJSONFiles() {
  try {
    const files = fs.readdirSync(INPUT_FOLDER);
    
    if (files.length === 0) {
      console.log(`No files found in ${INPUT_FOLDER}`);
    } else {
      console.log(files)
      for (const file of files) {
        if (file === TARGET_FILE) {
          const filePath = path.join(INPUT_FOLDER, file);
          await processJSONFile(filePath);
        }
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


processJSONFiles();
