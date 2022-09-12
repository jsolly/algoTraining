import unittest
import codewars_solutions


class TestClass(unittest.TestCase):
    def test_add(self):
        result = codewars_solutions.add(10, 20)
        self.assertEqual(result, 30)

    def test_order(self):
        self.assertEqual(
            codewars_solutions.order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est"
        )
        self.assertEqual(
            codewars_solutions.order("4of Fo1r pe6ople g3ood th5e the2"),
            "Fo1r the2 g3ood 4of th5e pe6ople",
        )
        self.assertEqual(codewars_solutions.order(""), "")

    def test_bmi(self):
        self.assertEqual("Underweight", codewars_solutions.bmi(50, 1.80))
        self.assertEqual(codewars_solutions.bmi(80, 1.80), "Normal")
        self.assertEqual(codewars_solutions.bmi(90, 1.80), "Overweight")
        self.assertEqual(codewars_solutions.bmi(110, 1.80), "Obese")
        self.assertEqual(codewars_solutions.bmi(50, 1.50), "Normal")

    def test_valid_spacing(self):
        self.assertEqual(codewars_solutions.valid_spacing2("Hello world"), True)
        self.assertEqual(codewars_solutions.valid_spacing2(" Hello world"), False)
        self.assertEqual(codewars_solutions.valid_spacing("Hello world  "), False)
        self.assertEqual(codewars_solutions.valid_spacing("Hello  world"), False)
        self.assertEqual(codewars_solutions.valid_spacing("Hello"), True)
        self.assertEqual(codewars_solutions.valid_spacing("Helloworld "), False)
        self.assertEqual(codewars_solutions.valid_spacing(" "), False)

    def test_rotateleft(self):
        arr = [1, 2, 3, 4, 5]
        d = 2
        self.assertEqual(codewars_solutions.rotateleft(d, arr), [3, 4, 5, 1, 2])

    def test_pig_it(self):  # Simple pig latin
        self.assertEqual(
            codewars_solutions.pig_it("Pig latin is cool ?"),
            "igPay atinlay siay oolcay ?",
        )
        self.assertEqual(
            codewars_solutions.pig_it("This is my string"), "hisTay siay ymay tringsay"
        )

    def test_solve_element_parity(self):  # Array element Parity
        self.assertEqual(codewars_solutions.solve_element_parity([1, -1, 2, -2, 3]), 3)
        self.assertEqual(
            codewars_solutions.solve_element_parity([-3, 1, 2, 3, -1, -4, -2]), -4
        )
        self.assertEqual(
            codewars_solutions.solve_element_parity([1, -1, 2, -2, 3, 3]), 3
        )
        self.assertEqual(
            codewars_solutions.solve_element_parity(
                [-110, 110, -38, -38, -62, 62, -38, -38, -38]
            ),
            -38,
        )
        self.assertEqual(
            codewars_solutions.solve_element_parity([-9, -105, -9, -9, -9, -9, 105]),
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
            self.assertEqual(codewars_solutions.fake_binary(inp), exp)

    def test_weather_info(self):  # Grasshopper Debug
        self.assertEqual(
            codewars_solutions.weather_info(50), "10.0 is above freezing temperature"
        )
        self.assertEqual(
            codewars_solutions.weather_info(23), "-5.0 is freezing temperature"
        )

    def test_remove_leftmost_duplicates(self):  # Simple Remove Duplicates
        self.assertEqual(
            codewars_solutions.remove_leftmost_duplicates([3, 4, 4, 3, 6, 3]),
            [4, 6, 3],
        )
        self.assertEqual(
            codewars_solutions.remove_leftmost_duplicates([1, 2, 1, 2, 1, 2, 3]),
            [1, 2, 3],
        )
        self.assertEqual(
            codewars_solutions.remove_leftmost_duplicates([1, 2, 3, 4]), [1, 2, 3, 4]
        )
        self.assertEqual(
            codewars_solutions.remove_leftmost_duplicates([1, 1, 4, 5, 1, 2, 1]),
            [4, 5, 2, 1],
        )

    def test_user_rank(self):  # Codewars style ranking system
        user = codewars_solutions.User()
        user.inc_progress(-7)
        self.assertEqual(user.progress, 10)

        user = codewars_solutions.User()
        user.inc_progress(-6)
        self.assertEqual(user.progress, 40)

        user = codewars_solutions.User()
        user.inc_progress(-4)
        self.assertEqual(user.rank, -7)
        self.assertEqual(user.progress, 60)

        user = codewars_solutions.User()
        user.inc_progress(2)
        user.inc_progress(-7)
        self.assertEqual(user.rank, 1)

        user = codewars_solutions.User()
        user.inc_progress(-4)
        self.assertEqual(user.rank, -7)

    def test_rgb(self):  # RGB to HEX Conversion
        self.assertEqual(
            codewars_solutions.rgb(0, 0, 0), "000000", "testing zero values"
        )
        self.assertEqual(
            codewars_solutions.rgb(1, 2, 3), "010203", "testing near zero values"
        )
        self.assertEqual(
            codewars_solutions.rgb(255, 255, 255), "FFFFFF", "testing max values"
        )
        self.assertEqual(
            codewars_solutions.rgb(254, 253, 252), "FEFDFC", "testing near max values"
        )
        self.assertEqual(
            codewars_solutions.rgb(-20, 275, 125),
            "00FF7D",
            "testing out of range values",
        )

    def test_is_pangram(self):  # Detect Pangram
        pangram = "The quick, brown fox jumps over the lazy dog!"
        self.assertTrue(codewars_solutions.is_pangram(pangram))
        pangram_2 = "This isn't a pangram! is not a pangram."
        self.assertFalse(codewars_solutions.is_pangram(pangram_2))

    def test_valid_parentheses(self):  # Valid Parentheses
        self.assertEqual(codewars_solutions.valid_parentheses("  ("), False)
        self.assertEqual(codewars_solutions.valid_parentheses(")test"), False)
        self.assertEqual(codewars_solutions.valid_parentheses(""), True)
        self.assertEqual(codewars_solutions.valid_parentheses("hi())("), False)
        self.assertEqual(codewars_solutions.valid_parentheses("hi(hi)()"), True)
        self.assertEqual(
            codewars_solutions.valid_parentheses("beljarsbqo)(vpoao)dudxlwjguh(cms"),
            False,
        )
        self.assertEqual(
            codewars_solutions.valid_parentheses(
                "(ph)kyienh(((rjxk)(x)zlsdw)mzvmeufm)jd)(pm(x)"
            ),
            False,
        )

        "(ph)kyienh(((rjxk)(x)zlsdw)mzvmeufm)jd)(pm(x)"

        self.assertEqual(codewars_solutions.valid_parentheses("l(k(hk)m)"), True)

    def test_solution(self):  # Split Strings
        tests = (
            ("asdfadsf", ["as", "df", "ad", "sf"]),
            ("asdfads", ["as", "df", "ad", "s_"]),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            self.assertEqual(exp, codewars_solutions.solution(inp))

    def test_make_readable(self):  # Make Readable
        self.assertEqual("00:00:00", codewars_solutions.make_readable(0))
        self.assertEqual("00:00:05", codewars_solutions.make_readable(5))
        self.assertEqual("00:01:00", codewars_solutions.make_readable(60))
        self.assertEqual("23:59:59", codewars_solutions.make_readable(86399))
        self.assertEqual("99:59:59", codewars_solutions.make_readable(359999))

    # Do something
    def test_create_phone_number(self):  # Create Phone Number

        self.assertEqual(
            codewars_solutions.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
            "(123) 456-7890",
        )
        self.assertEqual(
            codewars_solutions.create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            "(111) 111-1111",
        )
        self.assertEqual(
            codewars_solutions.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
            "(123) 456-7890",
        )
        self.assertEqual(
            codewars_solutions.create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]),
            "(023) 056-0890",
        )
        self.assertEqual(
            codewars_solutions.create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            "(000) 000-0000",
        )

    def test_decode_morse(self):
        code = ".... . -.--   .--- ..- -.. ."
        decoded = codewars_solutions.decode_morse(code)
        self.assertEqual(decoded, "HEY JUDE")

    def test_find_outlier(self):
        self.assertEqual(codewars_solutions.find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(
            codewars_solutions.find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11
        )
        self.assertEqual(
            codewars_solutions.find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160
        )

        self.assertEqual(
            codewars_solutions.find_outlier(
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
            codewars_solutions.song_decoder(
                "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
            ),
            "WE ARE THE CHAMPIONS MY FRIEND",
        )

        self.assertEqual(
            codewars_solutions.song_decoder("AWUBBWUBC"),
            "A B C",
            "WUB should be replaced by 1 space",
        )
        self.assertEqual(
            codewars_solutions.song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
            "A B C",
            "multiples WUB should be replaced by only 1 space",
        )
        self.assertEqual(
            codewars_solutions.song_decoder("WUBAWUBBWUBCWUB"),
            "A B C",
            "heading or trailing spaces should be removed",
        )

    def test_digital_root_sum(self):  # Digital Root Sum
        self.assertEqual(codewars_solutions.digital_root_sum(7), 7)
        self.assertEqual(codewars_solutions.digital_root_sum(16), 7)
        self.assertEqual(codewars_solutions.digital_root_sum(456), 6)

    def test_fizz_buzz(self):
        fizzbuzz = 15
        fizz = 3
        buzz = 5

        for i in range(30):
            print(codewars_solutions.fizz_buzz(i))
        self.assertEqual(codewars_solutions.fizz_buzz(fizzbuzz), "FizzBuzz")
        self.assertEqual(codewars_solutions.fizz_buzz(fizz), "Fizz")
        self.assertEqual(codewars_solutions.fizz_buzz(buzz), "Buzz")

    def test_fibonacci_generator(self):
        fib_gen = codewars_solutions.fibonacci_generator(10)
        first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for fib, num in zip(fib_gen, first_ten):

            self.assertEqual(fib, num)