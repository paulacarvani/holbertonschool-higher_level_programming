#!/usr/bin/node
// Script to prints the arg if this is a number
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
