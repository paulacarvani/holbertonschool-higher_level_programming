#!/usr/bin/node
// script that reads and prints the content of a file.
// Source https://nodejs.dev/learn/reading-files-with-nodejs

const fs = require('fs')
const { argv } = require('process')

fs.readFile(argv[2], 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }
  console.log(data.toString('utf-8'))
})
