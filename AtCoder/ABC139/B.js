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
  var AB = lines[0].split(' ').map(Number);
  var A = AB[0], B = AB[1];
  console.log(Math.ceil((B-1)/(A-1)));
});

