#!/usr/bin/node
// return the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let ocur = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      ocur += 1;
    }
  }
  return ocur;
};
