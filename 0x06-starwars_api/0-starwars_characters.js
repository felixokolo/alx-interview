#!/usr/bin/node
const request = require('request');
let part = 0;
if (process.argv.length === 3) {
  part = process.argv[2];
}
const url = `https://swapi-api.alx-tools.com/api/films/${part}/?format=json`;

function getPersonPromise (url) {
  const promise = new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      console.error(err);
      if (resp.statusCode === 200) {
        const personName = JSON.parse(body).name;
        resolve(personName);
      } else {
        reject(new Error('Error'));
      }
    });
  });
  return promise;
}

request(url, (err, resp, body) => {
  console.error(err);
  if (resp.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const promises = characters.map((uri) => getPersonPromise(uri));
    Promise.all(promises).then(result => {
      result.forEach(element => {
        console.log(element);
      });
    });
  }
});
