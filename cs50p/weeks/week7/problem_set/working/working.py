import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(hours):
    if matches := re.search(r"^([0-9]{1,2}):?([0-9]{2})? ([AP]M) to ([0-9]{1,2}):?([0-9]{2})? ([AP]M)$", hours):
        hour_1 , hour_2 = 0, 0
        min_1 , min_2 = 00, 00
        try:
            if matches.group(2) is not None:
                min_1 = int(matches.group(2))
            if matches.group(5) is not None:
                min_2 = int(matches.group(5))

            if matches.group(3) == "AM":
                hour_1 = 0 if int(matches.group(1)) == 12 else int(matches.group(1))
                hour_2 = int(matches.group(4)) + 12 if int(matches.group(4)) != 12 else int(matches.group(4))
            else:
                hour_1 = int(matches.group(1)) + 12 if int(matches.group(1)) != 12 else int(matches.group(1))
                hour_2 = 0 if int(matches.group(4)) == 12 else int(matches.group(4))

        except ValueError:
            raise ValueError()     
        
        if not (0 <= hour_1 < 24) or not (0 <= hour_2 < 24) or not (0 <= min_1 < 60) or not (0 <= min_2 < 60):
            raise ValueError()
        
        return f"{hour_1:02}:{min_1:02} to {hour_2:02}:{min_2:02}"
    else:
       raise ValueError()

if __name__ == "__main__":
    main()