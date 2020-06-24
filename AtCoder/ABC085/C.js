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
  var N = Number(words[0]), Y = Number(words[1]);

  OUT_OF_THE_LOOP:
  {
    for(var x=0; x <=N; ++x) for(var y=0; x+y<=N; ++y) {
      var z = N-x-y;
      if(10000*x+5000*y+1000*z==Y) {
        console.log(x+' '+y+' '+z);
        break OUT_OF_THE_LOOP;
      }
    }

    console.log('-1 -1 -1');
  }
  
});

