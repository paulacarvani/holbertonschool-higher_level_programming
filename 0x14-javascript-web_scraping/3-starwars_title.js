#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const { argv } = require('process');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
