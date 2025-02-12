import random

# Initialise rounds points
user_points = 0
comp_points = 0
double_user = "no"

# Roll the dice for the user and not if they got a double
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

if dice_1 == dice_2:
    double_user = "yes"

# roll the dice for the computer
comp_1 = random.randint(1, 6)
comp_2 = random.randint(1, 6)

if comp_1 == comp_2:
    double_user = "yes"

# Update the user / computer points
user_points += dice_1 + dice_2
comp_points += comp_1 + comp_2



# Output the results
print("\nInitial Points")
print(f"You       - Roll 1: {dice_1}  \t| Roll 2: {dice_2} \t| Total: {user_points}")
print(f"Opponent       - Roll 1: {comp_1}  \t| Roll 2: {comp_2} \t| Total: {comp_points}")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")



