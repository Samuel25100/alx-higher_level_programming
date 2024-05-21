#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res) => {
  if (err == null) {
    console.log('code: ', res.statusCode);
  }
});
