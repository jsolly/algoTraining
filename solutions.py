import string
from typing import List, Optional
from collections import defaultdict
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def preorder(root: "Node", ans: list = None) -> List[int]:
    if root is None:
        return []

    stack = [root]
    output = []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.children:
            stack.extend(root.children[::-1])

    return output


def level_order_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    queue = [root]
    next_queue = []
    level = []
    result = []
    while queue != []:
        for node in queue:
            level.append(node.val)
            if node.left is not None:
                next_queue.append(node.left)
            if node.right is not None:
                next_queue.append(node.right)
        result.append(level)
        level = []
        queue = next_queue
        next_queue = []
    return result


def level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    d = defaultdict(list)

    def dfs(node, level):
        if node:
            d[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1)

            if node.right:
                dfs(node.right, level + 1)

    dfs(root, 0)

    return list(d.values())


def longest_palindrome(s: str) -> int:
    pairs = 0
    unpaired_chars = set()

    for char in s:
        if char in unpaired_chars:
            pairs += 1
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return pairs * 2 + 1 if unpaired_chars else pairs * 2


def max_profit(prices: List[int]) -> int:
    highest_difference = 0
    min_so_far = prices[0]

    for val in prices[1:]:
        if val < min_so_far:
            min_so_far = val
        else:
            highest_difference = max(highest_difference, val - min_so_far)

    return highest_difference


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        if not next_temp:
            return curr
        prev = curr
        curr = next_temp


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


def is_subsequence(s: str, t: str) -> bool:
    LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

    def rec_isSubsequence(left_index, right_index):
        # base cases
        if left_index == LEFT_BOUND:
            return True
        if right_index == RIGHT_BOUND:
            return False
        # consume both strings or just the target string
        if s[left_index] == t[right_index]:
            left_index += 1
        right_index += 1

        return rec_isSubsequence(left_index, right_index)

    return rec_isSubsequence(0, 0)


def is_isomorphic(s: str, t: str):
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):

        # Case 1: No mapping exists in either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
        # it doesn't match in either of the dictionaries or both
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False

    return True


def pivot_index(nums):
    total = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (total - leftsum - x):
            return i
        leftsum += x
    return -1


def running_sum(nums: List[int]) -> List[int]:
    cumsum = 0
    return [cumsum := cumsum + i for i in nums]


"""Given an integer x, return true if x is palindrome integer."""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    list_x = list(str(x))
    if list_x == list(reversed(list_x)):
        return True

    return False


def add(a, b):
    return a + b


def divTime(r, y, n=0):
    while r >= y:
        r = r - y
        n += 1

    return n


def order(words: str) -> str:
    if not words:
        return ""
    words_split = words.split()
    new_list = [0] * len(words_split)
    for word in words_split:
        for character in word:
            if character.isdigit():
                character_num = int(character)
                new_list[character_num - 1] = str(word)
    return " ".join(new_list)


