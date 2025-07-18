def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Number must be greater than zero. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

def main():
    print("💰 Welcome to the Advanced Bill Splitter 💰")

    total_bill = get_float_input("Enter the total bill amount: ₹")

    tip_percentage = get_float_input("Enter tip percentage (0 if no tip): ")
    total_tip = total_bill * (tip_percentage / 100)
    total_bill_with_tip = total_bill + total_tip

    num_people = get_int_input("Enter number of people to split the bill: ")

    people = []
    paid_amounts = []

    print("\nPlease enter each person's name and the amount they paid:")
    for i in range(num_people):
        name = input(f"\nEnter name of person {i+1}: ").strip()
        if not name:
            name = f"Person {i+1}"
        amount_paid = get_float_input(f"How much did {name} pay? ₹")
        people.append(name)
        paid_amounts.append(amount_paid)

    equal_share = round(total_bill_with_tip / num_people, 2)

    print("\n🧾 Bill Summary:")
    print(f"Original Bill: ₹{total_bill:.2f}")
    print(f"Tip ({tip_percentage}%): ₹{total_tip:.2f}")
    print(f"Total Amount (with tip): ₹{total_bill_with_tip:.2f}")
    print(f"Equal Share Per Person: ₹{equal_share:.2f}\n")

    print("📊 Individual Balances:")
    for i in range(num_people):
        balance = round(paid_amounts[i] - equal_share, 2)
        if balance > 0:
            print(f"{people[i]} should receive ₹{balance:.2f}")
        elif balance < 0:
            print(f"{people[i]} should pay ₹{abs(balance):.2f}")
        else:
            print(f"{people[i]} is settled up.")

if __name__ == "__main__":
    main()
