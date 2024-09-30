class QuickSort:
    def sort(self, array):
        if len(array) <= 1:
            return [array]  # No steps needed for arrays with 0 or 1 element
        steps = []
        self._quick_sort(array, 0, len(array) - 1, steps)
        return steps

    def _quick_sort(self, array, low, high, steps):
        if low < high:
            pi = self._partition(array, low, high, steps)
            self._quick_sort(array, low, pi - 1, steps)
            self._quick_sort(array, pi + 1, high, steps)

    def _partition(self, array, low, high, steps):
        pivot = array[high]  # Choosing the rightmost element as pivot
        i = low - 1  # Index of the smaller element
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]  # Swap
        array[i + 1], array[high] = array[high], array[i + 1]  # Move pivot to the correct position
        steps.append(array.copy())  # Append the current state of the array to steps
        return i + 1  # Return the partitioning index