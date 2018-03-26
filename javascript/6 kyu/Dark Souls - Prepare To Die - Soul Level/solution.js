var startingDict = {};
startingDict["warrior"] = [4, 11, 8, 12, 13, 13, 11, 9, 9];
startingDict["knight"] = [5, 14, 10, 10, 11, 11, 10, 9, 11];
startingDict["wanderer"] = [3, 10, 11, 10, 10, 14, 12, 11, 8];
startingDict["thief"] = [5, 9, 11, 9, 9, 15, 10, 12, 11];
startingDict["bandit"] = [4, 12, 8, 14, 14, 9, 11, 8, 10];
startingDict["hunter"] = [4, 11, 9, 11, 12, 14, 11, 9, 9];
startingDict["sorcerer"] = [3, 8, 15, 8, 9, 11, 8, 15, 8];
startingDict["pyromancer"] = [1, 10, 12, 11, 12, 9, 12, 10, 8];
startingDict["cleric"] = [2, 11, 11, 9, 12, 8, 11, 8, 14];
startingDict["deprived"] = [6, 11, 11, 11, 11, 11, 11, 11, 11];

function levelDifference(array1, array2) {
  var diff = 0
  for (var i=0; i<array1.length; i++) {
    diff += array1[i]-array2[i];
  }
  return diff;
}

function soulsPerLevel(level) {
  const soulsPerLevel = [0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829];
  if (level <=  soulsPerLevel.length) {
    return soulsPerLevel[level - 1];
  }
  else {
    var resultSouls = Math.round(Math.pow(level, 3) * 0.02 + Math.pow(level, 2) * 3.06 + 105.6 * level - 895)
    return resultSouls;
  }

}

const souls = (character, build) => {
  var charStats = startingDict[character.toLowerCase()];

  var minimumStats = charStats.slice(1,charStats.length);
  var minLevel = startingDict[character.toLowerCase()][0];

  var levelDiff = levelDifference(build, minimumStats);

  var resultSouls = 0;
  for (var i = minLevel+1; i <= (minLevel+levelDiff); i++) {
    resultSouls += soulsPerLevel(i);
  }

  return "Starting as a "+character+", level " + (minLevel+levelDiff) + " will require " + resultSouls + " souls."
}
