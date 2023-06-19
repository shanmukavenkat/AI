j1_capacity = int(input("Enter the capacity of Jug 1 in liters: "))
j2_capacity = int(input("Enter the capacity of Jug 2 in liters: "))
target_amount = int(input("Enter the required amount of water in Jug 1: "))

jug1 = 0
jug2 = 0

print("Initial state: Jug 1 =", jug1, "liters,", "Jug 2 =", jug2, "liters")
print("RULE 1jug1")
print("RULE ")

while jug1 != target_amount:
    choice = int(input("Choose a rule to apply: "))

    if choice == 1:  # Fill Jug 1
        jug1 = j1_capacity
    elif choice == 2:  # Fill Jug 2
        jug2 = j2_capacity
    elif choice == 3:  # Pour water from Jug 1 to Jug 2
        amount_to_pour = min(jug1, j2_capacity - jug2)
        jug1 -= amount_to_pour
        jug2 += amount_to_pour
    elif choice == 4:  # Pour water from Jug 2 to Jug 1
        amount_to_pour = min(jug2, j1_capacity - jug1)
        jug2 -= amount_to_pour
        jug1 += amount_to_pour
    elif choice == 5:  # Empty Jug 1
        jug1 = 0
    elif choice == 6:  # Empty Jug 2
        jug2 = 0
    else:
        print("Invalid choice! Please choose a valid rule.")

    print("Current state: Jug 1 =", jug1, "liters,", "Jug 2 =", jug2, "liters")

print("Goal achieved! The required amount of water in Jug 1 has been reached.")
