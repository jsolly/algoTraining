import { expect, test } from 'vitest';
import { Kata } from '../src/solutions';

test.concurrent('Square Digets', () => {
  const result = Kata.squareDigits(9119);
  expect(result).toBe(811181);
});

test.concurrent('Tidy Number True', () => {
  const result = Kata.tidyNumber(12);
  expect(result).toBe(true);
});

test.concurrent('Tidy Number False', () => {
  const result = Kata.tidyNumber(32);
  expect(result).toBe(false);
});

test.concurrent('Running Sum 1', () => {
  const result = Kata.runningSum([1, 2, 3, 4]);
  expect(result).toEqual([1, 3, 6, 10]);
});

test.concurrent('Running Sum 2', () => {
  const result = Kata.runningSum([1, 1, 1, 1, 1]);
  expect(result).toEqual([1, 2, 3, 4, 5]);
});

test.concurrent('Find Pivot Index', () => {
  const result = Kata.pivotIndex([1, 7, 3, 6, 5, 6]);
  expect(result).toBe(3);
});

test.concurrent('Find Pivot Index 2', () => {
  const result = Kata.pivotIndex([1, 2, 3]);
  expect(result).toBe(-1);
});

test.concurrent('Find Pivot Index 3', () => {
  const result = Kata.pivotIndex([2, 1, -1]);
  expect(result).toBe(0);
});
