#!/usr/bin/node

fs = require('fs')

fs.readFile('./input.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }

  list_input = data.split("\n")
  let matrix = []
  
  for (i = 0; i < list_input.length; i++) {
      matrix[i] = list_input[i].split("");
  }
  
  row_length = matrix[0].length
  road_length = matrix.length

  x = 0
  y = 0
  trees = 0

  while(true) {
    if (matrix[y] == null) {
      break
    }
    if (x >= row_length) {
        x = x - row_length
    }
    if (matrix[y][x] == "#") {
      trees = trees+1
    }
    y = y+1 // change rows
    x = x+3 // change columns
  }

  console.log(trees)
});