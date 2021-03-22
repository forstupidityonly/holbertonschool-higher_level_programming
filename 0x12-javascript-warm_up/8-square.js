#!/usr/bin/node
const argOne = parseInt(process.argv[2]);
if (!isNaN(argOne)) {
  for (let i = 0; i < argOne; i++) {
    console.log('X'.repeat(argOne));
  }
} else {
  console.log('Missing size');
}
