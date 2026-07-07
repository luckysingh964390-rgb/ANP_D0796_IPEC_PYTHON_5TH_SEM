#function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
#main_program
principal = float(input("Enter the principal (in rupees): "))
rate = float(input("Enter the rate (in %): "))
time = float(input("Enter the time  (in years): "))
print("The simple interest is:", calculate_simple_interest(principal, rate, time))