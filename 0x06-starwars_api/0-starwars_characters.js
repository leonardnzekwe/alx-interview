#!/usr/bin/node

// Importing the 'request' module
const request = require('request');

/**
 * Asynchronous function to fetch characters of a specific Star Wars movie
 * @param {number} movieId - The ID of the Star Wars movie
 * @returns {Promise<Array<string>>} - A promise that resolves to an array of character names
 */
async function getCharacters (movieId) {
  // Constructing the API URL for the specified movie ID
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    // Making a GET request to fetch film data
    const filmResponse = await new Promise((resolve, reject) => {
      request(apiUrl, function (error, response, body) {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(new Error(`Status: ${response.statusCode}`));
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    // Extracting character URLs from the film data
    const charactersUrls = filmResponse.characters;

    // Fetching character data for each character URL
    const characters = await Promise.all(charactersUrls.map(async url => {
      // Making a GET request to fetch character data
      const characterResponse = await new Promise((resolve, reject) => {
        request(url, function (error, response, body) {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(new Error(`Status: ${response.statusCode}`));
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      return characterResponse;
    }));

    // Returning the array of character names
    return characters;
  } catch (error) {
    // Handling errors
    throw new Error(`Error fetching characters: ${error}`);
  }
}

// Main function
async function main () {
  // Retrieving the movie ID from command-line arguments
  const movieId = process.argv[2];
  try {
    // Calling the getCharacters function to fetch characters
    const characters = await getCharacters(movieId);
    // Printing each character name
    characters.forEach(character => console.log(character));
  } catch (error) {
    // Handling errors
    console.error(error);
  }
}

// Invoking the main function
main();
