function solveIt(excel){
  rows = excel.length

  diff1 = 0;
  row = -1


  for (i=0; i<rows; i++) {
    diff1 = excel[i].reduce(function(a,b){return a+b;},-2*excel[i][rows-1]);
    if (diff1 != 0) {
      row = i
      break;
    }
  }

  diff2 = 0;
  col = -1;

  for (i=0; i<rows; i++) {
    diff2 = excel.map(function(value,index) { return value[i]; }).reduce(function(a,b){return a+b;},-2*excel[rows-1][i]);
    if (diff2 != 0) {
      col = i
      break;
    }
  }

  if (col == rows-1) {
    return (excel[row][col] + diff1)
  }

  return( excel[row][col]-diff1)
}
