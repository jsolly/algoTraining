function getSubSequencesString(myString: string): string[][] {
  const subSequences: string[][] = [];
  helper(myString, 0, '');
  return subSequences;

  function helper(s: string, index: number, path: string): void {
    // Print the subsequence when reaching the leaf of recursion tree
    if (index == myString.length) {
      // Condition to avoid printing empty subsequence
      if (path.length > 0) {
        const pathDeepCopy = JSON.parse(JSON.stringify(path)) as string[];
        subSequences.push(pathDeepCopy);
      }
    } else {
      // Subsequence without including the element at current index
      helper(myString, index + 1, path);
      path += myString[index];
      // Subsequence including the element at current index
      helper(myString, index + 1, path);
      path = path.slice(0, -1);
    }
  }
}

console.log(getSubSequencesString('abc'));
