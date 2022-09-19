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
    const result = Kata.runningSum([1,2,3,4]);
    expect(result).toEqual([1,3,6,10]);
  });

test.concurrent('Running Sum 2', () => {  
    const result = Kata.runningSum([1,1,1,1,1]);
    expect(result).toEqual([1,2,3,4,5]);
  });  
