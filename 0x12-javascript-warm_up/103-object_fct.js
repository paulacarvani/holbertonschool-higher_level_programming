#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// my code here:
myObject.incr = function () {
  return this.value++;
};
// end of my code

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
