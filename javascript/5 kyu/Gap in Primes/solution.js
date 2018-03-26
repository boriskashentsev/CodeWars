
function gap(g, m, n) {
    var cur = m;
    while (!isPrime(cur)) {
      cur++;
    }
    for(var i = cur+1; i<=n; i++) {
      if(isPrime(i)) {
        if (i-cur == g) {
          return [cur, i];
        }
        cur = i;
      }
    }
    return null;
}


function isPrime(n) {
  for(var i=2; i<Math.round(n/2);i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}
