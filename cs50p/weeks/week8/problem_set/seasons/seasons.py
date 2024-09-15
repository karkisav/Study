from datetime import date, timedelta
import inflect
import sys

class DateToMins():
    def __init__(self, text):
        self.text = text


    def valid(self):
        try:
            return date.fromisoformat(self.text)
        except (ValueError, AttributeError):
            sys.exit("Invalid date")

    def __str__(self):
        return f"{date.fromisoformat(self.text)}"
    
    def __sub__(self, other):
        if self.valid():
            return abs(date.fromisoformat(self.text) - other)
        
    def convert_to_min(self, delta):
        try:
            if isinstance(delta, timedelta):
                return delta.total_seconds()/60
        except ValueError:
            sys.exit("Invalid date")

    def min_to_words(self, sec):
        try:
            sec = int(sec)
            p = inflect.engine()
            return p.number_to_words(sec, andword="").capitalize() + " minutes"
        except (ValueError, TypeError):
            sys.exit("Can only opeerate on int")

    @classmethod
    def get(cls):
        text = input("Date of Birth: ")
        return cls(text)


def main():
    time = DateToMins.get()
    today = date.today()

    delta = time - today

    delta_seconds = time.convert_to_min(delta)
    print(time.min_to_words(delta_seconds))
    

if __name__ == "__main__":
    main()