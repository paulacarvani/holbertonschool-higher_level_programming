#!/usr/bin/node
// imports an array and computes a new array
 const list = require('./100-data.js').list;
const temp = list.map((x, index) => x * index);
console.log(list);
console.log(temp);
