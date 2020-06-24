var readline = require('readline')
var reader = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var lines = [];
reader.on('line', function(line) {
  lines.push(line);
});

reader.on('close', function() {
  console.log(lines[0].slice(0,3) + '8' + lines[0].slice(4));
});

