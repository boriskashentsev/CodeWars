function shiftedDiff(first,second){
  var doubleStr = second+second;
  return (first.length == second.length) ? doubleStr.indexOf(first) : -1;
}
