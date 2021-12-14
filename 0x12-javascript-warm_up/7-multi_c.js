#!/usr/bin/node
// script that prints a sentence x args passed
const num = parseInt(process.argv[2]);
if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
