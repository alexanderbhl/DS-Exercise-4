def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

def main():
    # Visualisierung des Beispielaufrufs in einem Plot
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
    # Kopie für 
    unsorted_list = my_list.copy()

    # Erstelle die Grafik mit zwei Subplots in einer Reihe
    plt.figure(figsize=(12, 5))

    # Plot 1: Unsortierte Liste
    plt.subplot(1, 2, 1)
    x = range(len(unsorted_list))
    plt.bar(x, unsorted_list)
    plt.title("Unsortierte Liste", fontsize=14, fontweight='bold')
    plt.xlabel("Index", fontsize=12)
    plt.ylabel("Wert", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xlim(-0.5, len(unsorted_list) - 0.5)  # Gleiche x-Achse für beide Plots
    plt.ylim(min(unsorted_list) - 10, max(unsorted_list) + 10)  # Gleiche y-Achse

    # Plot 2: Sortierte Liste
    plt.subplot(1, 2, 2)
    mergeSort(my_list)  # Sortiere die Liste
    plt.bar(x, my_list, color='orange') 
    plt.title("Sortierte Liste (Mergesort)", fontsize=14, fontweight='bold')
    plt.xlabel("Index", fontsize=12)
    plt.ylabel("Wert", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xlim(-0.5, len(my_list) - 0.5)
    plt.ylim(min(unsorted_list) - 10, max(unsorted_list) + 10)  # Gleiche y-Achse

    # Überschrift für die gesamte Grafik
    plt.suptitle("Vergleich: Unsortiert vs. Sortiert (Mergesort)",
                fontsize=16, fontweight='bold', y=1.02)

    # Automatische Anpassung der Layouts
    plt.tight_layout()

    # Anzeigen der Grafik
    plt.show()

    return

if __name__ == "__main__":
    main()
