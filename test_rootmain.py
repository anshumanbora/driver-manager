import unittest
import rootmain
from driver import Driver

class TestRootmain(unittest.TestCase):
    def test_calculate_time(self):
        self.assertEqual(rootmain.calculate_time('00:00','00:00'),0)
        self.assertEqual(rootmain.calculate_time('23:59','23:59'),0)
        self.assertEqual(rootmain.calculate_time('17:50', '20:55'), 185)
        self.assertEqual(rootmain.calculate_time('00:20', '07:06'), 406)
        self.assertEqual(rootmain.calculate_time('00:00', '23:59'), 1439)

    def test_create_object(self):
        self.assertTrue(rootmain.create_object(['Driver','Alex'],{}))

    def test_fill_object(self):
        new_object = Driver()
        new_object.name = 'Dan'
        self.assertTrue(rootmain.fill_object(['Trip','Dan','00:15','00:45','17.3'],{'Dan':new_object}))

    def test_read_write(self):
        self.assertRaises(FileNotFoundError,rootmain.read_write('input.txt','output.txt',{}))
        self.assertRaises(FileNotFoundError, rootmain.read_write('', 'output.txt', {}))
        self.assertRaises(FileNotFoundError, rootmain.read_write('input.txt', '', {}))
        self.assertRaises(FileNotFoundError, rootmain.read_write('', '', {}))

if __name__=="__main__":
    unittest.main()
