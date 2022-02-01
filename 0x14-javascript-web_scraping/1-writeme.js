#!/usr/bin/node
// script that writes a string to a file.
// Source https://nodejs.dev/learn/writing-files-with-nodejs

const fs = require('fs');
const { argv } = require('process');

const content = argv[3];

fs.writeFile(argv[2], content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
