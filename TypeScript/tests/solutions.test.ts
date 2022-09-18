import { expect, test } from 'vitest';
import { Kata } from '../src/solutions';

test.concurrent('Sum', () => {
    const result = Kata.squareDigits(9119);
    expect(result).toBe(811181);
  });