function solution(number){
  // convert the number to a roman numeral
  var numArray = [1000,900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var grArray = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

  var index = 0;
  var result = "";

  while(number > 0) {
    if(number >= numArray[index]) {
      number -= numArray[index];
      result += grArray[index];
    } else {
      index ++;
    }
  }
  return result;
}
