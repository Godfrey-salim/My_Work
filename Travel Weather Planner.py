# Define the variables with example values
# You can change these values to test different scenarios
distance_mi = 5  # example distance in miles
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# Use conditional statements to determine if commuting is possible
if not distance_mi:  # Check for falsy value (0, None, etc.)
    print(False)
elif distance_mi <= 1:
    # Distance is 1 mile or less
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    # Distance is between 1 and 6 miles (excluded 1, included 6)
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    # Distance is greater than 6 miles
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)