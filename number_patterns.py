def question_one():
    # array of mumbers
    numbers = [1, 2, 5, 2, 5, 6, 1, 6]

    # create a set to add unique values
    new_numbers = set()

    # loop through numbers
    for num in numbers:
        # see if there's a repeating number in set
        if num in new_numbers:
            print("*" * 60)
            print("The first repeating number is: ", num)
            break
    # add numbers to set
        new_numbers.add(num)

    # numbers in set
    print("*" * 60)
    print("The numbers in the set are: ", new_numbers)
    print("The numbers in the array are: ", numbers)
    print("*" * 60)


def question_two():
    # array of mumbers
    numbers = [1, 2, 5, 2, 5, 6, 1, 6]

    # create a dictionary to add unique values
    number_dict = {}

    # loop through numbers
    for num in numbers:
        # see if there's a repeating number in set
        if num in number_dict:
            number_dict[num] += 1
        else:
            # add numbers to set
            number_dict[num] = 1

    # loop through the dictionary
    # use items() to get the key and value via tuples
    for num, freq in number_dict.items():
        print("*" * 30)
        print(f"Number: {num}, Times Repeated: {freq}")


# call functions with some formatting
print("\n")
question_one()
print("\n")
question_two()
print("\n")
