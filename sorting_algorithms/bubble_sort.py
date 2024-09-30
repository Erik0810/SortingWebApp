class BubbleSort:
    def sort(self, array):
        n = len(array)
        steps = []

        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]  # Swap
                    swapped = True
                steps.append(array.copy())  # Store the current step

            if not swapped:
                break  # If no two elements were swapped, the array is sorted
        return steps
