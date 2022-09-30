function isSubsequence(s: string, t: string): boolean {
  let counter = 0;
  let pointerA = 0;
  let pointerB = 0;
  while (pointerA < t.length) {
    if (t[pointerA] === s[pointerB]) {
      counter++;
      pointerA++;
      pointerB++;
    } else {
      pointerA++;
    }
  }
  return s.length === counter;
}
