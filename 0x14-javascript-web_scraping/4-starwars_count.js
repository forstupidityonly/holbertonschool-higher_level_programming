#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    let Count = 0;
    const movies = JSON.parse(body).results;
    for (let x = 0; x < movies.length; x++) {
      for (let y = 0; y < movies[x].characters.length; y++) {
        if (movies[x].characters[y].includes('/18/')) {
          Count++;
          break;
        }
      }
    }
    console.log(Count);
  }
});
