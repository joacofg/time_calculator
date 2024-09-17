def add_time(start, duration, day_of_week=None):
    # Define variables for AM/PM and days of the week
    am_pm = start.split()[1]
    days_of_week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # Split the start time into hours and minutes
    start_hour, start_minute = map(int, start.split()[0].split(':'))
    
    # Split the duration time into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour format for easier calculations
    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12
    elif am_pm == 'AM' and start_hour == 12:
        start_hour = 0

    # Add the duration to the start time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60
    
    # Calculate the number of days that have passed
    days_later = end_hour // 24
    end_hour %= 24

    # Determine AM or PM for the resulting time
    if end_hour == 0:
        final_am_pm = 'AM'
        final_hour = 12
    elif end_hour < 12:
        final_am_pm = 'AM'
        final_hour = end_hour
    elif end_hour == 12:
        final_am_pm = 'PM'
        final_hour = 12
    else:
        final_am_pm = 'PM'
        final_hour = end_hour - 12

    # Format the final time string
    new_time = f"{final_hour}:{end_minute:02d} {final_am_pm}"

    # Add the day of the week, if provided
    if day_of_week:
        day_of_week_index = (days_of_week_list.index(day_of_week.capitalize()) + days_later) % 7
        new_day_of_week = days_of_week_list[day_of_week_index]
        new_time += f", {new_day_of_week}"

    # Add information about the number of days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
print(add_time('3:00 PM', '3:10'))