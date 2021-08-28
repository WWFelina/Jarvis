import unittest
from tests import PluginTest  
from plugins import topmedia


class topmediaTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(topmedia.topmedia)

    def test_invalid_medium(self):
        self.test.run("randomstring")
        self.assertEqual(self.history_say().last_text(), "Please run the command with a valid medium.\nExample: topmedia tv")

    def test_invalid_medium2(self):
        self.test.run("tv1")
        self.assertEqual(self.history_say().last_text(), "Please run the command with a valid medium.\nExample: topmedia tv")

    


if __name__ == '__main__':
    unittest.main()