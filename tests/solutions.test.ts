import { expect, test } from 'vitest';
import * as Solution from '../src/solutions';
import { ListNode } from '../src/utils';

test('middleNode', () => {
  expect(Solution.middleNode(null)).toBe(null);
  expect(Solution.middleNode(new ListNode(1))).toBe(new ListNode(1));
  expect(Solution.middleNode(new ListNode(1, new ListNode(2)))).toBe(
    new ListNode(2),
  );
  expect(Solution.middleNode(new ListNode(1, new ListNode(2, new ListNode(3))))).toBe(
    new ListNode(2, new ListNode(3)),
  );

test.concurrent('Reverse Linked List', () => {
  const head = new ListNode(
    1,
    new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))),
  );
  const expected = new ListNode(
    5,
    new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(1)))),
  );
  expect(Solution.reverseList(head)).toEqual(expected);

  const head2 = new ListNode(1, new ListNode(2));
  const expected2 = new ListNode(2, new ListNode(1));
  expect(Solution.reverseList(head2)).toEqual(expected2);
});

test.concurrent('Merge Two Sorted Linked Lists', () => {
  const listNode1 = new ListNode(1, new ListNode(2, new ListNode(4)));
  const listNode2 = new ListNode(1, new ListNode(3, new ListNode(4)));
  const expected = new ListNode(
    1,
    new ListNode(
      1,
      new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(4)))),
    ),
  );
  const actual = Solution.mergeTwoLists(listNode1, listNode2);
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
