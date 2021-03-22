#!/usr/bin/node
const arg_1 = parseint(process.argv[2]);
if (!isNaN(arg_1)) {
    console.log('My number:' + ' ' + arg_1);
} else {
    console.log('Not a number')
}