def bmi(weight: int, height: int) -> str:
    bmi = weight / pow(height, 2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25:
        return "Normal"
    if bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


def valid_spacing2(s):
    s_split = s.split()
    join_s_split = " ".join(s_split)
    if s == join_s_split:
        return True
    else:
        return False


def valid_spacing(s):
    if s == "":
        return True

    if s[0] == " ":
        print("space at beginning")
        return False

    if s[-1] == " ":
        print("space at end")
        return False

    if "  " in s:
        return False

    else:
        return True
        print("I returned True!")


def rotateleft(d, arr):
    while d != 0:
        arr.append(arr.pop(0))
        d -= 1
    return arr


def pig_it(sentence):
    sentence_split = sentence.split(" ")
    pig_sentence = []
    for word in sentence_split:
        if word in string.punctuation:
            pig_sentence.append(word)
        else:
            pig_sentence.append(f"{word[1:]}{word[0]}ay")
    return " ".join(pig_sentence)


def solve_element_parity(arr):
    for number in arr:
        if (number * -1) not in arr:
            return number


def fake_binary(input_string):
    def convert_num(number):
        below = ["0", "1", "2", "3", "4"]

        if number in below:
            return "0"
        return "1"

    new_string = [convert_num(number) for number in input_string]
    return "".join(new_string)


def weather_info(f_temp):
    c_temp = convert_to_celsius(f_temp)
    if c_temp > 0:
        return f"{c_temp} is above freezing temperature"
    else:
        return f"{c_temp} is freezing temperature"


def convert_to_celsius(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp


def remove_leftmost_duplicates(array_obj):
    array_obj.reverse()

    new_list = []

    for element in array_obj:
        if element not in new_list:
            new_list.append(element)

    new_list.reverse()

    return new_list


class User:
    ranks = [rank for rank in range(-8, 9) if rank != 0]

    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.level_index = User.ranks.index(self.rank)

    def check_level(self):
        while self.progress >= 100 and self.rank != User.ranks[-1]:
            self.rank = User.ranks[self.level_index + 1]
            self.level_index += 1
            self.progress -= 100

        if self.rank == 8:
            self.progress = 0

    def inc_progress(self, rank_of_activity):
        activity_level = User.ranks.index(rank_of_activity)
        rank_difference = abs(User.ranks.index(rank_of_activity) - self.level_index)

        if rank_of_activity not in User.ranks:
            raise ValueError

        elif self.rank == User.ranks[-1]:
            return

        elif activity_level < (self.level_index - 1):
            return

        elif rank_difference == 0:
            self.progress += 3

        elif activity_level == (self.level_index - 1):
            self.progress += 1

        else:
            self.progress += 10 * rank_difference * rank_difference

        self.check_level()


def parse_molecule(formula):
    def add_to_element_dict(dict_obj, element, atoms=1) -> dict:
        try:
            dict_obj[element] += int(atoms)
        except KeyError:
            dict_obj[element] = int(atoms)

        return dict_obj

    def smart_combine_dicts(dict_objs: list):
        base_dict = dict_objs[0]

        for dict_obj in dict_objs:
            for element, atoms in dict_obj.items():
                add_to_element_dict(base_dict, element, atoms)

        return base_dict


def rgb(r, g, b):
    def get_hex_from_RGB_val(val):
        hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        if val <= 0:
            return "00"

        elif val > 255:
            return "FF"

        elif 0 < val < 10:
            return f"{val:02}"

        else:
            floor_division_by_16 = val // 16
            remainder = val % 16
            if 10 <= remainder <= 15:
                remainder = hex_dict[remainder]

            if 10 <= floor_division_by_16 <= 15:
                result = f"{hex_dict[floor_division_by_16]}{remainder}"

            elif floor_division_by_16 < 10:
                result = f"{floor_division_by_16}{remainder}"

            return result

    convert = get_hex_from_RGB_val
    return f"{convert(r)}{convert(g)}{convert(b)}"


def is_pangram(s):
    s = s.lower()
    alphabet = string.ascii_lowercase

    if len(set(alphabet).intersection(s)) == 26:
        return True

    return False


def valid_parentheses(s):
    if not s:
        return True
    elif s.count("(") != s.count(")"):
        return False

    parentheses_string = "".join([character for character in s if character in "()"])
    while True:
        parentheses_string = parentheses_string.replace("()", "")
        if parentheses_string == ")(":
            return False
        if parentheses_string == "":
            return True


def solution(s):
    if not s:
        return []

    split_string = [(s[index : index + 2]) for index in range(0, len(s), 2)]

    if len(split_string[-1]) == 1:
        split_string[-1] += "_"
    return split_string


def make_readable(seconds):
    whole_hours = seconds // 3600 if seconds >= 3600 else 0
    remainder_seconds = seconds % 3600
    whole_minutes = remainder_seconds // 60 if 0 < remainder_seconds < 3600 else 0
    whole_seconds = remainder_seconds % 60

    return f"{whole_hours:02}:{whole_minutes:02}:{whole_seconds:02}"


def create_phone_number(numbers: list):
    number_string = "".join(str(digit) for digit in numbers)

    return f"({number_string[:3]}) {number_string[3:6]}-{number_string[6:10]}"


def decode_morse(code):
    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ", ",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
    }

    translated_message = " ".join(
        [
            "".join(
                [morse_code_dict[morse_letter] for morse_letter in morse_word.split()]
            )
            for morse_word in code.split("   ")
        ]
    )

    return translated_message.strip()


def find_outlier(integers: list):
    def check_int_type(integer, int_type):
        remainder = integer % 2
        if remainder == 1 and int_type == "even":
            return False

        elif remainder == 0 and int_type == "odd":
            return False

        else:
            return True

    even_count = 0
    current_type = "even"
    for i in integers[:3]:
        if check_int_type(i, current_type):
            even_count += 1

    current_type = current_type if even_count >= 2 else "odd"

    for number in integers:
        if not check_int_type(number, current_type):
            return number


def song_decoder(song: str):
    removed_wubs = [word for word in song.split("WUB") if word != "WUB"]
    while "" in removed_wubs:
        removed_wubs.remove("")
    final_string = " ".join(removed_wubs)
    return final_string


def digital_root_sum(n):
    while n > 10:
        n = sum((int(n) for n in str(n)))
    return n


def fizz_buzz(num):
    if num == 0:
        return 0

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    elif num % 3 == 0:
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def fibonacci(num):
    a, b = 0, 1

    for i in range(0, num):
        print(a)
        a, b = b, a + b


# Generator examples
def fibonacci_generator(num):
    a, b = 0, 1

    for i in range(0, num):
        yield a
        a, b = b, a + b


def sentence_gen_func(sentence):
    for word in sentence.split():
        yield word


class Sentence1:
    def __init__(self, sentence):
        self.sentence_iterator = iter(sentence.split())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.sentence_iterator)


class Sentence2:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.words[current_index]
