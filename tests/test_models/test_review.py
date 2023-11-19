#!/usr/bin/python3
"""test for review"""
import os
import unittest

import pep8

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/review.py"])
        self.assertEqual(pep.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue("id" in self.rev.__dict__)
        self.assertTrue("created_at" in self.rev.__dict__)
        self.assertTrue("updated_at" in self.rev.__dict__)
        self.assertTrue("place_id" in self.rev.__dict__)
        self.assertTrue("text" in self.rev.__dict__)
        self.assertTrue("user_id" in self.rev.__dict__)

    def test_is_subclass_review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(
        os.getenv("HBNB_TYPE_STORAGE") == "db",
        "This test only work in Filestorage",
    )
    def test_save_review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_review(self):
        """test if dictionary works"""
        self.assertEqual("to_dict" in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
