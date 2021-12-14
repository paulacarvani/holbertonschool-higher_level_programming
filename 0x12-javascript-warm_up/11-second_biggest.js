#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const num = process.argv.slice(2).map((x) => {
  return parseInt(x);
});
if (num.length <= 1) {
  console.log(0);
} else {
  console.log(num.sort((a, b) => {
    return b - a;
  })[1]);
}
