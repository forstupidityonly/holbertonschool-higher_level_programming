#!/usr/bin/node
//reads a file
const fs = require('fs');
fs.readFile()process.argv[2], 'utf8', (error, data) => {
    if (err) console.log(err);
    else console.log(data);
});
