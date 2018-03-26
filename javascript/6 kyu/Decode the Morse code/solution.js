decodeMorse = function(morseCode){
  morseCode = morseCode.replace(/   /g," | ");
  var morseLetters = morseCode.split(" ");

  var result = "";
  for(i = 0; i < morseLetters.length; i++) {
    if (morseLetters[i] == "|") {
      if(result != "")
        result += " ";
    }
    else if (morseLetters[i] != "") {
      result += MORSE_CODE[morseLetters[i]];
    }
  }
  return result;
}
