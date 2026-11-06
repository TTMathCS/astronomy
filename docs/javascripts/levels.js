// the level shown at the top of a book chapter on astronomy.akadian.ca, worked out from where it sits in its book.
// History chapters read at every level: each one starts with the story and ends with the evidence and the arguments.
window.akadianLevel = function (path, ch, n) {
  if (/\/books\/history\/\d+-/.test(path)) return "All";
  if (/\/books\/[^\/]+\/\d+-/.test(path) && ch && n) {
    if (ch === n) return "Expert";
    if (ch <= Math.ceil(n * 0.2)) return "Beginner";
    if (ch > n * 0.75) return "Expert";
    return "Intermediate";
  }
  return null;
};
