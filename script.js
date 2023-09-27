const fs = require('fs');
const axios = require('axios');
const path = require('path');

const API_KEY = 'YOUR_OPENAI_API_KEY';
const INPUT_FOLDER = './json'; 
const OUTPUT_FOLDER = './results'; 

if (!fs.existsSync(OUTPUT_FOLDER)) {
  fs.mkdirSync(OUTPUT_FOLDER);
}

async function processJSONFiles() {
  try {
    const files = fs.readdirSync(INPUT_FOLDER);

    for (const file of files) {
      if (file.endsWith('.json')) {
        const filePath = path.join(INPUT_FOLDER, file);
        const jsonData = require(filePath); // Load JSON data

        // Create an object to store results for each keyword
        const resultObject = {};

        for (let i = 0; i < jsonData.length; i++) {
          const question = jsonData[i].question;

          const response = await axios.post('https://api.openai.com/v1/engines/davinci-codex/completions', {
            prompt: question,
            max_tokens: 50, 
          }, {
            headers: {
              Authorization: `Bearer ${API_KEY}`,
              'Content-Type': 'application/json',
            },
          });

          // Assign the response to the corresponding keyword
          const keyword = `keyword${i + 1}`;
          resultObject[keyword] = response.data.choices[0].text; // Assuming you want to save the response text

          // Save the API response to the results folder
          const resultFileName = `result_${file}_${i}.json`;
          const resultFilePath = path.join(OUTPUT_FOLDER, resultFileName);
          fs.writeFileSync(resultFilePath, JSON.stringify(response.data, null, 2));
        }

        // Convert the resultObject to JSON and save it in the specified format
        const resultData = {
          hard_skills: JSON.stringify(resultObject),
          essential_keywords: JSON.stringify(resultObject),
          related_jobs: JSON.stringify(resultObject),
        };

        // Save the resultData in the desired format
        const resultDataFileName = `formatted_result_${file}.json`;
        const resultDataFilePath = path.join(OUTPUT_FOLDER, resultDataFileName);
        fs.writeFileSync(resultDataFilePath, JSON.stringify(resultData, null, 2));
      }
    }

    console.log('Processing complete.');
  } catch (error) {
    console.error('Error:', error);
  }
}

processJSONFiles();
