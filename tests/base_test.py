import sys
import os
import unittest


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(SCRIPT_DIR + '/../src/')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseTestCase (unittest.TestCase):

    # executed prior to each test - setUp() is a unittest thing
    def setUp(self):
        return True
    # executed after each test - tearDown() is a unittest thing
    def tearDown(self):
        return True
