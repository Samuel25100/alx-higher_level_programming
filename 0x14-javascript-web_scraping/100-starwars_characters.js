#!/usr/bin/node
const request = require('request');

const mid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${mid}/`;

request(url, { json: true }, (err, res, body) => {
  if (err == null) {
    const result = body.characters;
    for (const link of result) {
      request(link, { json: true }, (err, res, body1) => {
        if (err == null) {
          console.log(body1.name);
        }
      });
    }
  }
});
