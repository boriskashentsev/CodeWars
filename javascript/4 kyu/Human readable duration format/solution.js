function formatDuration (seconds) {
  if (seconds == 0) {
    return "now";
  }
  var result = "";
  var array = [];
  var years = Math.floor(seconds / 31536000);
  if (years > 0) {
    if (years == 1) {
      array.push(years+ " year");
    } else {
      array.push(years+ " years");
    }
    seconds -= years * 31536000;
  }
  var days = Math.floor(seconds / 86400);
  if (days > 0) {
    if(days == 1) {
      array.push(days+ " day");
    } else {
      array.push(days+ " days");
    }
    seconds -= days * 86400;
  }
  var hours = Math.floor(seconds / 3600);
  if (hours > 0) {
    if (hours == 1) {
      array.push(hours+ " hour");
    } else {
      array.push(hours+ " hours");
    }
    seconds -= hours * 3600;
  }
  var minutes = Math.floor(seconds / 60);
  if (minutes > 0) {
    if (minutes == 1) {
      array.push(minutes+ " minute");
    } else {
      array.push(minutes+ " minutes");
    }
    seconds -= minutes * 60;
  }
  if (seconds == 1) {
    array.push(seconds+ " second");
  } else if (seconds > 1) {
    array.push(seconds+ " seconds");
  }
  if (array.length > 1) {
    for (var i = 0; i < array.length-2; i++) {
      result += array[i] + ", ";
    }
    result += array[array.length-2] + " and ";
  }
  result += array[array.length-1];
  return result;
}
