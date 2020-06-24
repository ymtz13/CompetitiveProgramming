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
  var ans = 0;
  for(var i=0; i<3; ++i) if(lines[0][i]==lines[1][i]) ++ans;
  console.log(ans);
});

