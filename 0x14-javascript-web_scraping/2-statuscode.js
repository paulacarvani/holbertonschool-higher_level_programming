#!/usr/bin/node
// Script that display the status code of a GET request.
// Source https://github.com/request/request

const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
