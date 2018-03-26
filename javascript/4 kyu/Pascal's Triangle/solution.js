function pascalsTriangle(n) {
  var indexCompensation = -2;
  var result = [];
  for(var level = 0; level < n; level ++) {
    if (level == 0) {
      result.push(1);
    } else {
      result.push(1);
      for(var i=0; i<level-1; i++) {
        result.push(result[(result.length+indexCompensation)/2]+result[(result.length+indexCompensation)/2+1])
        indexCompensation++;
      }
      result.push(1);
    }
  }
  return result;
}
