"""
Merge_sort-Algorithmus implementiert in Python.

Dieser Modul implementiert den klassischen Merge_sort-Algorithmus, mit O(n log n) Zeitkomplexität.

Funktionen:
    merge_sort(arr: list) -> None
        Sortiert die übergebene Liste in-place mit Merge_sort.
Beispiel:
    >>> my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> merge_sort(my_list)
    >>> print(my_list)
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
"""

import matplotlib.pyplot as plt

def merge_sort(arr):   
    if (len(arr) <= 1):
        return            
    
    # Zerteilen der Liste
    mid = len(arr) // 2
    left_list = arr[:mid]
    right_list = arr[mid:]

    # Recursiver Aufruf auf die zwei Teillisten
    merge_sort(left_list)
    merge_sort(right_list)

    # Zusammenführen der sortierten Teillisten --------------------
    left_index = 0
    right_index = 0
    main_index = 0

    # Einfügen des jeweils kleineren Elementes aus linker oder rechter Liste in arr
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            arr[main_index] = left_list[left_index]
            left_index += 1
        else:
            arr[main_index] = right_list[right_index]
            right_index += 1
        main_index += 1

    # Einfügen der übrigen Elemente aus der linken Liste
    while left_index < len(left_list):
        arr[main_index] = left_list[left_index]
        left_index += 1
        main_index += 1

    # Einfügen der übrigen Elemente aus der rechten Liste    
    while right_index < len(right_list):
        arr[main_index] = right_list[right_index]
        right_index += 1
        main_index += 1
    
    return
    
def main():
    # Visualisierung des Beispielaufrufs in einem Plot
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x_values = range(len(my_list))

    # Ploten der UNSORTIERTEN Liste
    plt.plot(x_values, my_list)
    plt.show()
    # Aufruf der Funktion
    merge_sort(my_list)

    # Ploten der SORTIERTEN Liste
    plt.plot(x_values, my_list)
    plt.show()

    return

if __name__ == "__main__":
    main()