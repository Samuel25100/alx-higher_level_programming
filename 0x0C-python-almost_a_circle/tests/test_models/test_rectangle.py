#!/usr/bin/python3
"""Unittest of class Rectangle:
    
all methods in class Rectangle are:
    Rectangle_instantiation
    Rectangle_width
    Rectangle_height
    Rectangle_x
    Rectangle_y
    area
    update_args
    update_kwargs
    to_dictionary
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class Test_Rec_init(unittest.TestCase):
    """Unittest for rectangle initialization."""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)


    def test_id(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_init_width(self):
        with self.assertRaises(TypeError):
            Rectangle('1', 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1.9, 1, 1)
    
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)
    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)
    
    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_init_width_1(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1, 1)

    def test_init_width_2(self):
        r1 = Rectangle(2, 3, 4)
        self.assertEqual(2, r1.width)

    def test_init_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, '1', 1)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))
    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')


    def test_init_height_1(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1.3, 1)

    def test_init_height_2(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1, 1)

    def test_init_height_3(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(2, r1.height)

    def test_init_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, '1', 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_init_x_1(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.2, 2)

    def test_init_x_2(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 2)

    def test_init_x_3(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -27, 2)
    
    def test_init_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, '2')

    def test_init_y_1(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 2.3)

    def test_init_y_2(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -2)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})


class Test_Rec_property(unittest.TestCase):

    def test_prop_width(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(1, r1.width)

    def test_prop_height(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(2, r1.height)

    def test_prop_x(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(3, r1.x)

    def test_prop_y(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(4, r1.y)


class Test_Rec_setter(unittest.TestCase):

    def test_set_width(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(1, r1.width)
        r1.width = 4
        self.assertEqual(4, r1.width)

    def test_set_width_1(self):
        r1 = Rectangle(22, 2)
        self.assertEqual(22, r1.width)
        r1.width = 5
        self.assertEqual(5, r1.width)

    def test_set_width_2(self):
        r1 = Rectangle(22, 2)
        with self.assertRaises(TypeError):
            r1.width = '2'
        with self.assertRaises(TypeError):
            r1.width = 2.5

    def test_set_width_3(self):
        r1 = Rectangle(22, 2)
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.width = -2

    def test_set_height(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(2, r1.height)
        r1.height = 4
        self.assertEqual(4, r1.height)

    def test_set_height_1(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(2, r1.height)
        r1.height = 5
        self.assertEqual(5, r1.height)

    def test_set_height_2(self):
        r1 = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            r1.height = 'is'
        with self.assertRaises(TypeError):
            r1.height = '2'

class Test_Rec_area(unittest.TestCase):

    def test_area(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(2, r1.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())



class Test_Rec_display(unittest.TestCase):

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        result = Test_Rec_display.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", result.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        result = Test_Rec_display.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", result.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        result = Test_Rec_display.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, result.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = Test_Rec_display.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())


class Test_Rec__str__(unittest.TestCase):

    def test__str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        ch = "[Rectangle] (12) 2/1 - 4/6".format()
        self.assertEqual(ch, r1.__str__())
    
    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

class Test_Rec_update_args(unittest.TestCase):

    def test_update_id(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5)
        self.assertEqual(5, r1.id)

    def test_update_width(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5, 5)
        self.assertEqual(5, r1.width)

    def test_update_height(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5, 5, 5)
        self.assertEqual(5, r1.height)

    def test_update_x(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5, 5, 5, 5)
        self.assertEqual(5, r1.x)

    def test_update_y(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5, 5, 5, 5, 5)
        self.assertEqual(5, r1.y)

    def test_update_all(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(5, 5, 5, 5, 5)
        self.assertEqual("[Rectangle] (5) 5/5 - 5/5", str(r1))

class Test_Rec_update_kwarg(unittest.TestCase):

    def test_update_k(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2,id=10, y=3, width=4)
        self.assertEqual("[Rectangle] (10) 1/3 - 4/2", str(r1))

    def test_update_k_one(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/1", str(r1))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))


if __name__ == "__main__":
    unittest.main()
