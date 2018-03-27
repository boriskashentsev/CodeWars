function to_nato(words) {
  words = words.toLowerCase();
  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  var natoLetters= ["Alfa","Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"];

  var result = "";

  for(i=0; i<words.length; i++) {
    if(words[i] != " ") {
      if(result.length > 0) {
        result+=" "
      }
      var index = alphabet.indexOf(words[i]);
      if(index != -1) {
        result += natoLetters[index];
      } else {
        result += words[i]
      }
    }
  }

  return result;
}
