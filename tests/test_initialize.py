from tests.base_test import BaseTestCase
from src.initialize import initialize, INIT_RESPONSE

class TestInitialize(BaseTestCase):
    def test_initialize(self):
        assert initialize() == INIT_RESPONSE
