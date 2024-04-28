
def add_zero():
    if y < 10:
        return ("0")
    else:
        break

# format minutes to 2 digits starting with 0 if only 1 digit
int_hours = int(input("Enter your marathon time hours: "))
int_min = int(input("Enter your marathon time minutes: "))
int_sec = int(input("Enter your marathon time seconds: "))

float_marathon_miles = 26.2188
int_total_sec = (int_hours * 60 * 60) + (int_min * 60) + int_sec
seconds_per_mile = int_total_sec / float_marathon_miles
min_per_mile = seconds_per_mile // 60
left_over_secs_per_mile = add_zero() + str(round(seconds_per_mile % 60))


print(f"Min and secs / mile = {int(min_per_mile)}:{left_over_secs_per_mile}")

