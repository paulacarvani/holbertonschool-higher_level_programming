#!/usr/bin/node
// function that executes x times a function
exports.callMeMoby = (n, f) => {
  for (let i = 0; i < n; i++) {
    f();
  }
};
