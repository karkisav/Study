def main():
    time = input("What time is it? ")
    convert(time)
    print(meal_type(time))


def convert(time):
    time = time.split(":")
    hour = time[0]
    minutes = time[1]
    return float(hour) + float(minutes) / 60

def meal_type(time):
    time = time.split(":")
    hour = float(time[0])
    minutes = float(time[1])
    if (hour == 7 and (minutes >= 0 or minutes <= 59)) or (hour == 8 and minutes == 0):
        return "breakfast time"
    elif (hour == 12 and (minutes >= 0 or minutes <= 59)) or (hour == 13 and minutes == 0):
        return "lunch time"
    elif (hour == 18 and (minutes >= 0 or minutes <= 59)) or (hour == 19 and minutes == 0):
        return "dinner time"
    else:
        return



if __name__ == "__main__":
    main()