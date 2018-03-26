function mobileDisplay(n,p){
  var result = "";
  var width = (n>20) ? n : 20;
  var percent = (p>30) ? p : 30;
  var height = Math.floor((width*percent)/100);
  var cwLine = Math.floor(height/2);
  for(var line=0; line <height; line++) {
    if (line == 0) {
      result += repeatChar(width,"*") + "\n";
    } else if (line == height-1) {
      result += repeatChar(width,"*");
    } else if (line == cwLine - 1) {
      result += "*" + repeatChar(Math.floor((width-10)/2)," ") + "CodeWars" + repeatChar(Math.round((width-10)/2)," ") + "*\n";
    } else if (line == height-2) {
      result += "* Menu" + repeatChar(width-16," ") + "Contacts *\n";
    } else {
      result += "*" + repeatChar(width-2," ") + "*\n";
    }
  }
  return result;
}

function repeatChar(n, ch) {
  var line = "";
  for(var i=0; i<n; i++){
    line += ch;
  }
  return line;
}
