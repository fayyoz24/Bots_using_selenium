const fs = require('fs');
const axios = require('axios');
const path = require('path');

const INPUT_FOLDER = 'bot_for_recruiters/datas/datas_json/';
const OUTPUT_FOLDER = 'results';
const TARGET_FILE = 'data.json';

if (!fs.existsSync(OUTPUT_FOLDER)) {
  fs.mkdirSync(OUTPUT_FOLDER);
}

async function processJSONFile(filePath) {
  try {
    const jsonData = JSON.parse(fs.readFileSync(filePath, 'utf8')); // Read and parse JSON data

    for (let i = 0; i < jsonData.length; i++) {
      const study = jsonData[i].study;
      const question = `kun je 10 hard skills geven die je leert per studie ${study}`;

      const options = {
        method: 'POST',
  url: 'https://chatgpt-api8.p.rapidapi.com/',
  headers: {
    'content-type': 'application/json',
    'X-RapidAPI-Key': '5676aba28fmshd9d37e059fa7aa4p1d8860jsnefebe1fcd045',
    'X-RapidAPI-Host': 'chatgpt-api8.p.rapidapi.com'
  },
        data: [
          {
            content: question,
            role: 'user',
          },
        ],
      };

      try {
        const response = await axios.request(options);

        // Extract hard skills from the response (you might need to adjust this part)
        const hardSkills = response?.data.text;

        // Format the response object
        const formattedResponse = {
          study: study,
          hard_skills: hardSkills,
        };

        // Save the formatted response to the results folder
        const resultFileName = `result_${path.basename(filePath, '.json')}_${i}.json`;
        const resultFilePath = path.join(OUTPUT_FOLDER, resultFileName);
        fs.writeFileSync(resultFilePath, JSON.stringify(formattedResponse, null, 2));

        console.log(`Processed ${study}`);
      } catch (error) {
        console.error(error);
      }
    }
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
      console.log(files);
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
