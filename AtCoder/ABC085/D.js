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
  var N = Number(words[0]), H = Number(words[1]);

  var B = [], amax = 0;
  for(var i=1; i<=N; ++i) {
    var ab = lines[i].split(' ').map(Number);
    amax = Math.max(amax, ab[0]);
    B.push(ab[1]);
  }
  B.sort(function(x,y){return y-x;})

  var ans=0;
  for(var i=0; i<N && B[i]>amax && H>0; ++i) {
    ans+=1;
    H -= B[i];
  }

  H = Math.max(H,0);
  ans += Math.ceil(H/amax);
  
  console.log(ans);
  
});

