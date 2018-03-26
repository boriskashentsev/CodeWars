function streetFighterSelection(fighters, position, moves){
  var y = fighters.length;
  var x = fighters[0].length;
  var index = 0;
  var result = [];

  var firstPosition = [];
  firstPosition.push(position[0]);
  firstPosition.push(position[1]);

  while (index < moves.length) {
    switch (moves[index]){
      case "up":
        if (firstPosition[0] > 0) {
          firstPosition[0]--;
        }
        break;
      case "down":
        if (firstPosition[0] < y-1) {
          firstPosition[0]++;
        }
        break;
      case "left":
        if(firstPosition[1] > 0) {
          firstPosition[1]--;
        } else {
          firstPosition[1] = x-1;
        }
        break;
      case "right":
        if(firstPosition[1] < x-1) {
          firstPosition[1]++;
        } else {
          firstPosition[1] = 0;
        }
        break;
    }
    result.push(fighters[firstPosition[0]][firstPosition[1]]);
    index++;
  }

  return result;
}
