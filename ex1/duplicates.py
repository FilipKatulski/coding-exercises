"""
This script contains a function that takes a list of strings and returns a list of duplicated instances,
in order of their first appearance.
"""

list1 = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
list2 = ["mama", "papa", "bro", "bro","mama", "sis"]
list3 = [2, 1, 3, 3, 5, 1, 3, 4, 3, 4]

def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        # check if the element is in the rest of the list and not already in the duplicates list
        if lst[i] in lst[i+1:] and lst[i] not in duplicates:
            duplicates.append(lst[i])
    return duplicates


def main():
    print(find_duplicates(list1))
    print(find_duplicates(list2))
    print(find_duplicates(list3))

if __name__ == "__main__":
    main()
