function solveIt(excel){
  var rows = excel.length

  var diff1 = 0;
  var row = -1


  for (var i=0; i<rows; i++) {
    diff1 = -excel[i][rows-1];
    for (var j=0; j<rows-1; j++) {
      diff1 += excel[i][j];
    }
    if (diff1 != 0) {
      row = i;
      break;
    }
  }

  var diff2 = 0;
  var col = -1;

  for (var i=0; i<rows; i++) {
    diff2 = -excel[rows-1][i];
    for (var j=0; j<rows-1; j++){
      diff2 += excel[j][i];
    }
    if (diff2 != 0) {
      col = i;
      break;
    }
  }

  if (col == rows-1) {
    return (excel[row][col] + diff1)
  }

  return (excel[row][col]-diff1)
}
