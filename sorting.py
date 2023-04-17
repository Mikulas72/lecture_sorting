import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data ={}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data



def selection_sort(number_array, direction="ascending"):
    for i in range(len(number_array)):
        min_index = i
        for number_index in range(i + 1, len(number_array)):
            if direction == "ascending":
                if number_array[min_index] > number_array[number_index]:
                    min_index = number_index
            elif direction == "descending":
                if number_array[min_index] < number_array[number_index]:
                    min_index = number_index
        number_array[i], number_array[min_index] = number_array[min_index], number_array[i]
    return number_array

def bubble_sort(number_array):
    n = len(number_array)
    for i in range(n - 1):
        for number_index in range(n - i - 1):
            if number_array[number_index] > number_array[number_index + 1]:
                number_array[number_index], number_array[number_index + 1] = number_array[number_index + 1], number_array[number_index]
    return number_array

def insertion_sort(number_array):
    n = len(number_array)
    for i in range(1, n):
        key = number_array[i]
        j = i - 1
        while j >= 0 and number_array[j] > key:
            number_array[j + 1] = number_array[j]
            j = j - 1
        number_array[j + 1] = key
    return number_array


def testovani_implementovanych_funkci():
    my_list = [3, 8, 1, 2, 32]
    my_list.sort()
    print(my_list)

    my_list = [3, 8, 1, 2, 32]
    my_list = sorted(my_list)
    print(my_list)

    my_list = [3, 8, 1, 2, 32]
    my_list = sorted(my_list, reverse=True)
    print(my_list)

    list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
    print(list_of_words)
    list_of_words = sorted(list_of_words, key=len)
    print(list_of_words)

    list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
    list_of_words = sorted(list_of_words, key=str.lower)
    print(list_of_words)

    return

def main():
    data = read_data("numbers.csv")
    print(data)
    sorted_array = selection_sort(data["series_1"].copy())
    sorted_array_reverse = selection_sort(data["series_1"].copy(), direction="descending")
    bubble_array = bubble_sort(data["series_1"].copy())
    insertion_array = insertion_sort(data["series_1"].copy())
    print(data["series_1"])
    print(sorted_array)
#   print(sorted_array_reverse)
#   print(bubble_array)
    print(insertion_array)

if __name__ == '__main__':
    main()