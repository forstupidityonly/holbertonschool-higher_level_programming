#!/usr/bin/node
const argOne = parseInt(process.argv[2]);
if (!isNaN(argOne)) {
  console.log('My number:' + ' ' + argOne);
} else {
  console.log('Not a number');
}
