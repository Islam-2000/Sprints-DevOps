import sprints.py

class TestFunction(unittest.TestCase):
    def test_my_func(self):
        """
        Test that it outputs mean of even numbers and maximum of floating point numbers or 0 if none exist in list
        """
        
        data = [0, 1, 2, 4, 5, 7.5, 2.5, 3.0]
        result = myFunc(data)
        self.assertEqual(result, [2.0, 3.0])
        

if __name__ == '__main__':
    unittest.main()