import { ListNode } from './utils';

/*
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
*/

export function middleNode(head: ListNode | null): ListNode | null {
  if (!head) {
    return null;
  }
  let rabbit = head.next;
  let turtle = head;

  while (rabbit) {
    rabbit = rabbit.next?.next;
    turtle = turtle.next;
  }

  return turtle;
}

/*
Given the head of a singly linked list, reverse the list, and return the reversed list.
*/

export function reverseList(head: ListNode | null): ListNode | null {
  let n = null,
    h = head;
  while (h !== null) {
    n = new ListNode(h.val, n);
    h = h.next;
  }
  return n;
}

/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/

export function mergeTwoLists(
  l1: ListNode | null,
  l2: ListNode | null,
): ListNode | null {
  const head: ListNode = new ListNode();
  let curr: ListNode = head;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      curr.next = l1;
      l1 = l1.next;
    } else {
      curr.next = l2;
      l2 = l2.next;
    }
    curr = curr.next;
  }
  curr.next = l1 ?? l2;
  return head.next;
}

/* Given two strings s and t, return true if s is a subsequence of t, or false otherwise. */
export function isSubsequence(s: string, t: string): boolean {
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

/*Given two strings s and t, determine if they are isomorphic.*/
export function isIsomorphic(s: string, t: string): boolean {
  const SmapToT: Record<string, string> = {};
  const TmapToS: Record<string, string> = {};
  for (let i = 0; i < s.length; i++) {
    if (!SmapToT[s[i]] && !TmapToS[t[i]]) {
      SmapToT[s[i]] = t[i];
      TmapToS[t[i]] = s[i];
    } else if (SmapToT[s[i]] != t[i] || TmapToS[t[i]] != s[i]) {
      return false;
    }
  }
  return true;
}

/*A Tidy number is a number whose digits are in non-decreasing order.*/
export function tidyNumber(num: number): boolean {
  const numSplitToString = num.toString().split('');
  const numArray = numSplitToString.map(Number);
  for (let i = 0; i < numArray.length; i++) {
    if (numArray[i] > numArray[i + 1]) {
      return false;
    }
  }
  return true;
}

/* Welcome. In this kata, you are asked to square every digit of a number and concatenate them.*/
export function squareDigits(num: number): number {
  const numSplitToString = num.toString().split('');
  const numArray = numSplitToString.map(Number);
  const squaredArray = numArray.map((num) => num * num);
  const squaredArrayToString = squaredArray.map(String);
  const squaredArrayToStringJoined = squaredArrayToString.join('');
  const squaredArrayToStringJoinedToNumber = Number(squaredArrayToStringJoined);
  return squaredArrayToStringJoinedToNumber;
}

/* Running Sum of 1d Array
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    */
export function runningSum(nums: number[]): number[] {
  for (let i = 1; i < nums.length; i++) {
    nums[i] += nums[i - 1];
  }
  return nums;
}

/* Find Pivot Index
    Given an array of integers nums, write a method that returns the "pivot" index of this array.
    */
export function pivotIndex(nums: number[]): number {
  function mySum(arr: number[]): number {
    return arr.reduce((a, b) => a + b, 0);
  }

  let leftSum = 0;
  const SUM = mySum(nums);
  for (let i = 0; i < nums.length; i++) {
    if (leftSum == SUM - leftSum - nums[i]) {
      return i;
    }
    leftSum += nums[i];
  }
  return -1;
}
