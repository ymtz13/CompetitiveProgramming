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
  var words = lines[0].split(' ');
  var x = Number(words[0]), y = Number(words[1]);
  console.log(Math.max(x,y))
});

