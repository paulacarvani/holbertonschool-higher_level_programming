#!/usr/bin/node
// script that prints a square
const num = parseInt(process.argv[2]);
const str = 'X';
if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log(str.repeat(num));
  }
} else {
  console.log('Missing size');
}
