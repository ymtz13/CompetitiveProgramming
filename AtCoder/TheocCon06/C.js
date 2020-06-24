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
  var N = Number(words[0]), M = Number(words[1]);
  var A = [];
  var B = [1];
  
  for(var i=0; i<N; ++i) A.push(true);

  for(var i=0; i<M; ++i) A[Number(lines[i+1])-1] = false;

  var mod = 1000000007;

  if(!A[0]) { B.push(0); }
  else { B.push(1); }
  
  for(var i=1; i<N; ++i) {
    if(!A[i]) { B.push(0); continue; }
    B.push((B[B.length-2]+B[B.length-1])%mod);
  }

  //console.log(B);
  
  console.log(B[B.length-1]);
  
});

