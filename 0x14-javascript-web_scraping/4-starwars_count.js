#!/usr/bin/node
// script that prints the number of movies where
// the character “Wedge Antilles” is present.

const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    if (film.characters.find((character) => character.includes('18'))) {
      count += 1;
    }
  }
  console.log(count);
});
