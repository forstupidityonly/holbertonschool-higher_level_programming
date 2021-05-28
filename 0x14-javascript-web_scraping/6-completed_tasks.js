#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, resp, bod) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(bod);
    const comptask = {};
    todos.forEach((todo) => {
      if (todo.completed && comptask[todo.userId] === undefined) {
        comptask[todo.userId] = 1;
      } else if (todo.completed) {
        comptask[todo.userId] += 1;
      }
    });
    console.log(comptask);
  }
});
