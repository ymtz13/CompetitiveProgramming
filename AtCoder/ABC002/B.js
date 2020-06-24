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
  var w = lines[0];
  var s = {a:0, i:0, u:0, e:0, o:0};
  var ans = "";
  for(var i in w) if(!(w[i] in s)) ans+=w[i];
  console.log(ans);
});

