#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err == null) {
    let count = 0;
    let signal = 0;
    const obj = {};
    for (const stat of body) {
      if (signal !== stat.userId) {
        count = 0;
      }
      if (stat.completed === true) {
        count++;
        obj[stat.userId] = count;
      }
      signal = stat.userId;
    }
    console.log(obj);
  }
});
