import { expect, test } from 'vitest';
import * as Solution from '../src/solutions';


test.concurrent('Merge Two Sorted Linked Lists', () => {
  const list1 = [1, 2, 4];
  const list2 = [1, 3, 4];
  const expected = [1, 1, 2, 3, 4, 4];
  const actual = Solution.mergeTwoLists(list1, list2);
  expect(actual).toEqual(expected);
});

test.concurrent('isSubsequence', () => {
  expect(Solution.isSubsequence('abc', 'ahbgdc')).toBe(true);
  expect(Solution.isSubsequence('axc', 'ahbgdc')).toBe(false);
});

test.concurrent('isIsomorphic', () => {
  expect(Solution.isIsomorphic('egg', 'add')).toBe(true);
  expect(Solution.isIsomorphic('foo', 'bar')).toBe(false);
  expect(Solution.isIsomorphic('paper', 'title')).toBe(true);
  expect(Solution.isIsomorphic('ab', 'aa')).toBe(false);
});

test.concurrent('Square Digts', () => {
  const result = Solution.squareDigits(9119);
  expect(result).toBe(811181);
});

test.concurrent('Tidy Number True', () => {
  const result = Solution.tidyNumber(12);
  expect(result).toBe(true);
});

test.concurrent('Tidy Number False', () => {
  const result = Solution.tidyNumber(32);
  expect(result).toBe(false);
});

test.concurrent('Running Sum 1', () => {
  const result = Solution.runningSum([1, 2, 3, 4]);
  expect(result).toEqual([1, 3, 6, 10]);
});

test.concurrent('Running Sum 2', () => {
  const result = Solution.runningSum([1, 1, 1, 1, 1]);
  expect(result).toEqual([1, 2, 3, 4, 5]);
});

test.concurrent('Find Pivot Index', () => {
  const result = Solution.pivotIndex([1, 7, 3, 6, 5, 6]);
  expect(result).toBe(3);
});

test.concurrent('Find Pivot Index 2', () => {
  const result = Solution.pivotIndex([1, 2, 3]);
  expect(result).toBe(-1);
});

test.concurrent('Find Pivot Index 3', () => {
  const result = Solution.pivotIndex([2, 1, -1]);
  expect(result).toBe(0);
});
