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
  var H = lines[1].split(' ').map(Number), ans=0, k=0;
  for(var i=1; i<N; ++i) if(H[i-1]>=H[i]) { ++k; ans=Math.max(ans,k); } else { k=0; }
  console.log(ans);
});

