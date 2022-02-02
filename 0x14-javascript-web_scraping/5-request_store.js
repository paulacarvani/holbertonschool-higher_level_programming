#!/usr/bin/node
// Script that saves the body content of a GET request to a file
const fs = require('fs');
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(argv[3], body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
