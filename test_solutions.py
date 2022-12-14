import unittest
import solutions
from solutions import ListNode
from solutions import TreeNode
from solutions import Node


class TestClass(unittest.TestCase):
    def test_detect_cycle(self):
        # [3,2,0,-4]
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next
        self.assertEqual(solutions.detect_cycle(head), head.next)

        # [1,2]
        head2 = ListNode(1)
        head2.next = ListNode(2)
        head2.next.next = head2
        self.assertEqual(solutions.detect_cycle(head2), head2)

    def test_middle_node(self):
        # [1,2,3,4,5]
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        l.next.next.next = ListNode(4)
        l.next.next.next.next = ListNode(5)

        result = solutions.middle_node(l)
        # [3,4,5]
        self.assertEqual(result.val, 3)
        self.assertEqual(result.next.val, 4)
        self.assertEqual(result.next.next.val, 5)

        l2 = ListNode(1)
        l2.next = ListNode(2)
        l2.next.next = ListNode(3)
        l2.next.next.next = ListNode(4)
        l2.next.next.next.next = ListNode(5)
        l2.next.next.next.next.next = ListNode(6)

        result2 = solutions.middle_node(l2)
        # [4,5,6]
        self.assertEqual(result2.val, 4)
        self.assertEqual(result2.next.val, 5)
        self.assertEqual(result2.next.next.val, 6)
    def test_search(self):
        self.assertEqual(solutions.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(solutions.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_preorder(self):
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        self.assertEqual(solutions.preorder(root), [1, 3, 5, 6, 2, 4])

    def test_level_order(self):
        # [3,9,20,null,null,15,7]
        tree = solutions.TreeNode(3)
        tree.left = solutions.TreeNode(9)
        tree.right = solutions.TreeNode(20)
        tree.right.left = solutions.TreeNode(15)
        tree.right.right = solutions.TreeNode(7)
        self.assertEqual(solutions.level_order_iterative(tree), [[3], [9, 20], [15, 7]])

    def test_longest_palindrome(self):
        self.assertEqual(solutions.longest_palindrome("a"), 1)
        self.assertEqual(solutions.longest_palindrome("abccccdd"), 7)
        self.assertEqual(solutions.longest_palindrome("ccc"), 3)
        self.assertEqual(solutions.longest_palindrome("bananas"), 5)

    def test_max_profit(self):
        self.assertEqual(solutions.max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(solutions.max_profit([7, 6, 4, 3, 1]), 0)

    def test_reverse_list(self):
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        l.next.next.next = ListNode(4)
        l.next.next.next.next = ListNode(5)
        result = solutions.reverse_list(l)
        self.assertEqual(result.val, 5)
        self.assertEqual(result.next.val, 4)

    def test_merge_two_lists(self):
        # [1,2,4]
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        # [1,3,4]
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        result = solutions.merge_two_lists(l1, l2)
        # [1,1,2,3,4,4]
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)

    def test_is_subsequence(self):
        self.assertEqual(solutions.is_subsequence("abc", "ahbgdc"), True)
        self.assertEqual(solutions.is_subsequence("axc", "ahbgdc"), False)
        self.assertEqual(solutions.is_subsequence("acb", "ahbgdc"), False)

    def test_is_isomorphic(self):
        self.assertEqual(solutions.is_isomorphic("egg", "add"), True)
        self.assertEqual(solutions.is_isomorphic("foo", "bar"), False)
        self.assertEqual(solutions.is_isomorphic("paper", "title"), True)
        self.assertEqual(solutions.is_isomorphic("ab", "aa"), False)
        self.assertEqual(solutions.is_isomorphic("abab", "baba"), True)

    def test_pivot_ndex(self):
        self.assertEqual(solutions.pivot_index([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(solutions.pivot_index([1, 2, 3]), -1)

    def test_running_sum(self):
        self.assertEqual(solutions.running_sum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(solutions.running_sum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(solutions.running_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])

    def test_is_palindrome(self):
        tests = {121: True, -121: False, 10: False}
        for key, value in tests.items():
            self.assertEqual(solutions.is_palindrome(key), value)

    def test_add(self):
        result = solutions.add(10, 20)
        self.assertEqual(result, 30)

    def test_order(self):
        self.assertEqual(solutions.order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(
            solutions.order("4of Fo1r pe6ople g3ood th5e the2"),
            "Fo1r the2 g3ood 4of th5e pe6ople",
        )
        self.assertEqual(solutions.order(""), "")

    def test_bmi(self):
        self.assertEqual("Underweight", solutions.bmi(50, 1.80))
        self.assertEqual(solutions.bmi(80, 1.80), "Normal")
        self.assertEqual(solutions.bmi(90, 1.80), "Overweight")
        self.assertEqual(solutions.bmi(110, 1.80), "Obese")
        self.assertEqual(solutions.bmi(50, 1.50), "Normal")

    def test_valid_spacing(self):
        self.assertEqual(solutions.valid_spacing2("Hello world"), True)
        self.assertEqual(solutions.valid_spacing2(" Hello world"), False)
        self.assertEqual(solutions.valid_spacing("Hello world  "), False)
        self.assertEqual(solutions.valid_spacing("Hello  world"), False)
        self.assertEqual(solutions.valid_spacing("Hello"), True)
        self.assertEqual(solutions.valid_spacing("Helloworld "), False)
        self.assertEqual(solutions.valid_spacing(" "), False)

    def test_rotateleft(self):
        arr = [1, 2, 3, 4, 5]
        d = 2
        self.assertEqual(solutions.rotateleft(d, arr), [3, 4, 5, 1, 2])

    def test_pig_it(self):  # Simple pig latin
        self.assertEqual(
            solutions.pig_it("Pig latin is cool ?"),
            "igPay atinlay siay oolcay ?",
        )
        self.assertEqual(
            solutions.pig_it("This is my string"), "hisTay siay ymay tringsay"
        )

    def test_solve_element_parity(self):  # Array element Parity
        self.assertEqual(solutions.solve_element_parity([1, -1, 2, -2, 3]), 3)
        self.assertEqual(solutions.solve_element_parity([-3, 1, 2, 3, -1, -4, -2]), -4)
        self.assertEqual(solutions.solve_element_parity([1, -1, 2, -2, 3, 3]), 3)
        self.assertEqual(
            solutions.solve_element_parity(
                [-110, 110, -38, -38, -62, 62, -38, -38, -38]
            ),
            -38,
        )
        self.assertEqual(
            solutions.solve_element_parity([-9, -105, -9, -9, -9, -9, 105]),
            -9,
        )

    def test_fake_binary(self):
        tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]

        for exp, inp in tests:
            self.assertEqual(solutions.fake_binary(inp), exp)

    def test_weather_info(self):  # Grasshopper Debug
        self.assertEqual(
            solutions.weather_info(50), "10.0 is above freezing temperature"
        )
        self.assertEqual(solutions.weather_info(23), "-5.0 is freezing temperature")

    def test_remove_leftmost_duplicates(self):  # Simple Remove Duplicates
        self.assertEqual(
            solutions.remove_leftmost_duplicates([3, 4, 4, 3, 6, 3]),
            [4, 6, 3],
        )
        self.assertEqual(
            solutions.remove_leftmost_duplicates([1, 2, 1, 2, 1, 2, 3]),
            [1, 2, 3],
        )
        self.assertEqual(
            solutions.remove_leftmost_duplicates([1, 2, 3, 4]), [1, 2, 3, 4]
        )
        self.assertEqual(
            solutions.remove_leftmost_duplicates([1, 1, 4, 5, 1, 2, 1]),
            [4, 5, 2, 1],
        )

    def test_user_rank(self):  # Codewars style ranking system
        user = solutions.User()
        user.inc_progress(-7)
        self.assertEqual(user.progress, 10)

        user = solutions.User()
        user.inc_progress(-6)
        self.assertEqual(user.progress, 40)

        user = solutions.User()
        user.inc_progress(-4)
        self.assertEqual(user.rank, -7)
        self.assertEqual(user.progress, 60)

        user = solutions.User()
        user.inc_progress(2)
        user.inc_progress(-7)
        self.assertEqual(user.rank, 1)

        user = solutions.User()
        user.inc_progress(-4)
        self.assertEqual(user.rank, -7)

    def test_rgb(self):  # RGB to HEX Conversion
        self.assertEqual(solutions.rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(solutions.rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(solutions.rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(
            solutions.rgb(254, 253, 252), "FEFDFC", "testing near max values"
        )
        self.assertEqual(
            solutions.rgb(-20, 275, 125),
            "00FF7D",
            "testing out of range values",
        )

    def test_is_pangram(self):  # Detect Pangram
        pangram = "The quick, brown fox jumps over the lazy dog!"
        self.assertTrue(solutions.is_pangram(pangram))
        pangram_2 = "This isn't a pangram! is not a pangram."
        self.assertFalse(solutions.is_pangram(pangram_2))

    def test_valid_parentheses(self):  # Valid Parentheses
        self.assertEqual(solutions.valid_parentheses("  ("), False)
        self.assertEqual(solutions.valid_parentheses(")test"), False)
        self.assertEqual(solutions.valid_parentheses(""), True)
        self.assertEqual(solutions.valid_parentheses("hi())("), False)
        self.assertEqual(solutions.valid_parentheses("hi(hi)()"), True)
        self.assertEqual(
            solutions.valid_parentheses("beljarsbqo)(vpoao)dudxlwjguh(cms"),
            False,
        )
        self.assertEqual(
            solutions.valid_parentheses(
                "(ph)kyienh(((rjxk)(x)zlsdw)mzvmeufm)jd)(pm(x)"
            ),
            False,
        )

        "(ph)kyienh(((rjxk)(x)zlsdw)mzvmeufm)jd)(pm(x)"

        self.assertEqual(solutions.valid_parentheses("l(k(hk)m)"), True)

    def test_solution(self):  # Split Strings
        tests = (
            ("asdfadsf", ["as", "df", "ad", "sf"]),
            ("asdfads", ["as", "df", "ad", "s_"]),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            self.assertEqual(exp, solutions.solution(inp))

    def test_make_readable(self):  # Make Readable
        self.assertEqual("00:00:00", solutions.make_readable(0))
        self.assertEqual("00:00:05", solutions.make_readable(5))
        self.assertEqual("00:01:00", solutions.make_readable(60))
        self.assertEqual("23:59:59", solutions.make_readable(86399))
        self.assertEqual("99:59:59", solutions.make_readable(359999))

    # Do something
    def test_create_phone_number(self):  # Create Phone Number

        self.assertEqual(
            solutions.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
            "(123) 456-7890",
        )
        self.assertEqual(
            solutions.create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            "(111) 111-1111",
        )
        self.assertEqual(
            solutions.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
            "(123) 456-7890",
        )
        self.assertEqual(
            solutions.create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]),
            "(023) 056-0890",
        )
        self.assertEqual(
            solutions.create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            "(000) 000-0000",
        )

    def test_decode_morse(self):
        code = ".... . -.--   .--- ..- -.. ."
        decoded = solutions.decode_morse(code)
        self.assertEqual(decoded, "HEY JUDE")

    def test_find_outlier(self):
        self.assertEqual(solutions.find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(solutions.find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(solutions.find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

        self.assertEqual(
            solutions.find_outlier(
                [
                    -4909475,
                    7195239,
                    6063525,
                    -9012935,
                    -6776165,
                    2381193,
                    7217527,
                    1676863,
                    4084677,
                    400289,
                    -2635775,
                    -5608435,
                    4701513,
                    731861,
                    196403,
                    -3692573,
                    5987535,
                    3131225,
                    1999352,
                    -6749383,
                    -9692083,
                    -6912431,
                    -9658485,
                    -7165165,
                    -7036133,
                    -7233649,
                    -4835191,
                    9412189,
                    6791181,
                    -5193163,
                    4406009,
                    -926235,
                    1624687,
                    -5588751,
                    -4692833,
                    3917503,
                ]
            ),
            1999352,
        )

    def test_song_decoder(self):
        self.assertEqual(
            solutions.song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"),
            "WE ARE THE CHAMPIONS MY FRIEND",
        )

        self.assertEqual(
            solutions.song_decoder("AWUBBWUBC"),
            "A B C",
            "WUB should be replaced by 1 space",
        )
        self.assertEqual(
            solutions.song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
            "A B C",
            "multiples WUB should be replaced by only 1 space",
        )
        self.assertEqual(
            solutions.song_decoder("WUBAWUBBWUBCWUB"),
            "A B C",
            "heading or trailing spaces should be removed",
        )

    def test_digital_root_sum(self):  # Digital Root Sum
        self.assertEqual(solutions.digital_root_sum(7), 7)
        self.assertEqual(solutions.digital_root_sum(16), 7)
        self.assertEqual(solutions.digital_root_sum(456), 6)

    def test_fizz_buzz(self):
        fizzbuzz = 15
        fizz = 3
        buzz = 5

        for i in range(30):
            print(solutions.fizz_buzz(i))
        self.assertEqual(solutions.fizz_buzz(fizzbuzz), "FizzBuzz")
        self.assertEqual(solutions.fizz_buzz(fizz), "Fizz")
        self.assertEqual(solutions.fizz_buzz(buzz), "Buzz")

    def test_fibonacci_generator(self):
        fib_gen = solutions.fibonacci_generator(10)
        first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for fib, num in zip(fib_gen, first_ten):

            self.assertEqual(fib, num)
