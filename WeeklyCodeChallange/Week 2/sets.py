def find_common_elements():
    set1 = set(map(int, input("Enter the first set of numbers separated by spaces: ").split()))
    set2 = set(map(int, input("Enter the second set of numbers separated by spaces: ").split()))

    common_set = set1 & set2  # Using set intersection

    print(f"Common elements: {common_set}")

find_common_elements()
