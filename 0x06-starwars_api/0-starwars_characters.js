#!/usr/bin/node
const request = require('request');
let part = 0;
if (process.argv.length == 3) {
  part = process.argv[2];
}
url = `https://swapi-api.alx-tools.com/api/films/${part}/?format=json`;



function getPersonPromise(url) {
  let promise = new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      if (resp.statusCode == 200) {
        personName = JSON.parse(body).name;
        resolve(personName);
      }
      else {
        reject("Error")
      }
    });
  });
  return promise;
}

request(url, (err, resp, body) => {
  if (resp.statusCode == 200){
    characters = JSON.parse(body).characters;
    let promises = characters.map((uri) => getPersonPromise(uri));
    Promise.all(promises).then(result => {
      result.forEach(element => {
        console.log(element);
      });
    })
  }
});


