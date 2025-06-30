#Lab 4

#Task 1: Checking Voting Eligibility Repeatedly 
checking = "yes"

while checking == "yes":
    print("what is your age")
    user_input = input()
    if int(user_input) >= 18:
        print ("Yes you can vote")

    else:
        print("You can't vote")
    print("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2

#Task 2: Checking Multiple Numbers for Positivity or Negativity
list1 = [3, -1, 0, 6, -4]

for x in list1:
    if x > 0:
        print("value is positive")
    elif x < 0:
        print("value is negative")
    else:
        print("number is 0")

#Task 3: Collecting Blocks in Minecraft
inventory = ["stone", "grass", "diamonds", "rotten flesh", "waxed lightly weathered chiseled copper stairs", "raw porkchops", "gold pickaxe", "bucket"]

for i in inventory:
    if i == "diamonds":
        print("You have found diamonds, YOU HIT THE JACKPOT!")
    elif i == "rotten flesh":
        print("you have rotten flesh, dont eat it..")
    elif i == "raw porkchops":
        print("you have raw porkchops ready to cook")
    else:
        print(f"you have {i}")

    



