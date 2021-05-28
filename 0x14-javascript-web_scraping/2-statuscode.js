#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const opt = {
    url:myArgs[0],
    method: 'GET',
    headers: {
       'Accept-Charset': 'utf8'
    }
};
request(opt, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
