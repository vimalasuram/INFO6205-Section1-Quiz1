import unittest
from BubbleSort import bubble_sort

class BubbleSortTest(unittest.TestCase):
    def test_sorted_array(self):
        """Test if a pre-sorted array remains unchanged."""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test if a reverse-sorted array is sorted correctly."""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """Test if an unsorted array is sorted correctly."""
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])

    def test_single_element_array(self):
        """Test if a single-element array remains unchanged."""
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty_array(self):
        """Test if an empty array remains unchanged."""
        self.assertEqual(bubble_sort([]), [])

    def test_duplicates_in_array(self):
        """Test if an array with duplicate elements is sorted correctly."""
        self.assertEqual(bubble_sort([3, 3, 3, 1, 2, 1]), [1, 1, 2, 3, 3, 3])

    def test_large_numbers(self):
        """Test if an array with large numbers is sorted correctly."""
        self.assertEqual(bubble_sort([1000000, 1, 500, 200000]), [1, 500, 200000, 1000000])

    def test_negative_numbers(self):
        """Test if an array with negative numbers is sorted correctly."""
        self.assertEqual(bubble_sort([-3, -1, -4, -1, -5, -9]), [-9, -5, -4, -3, -1, -1])

if __name__ == "__main__":
    unittest.main()