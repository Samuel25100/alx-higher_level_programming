#!/usr/bin/node
/*  returns the reversed version of a list */
exports.esrever = function (list) {
  const rev = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    rev.push(list[i]);
  }
  return (rev);
};
