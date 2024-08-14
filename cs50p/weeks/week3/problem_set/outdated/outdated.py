months = [
    "January", "February", "March", "April", "May", "June", "July", 
    "August", "September", "October", "November", "December"
]

def main():
    date = validate_date("Date: ", months=months)
    print(f"{date[0]}-{date[1]:02d}-{date[2]:02d}")

def validate_date(prompt, months):
    time = []
    while True:
        try:
            date = input(prompt)
            if len(date.split("/")) == 3:
                date = date.split("/")
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])

                if (month <= 0 or month > 12) or (day > 31) or (year / 1000 < 1):
                    pass
                else:
                    time.append(year)
                    time.append(month)
                    time.append(day)
                    return time
            elif len(date.split(" ")) == 3:
                date = date.split(" ")
                datex = date[1]
                
                if ',' in datex:
                    month = date[0]
                    day = int(date[1].strip(","))
                    year = int(date[2])
                    
                    if (month not in months) or (day > 31) or (year / 1000 < 1):
                        pass

                    else:
                        month = months.index(month) + 1
                        time.append(year)
                        time.append(month)
                        time.append(day)
                        return time
                else:
                    pass
        except (EOFError, ValueError):
            pass
main()