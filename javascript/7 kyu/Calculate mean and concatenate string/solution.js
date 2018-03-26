
function mean(lst){
  var meanValue = 0;
  var string = "";
  for(i=0; i<lst.length; i++) {
    if (!isNaN(lst[i])) {
      meanValue += parseInt(lst[i]);
    } else {
      string += lst[i];
    }
  }
  return [meanValue/10., string];
}
