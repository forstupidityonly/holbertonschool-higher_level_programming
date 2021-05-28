#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.writeFile(myArgs[0], muArgs[1], 'utf-8', (err, data) => {
  if (err) console.log(err);
});
