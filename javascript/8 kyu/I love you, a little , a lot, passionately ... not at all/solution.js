function howMuchILoveYou(nbPetals) {
  let phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"];

  return phrases[(nbPetals-1) % phrases.length];
}
