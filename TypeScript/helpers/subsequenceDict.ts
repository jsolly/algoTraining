function isSubsequence(s: string, t: string): boolean {
  if (s == '') {
    return true;
  }
  const subsequences = getSubSequencesDict(t);
  if (s in subsequences) {
    return true;
  }
  return false;

  function getSubSequencesDict(myString: string): object {
    const subSequences: Record<string, boolean> = {};
    helper(myString, 0, '');
    return subSequences;

    function helper(s: string, index: number, path: string): void {
      // Print the subsequence when reaching the leaf of recursion tree
      if (index == myString.length) {
        // Condition to avoid printing empty subsequence
        if (path.length > 0) {
          subSequences[path] = true;
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
}
