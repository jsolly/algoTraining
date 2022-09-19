import { expect, test } from 'vitest';
import {
  squareDigits,
  tidyNumber,
  runningSum,
  pivotIndex,
} from '../src/solutions';

test.concurrent('Square Digets', () => {
  const result = squareDigits(9119);
  expect(result).toBe(811181);
});

test.concurrent('Tidy Number True', () => {
  const result = tidyNumber(12);
  expect(result).toBe(true);
});

test.concurrent('Tidy Number False', () => {
  const result = tidyNumber(32);
  expect(result).toBe(false);
});

test.concurrent('Running Sum 1', () => {
  const result = runningSum([1, 2, 3, 4]);
  expect(result).toEqual([1, 3, 6, 10]);
});

test.concurrent('Running Sum 2', () => {
  const result = runningSum([1, 1, 1, 1, 1]);
  expect(result).toEqual([1, 2, 3, 4, 5]);
});

test.concurrent('Find Pivot Index', () => {
  const result = pivotIndex([1, 7, 3, 6, 5, 6]);
  expect(result).toBe(3);
});

test.concurrent('Find Pivot Index 2', () => {
  const result = pivotIndex([1, 2, 3]);
  expect(result).toBe(-1);
});

test.concurrent('Find Pivot Index 3', () => {
  const result = pivotIndex([2, 1, -1]);
  expect(result).toBe(0);
});
