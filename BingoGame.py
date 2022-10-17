Bingo_card = ["31", "76", "1", "18", "60", "80", "29", "44", "7", "23"]

print("                               READY TO PLAY BINGO?                     ")
print()
print("INSTRUCTIONS: You will receive a Bingo card with 10 numbers ranging from 1-80.")
print("You have to guess which numbers are on the card. ")
print("If the number you enter exists, it will be crossed out. Keep entering numbers until you guess correctly!")
print("When all the numbers have been crossed out, then you have BINGO.")
print()

i = str(input("Press enter to play!"))

while Bingo_card:

    number_input = input("Enter a number between 1 and 80 only! ")

    while number_input in Bingo_card:
        Bingo_card.remove(number_input)
        print("Congrats! Your number matched!")
        break 

    else:
        print("Incorrect! Try again!")

if not Bingo_card:
    print("B I N G O! Thank you for playing!")
