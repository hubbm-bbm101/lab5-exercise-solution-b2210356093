number=int(input("Enter a number: "))
if number < 0:
    print("You can not choose a number less than zero.")
else:
    even = sum(range(2, number+1, 2))
    odd = sum(range(1, number+1, 2))
    average = even / number
    print("Sum of odd numbers: ", odd)
    print("Average of even numbers(approximately): {} / {} = {}".format(even,number,average))

exit = input("Please press enter to exit: ")
