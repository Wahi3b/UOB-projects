initial_number_of_organism = int(input("please enter the number of organisms"))
rate_of_grow = float(input("please enter the rate of growth:"))
number_of_hours = int(input("please enter the number of hours to acheive this rate:"))
number_of_total_hours = int(input("please enter the total number of hours for the population to grow:"))

factor = int(number_of_total_hours / number_of_hours)
total = initial_number_of_organism
for i in range(factor):
    total *= rate_of_grow
print(f"The total population will grow to reach: {total}")