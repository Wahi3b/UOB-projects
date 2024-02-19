def calculate_bounce_distance(initial_height, bounciness_index, num_bounces):
    total_distance = initial_height
    for _ in range(num_bounces):
        initial_height *= bounciness_index
        total_distance += 2 * initial_height  # Add both the downward and upward distances
    return total_distance

initial_height = float(input("please enter the initial height of the ball:"))
bounciness_index = float(input("please enter the bouncing index:"))
num_bounces = int(input("please enter number of times that the ball is allowed to bounce:"))

# output
total_distance = calculate_bounce_distance(initial_height, bounciness_index, num_bounces)
print(f"The total distance traveled by the ball is {total_distance:.2f} feet.")
