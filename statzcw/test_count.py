# test_main_script.py
import unittest
import pandas as pd
from count import count

class TestCountFunction(unittest.TestCase):
    def setUp(self):
        """Create temporary CSV files for the tests."""
        self.csv_file = 'test_dataOne.csv'
        self.csv_file2 = 'test_dataTwo.csv'
        self.csv_file3 = 'test_dataThree.csv'
        self.csv_file0 = 'test_dataZero.csv'

        # Create example DataFrames and save them as CSV files
        df1 = pd.DataFrame({
            'A': [1, 2, None],
            'B': [4, 5, 6]
        })
        df2 = pd.DataFrame({
            'A': [7, 8, 9],
            'B': [None, None, None]
        })
        df3 = pd.DataFrame({
            'A': [None, None, None],
            'B': [10, 11, 12]
        })
        df0 = pd.DataFrame({
            'A': [],
            'B': []
        })

        # Save DataFrames as CSVs
        df1.to_csv(self.csv_file, index=False)
        df2.to_csv(self.csv_file2, index=False)
        df3.to_csv(self.csv_file3, index=False)
        df0.to_csv(self.csv_file0, index=False)

    def tearDown(self):
        """Clean up temporary CSV files after tests."""
        import os
        os.remove(self.csv_file)
        os.remove(self.csv_file2)
        os.remove(self.csv_file3)
        os.remove(self.csv_file0)

    def test_count_function(self):
        """Test the count function with various CSV inputs."""
        result1 = count(self.csv_file)
        result2 = count(self.csv_file2)
        result3 = count(self.csv_file3)
        result0 = count(self.csv_file0)

        # Assertions for the first CSV
        self.assertEqual(result1['A'], 2)  # 2 non-null values in column 'A'
        self.assertEqual(result1['B'], 3)  # 3 non-null values in column 'B'

        # Assertions for the second CSV
        self.assertEqual(result2['A'], 3)  # 3 non-null values in column 'A'
        self.assertEqual(result2['B'], 0)  # 0 non-null values in column 'B'

        # Assertions for the third CSV
        self.assertEqual(result3['A'], 0)  # 0 non-null values in column 'A'
        self.assertEqual(result3['B'], 3)  # 3 non-null values in column 'B'

        # Assertions for the empty CSV
        self.assertEqual(result0['A'], 0)  # 0 non-null values in column 'A'
        self.assertEqual(result0['B'], 0)  # 0 non-null values in column 'B'

if __name__ == '__main__':
    unittest.main()