#!/usr/bin/node
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
