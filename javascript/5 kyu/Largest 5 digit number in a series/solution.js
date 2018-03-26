function solution(digits){
  var result = -1;
  for(var i=0; i<digits.length-4; i++) {
    var current = digits.substr(i,5);
    if (result < parseInt(current)) {
      result = parseInt(current);
    }
  }
  return result;
}
