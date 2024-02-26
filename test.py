from datetime import timedelta

# Creating a timedelta object representing 2 hours and 30 minutes
duration = timedelta(hours=4, minutes=30)

# Calculating the total duration in seconds
total_seconds = duration.total_seconds()

print(total_seconds)