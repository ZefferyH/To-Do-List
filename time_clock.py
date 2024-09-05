import time
def is_valid_time(time_str):

    if len(time_str) != 5 or time_str[2] != ':':
        return False
    hours, minutes = time_str.split(':')
    if hours.isdigit() and minutes.isdigit():
        hour = int(hours)
        minute = int(minutes)
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return True

    return False
def time_difference(time1):
    time1_struct = time.strptime(time1, "%Y-%m-%d %H:%M")
    current_time_struct = time.localtime()
    time1_seconds = time.mktime(time1_struct)
    current_time_seconds = time.mktime(current_time_struct)
    difference_seconds = (current_time_seconds - time1_seconds)
    is_in_future = difference_seconds <= 0
    if is_in_future:
        difference_seconds = difference_seconds * -1
    days = difference_seconds // (24 * 3600)
    difference_seconds_in_day = difference_seconds % (24 * 3600)
    hours = difference_seconds_in_day // 3600
    difference_seconds_in_hour = difference_seconds_in_day % 3600
    minutes = difference_seconds_in_hour // 60


    return {
        'days': int(days),
        'hours': int(hours),
        'minutes': int(minutes),
        'in_future':is_in_future
    }

def task_to_mktime(task):
    time_string = f"{task["date"]} {task["time"]}"
    return datetime_to_mktime(time_string)
def datetime_to_mktime(datetime_str):
    time_format = "%Y-%m-%d %H:%M"
    struct_time = time.strptime(datetime_str, time_format)
    timestamp = time.mktime(struct_time)
    return timestamp
