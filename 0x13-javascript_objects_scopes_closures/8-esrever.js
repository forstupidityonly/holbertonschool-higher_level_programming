#!/usr/bin/node
export.esrever = function (list) {
    const answer = [];
    for (let i = 0; i < list.length; i++) {
        answer.unshift(list[i]);
    }
    return answer;
};