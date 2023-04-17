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



def selection_sort(number_array):
    for i in range(len(number_array)):
        min_index = i
        for number_index in range(i + 1, len(number_array)):
            if number_array[min_index] > number_array[number_index]:
                min_index = number_index
        number_array[i], number_array[min_index] = number_array[min_index], number_array[i]
    return number_array


def main():
    data = read_data("numbers.csv")
    print(data)
    sorted_array = selection_sort(data["series_1"].copy())
    print(data["series_1"])
    print(sorted_array)

if __name__ == '__main__':
    main()