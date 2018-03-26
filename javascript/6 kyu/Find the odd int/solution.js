function findOdd(A) {

  var array=[];
  var amount = [];

  for(var i=0; i<A.length; i++) {

    var j=0;
    for(j=0; j<array.length; j++) {
      if(array[j] == A[i]){
        break;
      }
    }

    if(j >= array.length) {
      array.push(A[i]);
      amount.push(1);
    } else {
      amount[j]++;
    }
  }

  for(i = 0; i<array.length; i++) {
    if (amount[i] % 2 == 1) {
      return array[i];
    }
  }
}
