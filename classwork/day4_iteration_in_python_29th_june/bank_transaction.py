deposit = 0
withdraw = 0

while True:
    amount = int(input("Enter transaction amount (0 to stop): "))

    if amount == 0:
        break
    elif amount > 0:
        deposit = deposit + amount
    else:
        withdraw = withdraw + amount

print("\nBank Transaction Summary")
print("Total Deposit =", deposit)
print("Total Withdrawal =", withdraw)
print("Final Balance =", deposit + withdraw)