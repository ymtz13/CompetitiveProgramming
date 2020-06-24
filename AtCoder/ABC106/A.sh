read line
AB=(${line})
A=${AB[0]}
B=${AB[1]}
echo $(( (A-1)*(B-1) ))
