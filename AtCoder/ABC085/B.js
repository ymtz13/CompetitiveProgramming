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
  var N = Number(lines[0]);

  var D = {}, ans=0;
  for(var i=1; i<=N; ++i) {
    var d = Number(lines[i]);
    if(d in D) continue;
    D[d]=null;
    ans+=1;
  }
  
  console.log(ans);
  
});

