#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err == null) {
    let count = 0;
    for (const list of body.results) {
      for (const char of list.characters) {
        if (char.includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
