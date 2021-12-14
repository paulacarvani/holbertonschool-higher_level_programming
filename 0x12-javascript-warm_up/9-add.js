#!/usr/bin/node
// script to add 2 args passed, define funtion first
function add (a, b) {
  console.log(a + b);
}

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);
if (Number.isInteger(n1) && Number.isInteger(n2)) {
  add(n1, n2);
} else {
  console.log('NaN');
}
