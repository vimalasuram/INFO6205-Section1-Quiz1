def bubble_sort(arr):
    """
    Bubble sort implementation to sort a list in ascending order.

    Args:
        arr (list): The list of integers to sort.

    Returns:
        list: The sorted list.
    """
    def swap(i, j):
        """
        Swap two elements in the list at indices i and j.

        Args:
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1)
    return arr

    # TODO: Implement the bubble sort algorithm below.
    pass
