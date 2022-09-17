import { expect, test } from 'vitest';
import { mySum } from '../src/sum';

test.concurrent('Sum', () => {
    const result = mySum(1, 2);
    expect(result).toBe(3);
  });