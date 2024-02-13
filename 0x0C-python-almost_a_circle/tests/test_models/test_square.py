#!/usr/bin/python3
"""Make unittest for class Square

classes of Square:
    __init__
    size
    x
    y
    area
    __str__
    update_args
    update_kwargs
    to_dictionary
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Sq_class(unittest.TestCase):

    def test_Sq_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_Sq_Rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)


class Test_Sq_initali(unittest.TestCase):

    def test_Sq_size(self):
        s1 = Square(5)
        self.assertEqual(5, s1.size)

    def test_Sq_width(self):
        s1 = Square(5)
        self.assertEqual(5, s1.width)

    def test_Sq_height(self):
        s1 = Square(5)
        self.assertEqual(5, s1.height)

    def test_Sq_equal_w_h(self):
        s1 = Square(5)
        self.assertEqual(s1.width, s1.height)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string")

    def test_sq_x(self):
        s1 = Square(1, 2)
        self.assertEqual(2, s1.x)

    def test_sq_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)



    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2})

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "string")

    def test_sq_y(self):
        s1 = Square(1, 2, 3)
        self.assertEqual(3, s1.y)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [1, 2, 3])

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2})

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 2, 3})

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "string")

    def test_sq_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

class Test_Sq__str__(unittest.TestCase):

    def test_Sq__str__(self):
        s1 = Square(3, 1, 3, 4)
        self.assertEqual("[Square] (4) 1/3 - 3", str(s1))

    def test_Sq__str__1(self):
        s1 = Square(3, 5, 3, 4)
        self.assertEqual("[Square] (4) 5/3 - 3", str(s1))

    def test_Sq__str__one(self):
        s1 = Square(5)
        result = "[Square] ({}) 0/0 - 5".format(s1.id)
        self.assertEqual(result, str(s1))

    def test_Sq__str__two(self):
        s1 = Square(3, 1)
        result = "[Square] ({}) 1/0 - 3".format(s1.id)
        self.assertEqual(result, str(s1))

    def test_Sq__str__three(self):
        s1 = Square(3, 1, 4)
        result = "[Square] ({}) 1/4 - 3".format(s1.id)
        self.assertEqual(result, str(s1))

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class Test_Sq_area(unittest.TestCase):

    def test_Sq_int_a(self):
        s1 = Square(5)
        self.assertEqual(25, s1.area())

    def test_Sq_int_a_1(self):
        s1 = Square(3, 1, 4)
        self.assertEqual(9, s1.area())

class Test_Sq_display(unittest.TestCase):

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_Sq_int_d(self):
        s1 = Square(5)
        result = '#####\n#####\n#####\n#####\n#####\n'
        capture = Test_Sq_display.capture_stdout(s1, "display")
        self.assertEqual(result, capture.getvalue())

    def test_Sq_int_d_2(self):
        s = Square(2, 1)
        capture = Test_Sq_display.capture_stdout(s, "display")
        self.assertEqual(" ##\n ##\n", capture.getvalue())


    def test_Sq_int_d_3(self):
        s1 = Square(3, 1, 4)
        result = '\n\n\n\n ###\n ###\n ###\n'
        capture = Test_Sq_display.capture_stdout(s1, "display")
        self.assertEqual(result, capture.getvalue())

    def test_display_size_y(self):
        s1 = Square(4, 0, 1, 9)
        capture = Test_Sq_display.capture_stdout(s1, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s1 = Square(3, 2, 3, 2)
        with self.assertRaises(TypeError):
            s1.display(1)

class Test_Sq_update_args(unittest.TestCase):

    def test_update_id(self):
        s1 = Square(5, 5, 5, 5)
        self.assertEqual(5, s1.id)
        s1.update(10)
        self.assertEqual(10, s1.id)

    def test_update_size(self):
        s1 = Square(1, 2)
        s1.update(10, 10)
        self.assertEqual(10, s1.size)

    def test_update_x(self):
        s1 = Square(1, 2, 3)
        s1.update(10, 10, 10)
        self.assertEqual(10, s1.x)

    def test_update_all(self):
        s1 = Square(1, 2, 3, 4)
        result = "[Square] (4) 2/3 - 1"
        self.assertEqual(result, str(s1))
        s1.update(10, 10, 10, 10)
        result = "[Square] (10) 10/10 - 10"
        self.assertEqual(result, str(s1))

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(1, 2, 3, 4, 5)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        result = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(result, str(s))

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, -3)

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(1, 2, -3)

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(1, 2, 3, -4)



class Test_Sq_update_kwargs(unittest.TestCase):

    def test_update_k_id(self):
        s1 = Square(5)
        s1.update(id=45)
        self.assertEqual(45, s1.id)

    def test_update_k_size(self):
        s1 = Square(5, 5)
        s1.update(size=45)
        self.assertEqual(45, s1.size)

    def test_update_k_x(self):
        s1 = Square(5, 5)
        s1.update(x=45)
        self.assertEqual(45, s1.x)

    def test_update_k_y(self):
        s1 = Square(5, 5, 5)
        s1.update(y=45)
        self.assertEqual(45, s1.y)

    def test_update_all(self):
        s1 = Square(5, 5, 5, 5)
        s1.update(y=3, x=3, size=3, id=3)
        self.assertEqual("[Square] (3) 3/3 - 3", str(s1))

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_str_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="str")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_str_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="str")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_kwargs_str_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="str")

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(5, 4, y=6)
        self.assertEqual("[Square] (5) 10/10 - 4", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

class Test_Sq_to_dictionary(unittest.TestCase):

    def test_to_dictionary_output(self):
        s = Square(1, 2, 3, 4)  
        correct = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertDictEqual(correct, s.to_dictionary())

class Test_Sq_save_to_file(unittest.TestCase):

    def test_Sq_save_to_file_emty(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 2)

    def test_Sq_save_to_file_None(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 2)











if __name__ == "__main__":
    unittest.main()

