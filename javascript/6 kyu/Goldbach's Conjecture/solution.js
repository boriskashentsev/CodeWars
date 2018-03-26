// Checks Goldbach's conjecture for the given argument

function isPrime(number) {
  if (number == 1) {
    return false;
  }
  for(var i = 2; i <= Math.floor(number/2.0); i++) {
      if(number % i == 0) {
        return false;
      }
  }
  return true;
}

function isEven(number) {
  return (number % 2 == 0);
}

var checkGoldbach = function(number) {
  if (!isEven(number) || number < 3) {
    return [];
  }

  for (var i = 2; i <= Math.floor(number / 2.0)+1; i++ ) {
    if (isPrime(i) && isPrime(number-i)) {
      return [i, number-i];
    }
  }
  return [];
};
