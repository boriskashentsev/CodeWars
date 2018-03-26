function kebabize(str) {
  var result = "";
  for(var i=0; i<str.length; i++) {
    if(str[i].match(/[a-z]/)) {
      result += str[i]
    } else if(str[i].match(/[A-Z]/)) {
      if (result.length > 0) {
        result += "-" + str[i].toLowerCase();
      } else {
        result += str[i].toLowerCase();
      }
    }
  }
  return result;
}
