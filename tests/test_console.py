#!/usr/bin/python3
"""Defines a class TestHBNBCommandDocs for HBNBCommand class/ console"""
import unittest
import pep8
import console
from console import HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """Tests for HBNBCommand documentation
    """

    def test_console_conforms_pep8(self):
        """Test if console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testconsole_conforms_pep8(self):
        """Test that tests/test_console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring.
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for HBNBCommand class docstring.
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_missing_docstrings(self):
        """Test for missing docstrings in console.py and tests/test_console.py"""
        with open("console.py", "r") as f:
            console_code = f.read()
        with open("tests/test_console.py", "r") as f:
            test_code = f.read()
        self.assertFalse("'''<missing_docstring>'''" in console_code, "Missing docstring in console.py")
        self.assertFalse("'''<missing_docstring>'''" in test_code, "Missing docstring in tests/test_console.py")

    def test_specific_method_docstrings(self):
        """Test the docstrings of specific methods in HBNBCommand"""
        do_help_docstring = HBNBCommand.do_help.__doc__
        self.assertIsNotNone(do_help_docstring, "Missing docstring for do_help method")
        self.assertTrue("Show documentation of a command." in do_help_docstring)

    def test_pep8_violations(self):
        """Test for PEP8 violations in console.py and tests/test_console.py"""
        pep8style = pep8.StyleGuide(quiet=True)

        with open("console.py", "a") as f:
            f.write("#" * 120)

        with open("tests/test_console.py", "a") as f:
            f.write("def test_invalid_indentation():\nprint('Invalid indentation')")

        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 1, "Expected PEP8 violation in console.py")

        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 1, "Expected PEP8 violation in tests/test_console.py")
