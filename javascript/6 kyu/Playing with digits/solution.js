function digPow(n, p){
  var result = 0;
  var newN = 0;
  var oldN = n;
  while (oldN>0) {
    newN = newN*10 + oldN % 10;
    oldN = Math.floor(oldN / 10);
  }
  while (newN >0) {
    result += Math.pow(newN%10, p),
    newN = Math.floor(newN / 10);
    p++;
  }

  if(result % n == 0) {
    return Math.round(result / n);
  }
  return -1;
}
