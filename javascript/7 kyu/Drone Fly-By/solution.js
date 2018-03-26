function flyBy(lamps, drone){
	var result = "";
	index = 0;
	while(index <lamps.length) {
		if(index >= drone.length) {
			result += lamps[index];
		}
		else {
			result += "o";
		}
    index++;
	}
	return result;
}
