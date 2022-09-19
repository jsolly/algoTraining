export class Kata {
  /*A Tidy number is a number whose digits are in non-decreasing order.*/
  static tidyNumber(num: number): boolean {
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
  static squareDigits(num: number): number {
    const numSplitToString = num.toString().split('');
    const numArray = numSplitToString.map(Number);
    const squaredArray = numArray.map((num) => num * num);
    const squaredArrayToString = squaredArray.map(String);
    const squaredArrayToStringJoined = squaredArrayToString.join('');
    const squaredArrayToStringJoinedToNumber = Number(
      squaredArrayToStringJoined,
    );
    return squaredArrayToStringJoinedToNumber;
  }

  /* Running Sum of 1d Array
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    */
  static runningSum(nums: number[]): number[] {
    for (let i = 1; i < nums.length; i++) {
      nums[i] += nums[i - 1];
    }
    return nums;
  }

  /* Find Pivot Index
    Given an array of integers nums, write a method that returns the "pivot" index of this array.
    */
  static pivotIndex(nums: number[]): number {
    function mySum(arr: number[]) {
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
}
