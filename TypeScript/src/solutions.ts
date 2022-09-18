export class Kata {
    /* Welcome. In this kata, you are asked to square every digit of a number and concatenate them.*/
    static squareDigits(num: number): number {
        const numSplitToString = num.toString().split("");
        const numArray = numSplitToString.map(Number);
        const squaredArray = numArray.map((num) => num * num);
        const squaredArrayToString = squaredArray.map(String);
        const squaredArrayToStringJoined = squaredArrayToString.join("");
        const squaredArrayToStringJoinedToNumber = Number(squaredArrayToStringJoined);
        return squaredArrayToStringJoinedToNumber;
    }
  }
