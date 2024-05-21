#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, { json: true }, (err, res, body) => {
  if (err == null) {
    fs.writeFileSync(file, body, 'utf8');
  }
});
