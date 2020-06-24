var readline = require('readline')
var reader = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var lines = [];
reader.on('line', function(line) {
  lines.push(line);
});

var d = [], e = [];
var dist = [];

function dfs(i, d_) {
  dist[i] = d_;
  for(var c in e[i]) {
    chd = e[i][c];
    if(dist[chd]!=-1) continue;
    dfs(chd, d_+d[i][chd]);
  }
}

reader.on('close', function() {
  var N = Number(lines[0]);
  for(var i=0; i<N; ++i) dist.push(-1);

  for(var i=0; i<N; ++i) {
    var dist_i = [];
    for(var j=0; j<N; ++j) {
      dist_i.push(-1);
    }
    d.push(dist_i);
    e.push([]);
  }
  
  for(var i=0; i<N-1; ++i) {
    var uvw = lines[i+1].split(' ');
    var u = Number(uvw[0]);
    var v = Number(uvw[1]);
    var w = Number(uvw[2]);

    e[u-1].push(v-1);
    e[v-1].push(u-1);
    d[u-1][v-1] = d[v-1][u-1] = w;
  }

  dfs(0,0);
  
  for(var i=0; i<N; ++i) console.log(dist[i]%2==0?0:1);
  
});

