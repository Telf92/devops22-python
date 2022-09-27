total_seconds = int(input("Please enter amount of seconds: "))
seconds_in_a_day = 60*60*24
nbr_of_days = total_seconds/seconds_in_a_day
print(nbr_of_days)

seconds= total_seconds % seconds_in_a_day
seconds_in_an_hour = 60*60
nbr_of_hours = seconds // seconds_in_an_hour
print(nbr_of_hours)
seconds = seconds % seconds_in_an_hour
print(seconds)