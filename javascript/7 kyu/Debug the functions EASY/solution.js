function multi(arr) {
  var result = 1;
  for (var i=0; i<arr.length; i++) {
    result *= arr[i];
  }
  return result;
}
function add(arr) {
  var result = 0;
  for (var i=0; i<arr.length; i++) {
    result += arr[i];
  }
  return result;
}
function reverse(str) {
  var result = "";
  for(var i=str.length-1; i>=0; i--) {
    result += str[i];
  }
  return result;
}
