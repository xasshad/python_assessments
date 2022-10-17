user_input = int(input("How many items would you like to store? "))

big_box = int(user_input / 5)
med_box = int((user_input - big_box * 5) / 3)
small_box = user_input - big_box * 5 - med_box * 3

total_box = big_box + med_box + small_box

print("For " + str(user_input) + " items, you will need the following boxes:")
print("Big box: " + str(big_box))
print("Medium box: " + str(med_box))
print("Small box: " + str(small_box))
print("The total amount of boxes you need are: " + str(total_box))