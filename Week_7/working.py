#https://cs50.harvard.edu/python/psets/7/working/
import re
import sys


def main():
    print(convert(input("Hours: ")))




def search(s):
    ui = re.search(r"^(\d\d?(?::\d\d)? (?:AM|PM)) to (\d\d?(?::\d\d)? (?:AM|PM))$",s, re.IGNORECASE)

    if ui:
        start = ui.group(1)
        end = ui.group(2)
        return f"{start} to {end}"

    else:
        raise ValueError("ValueError")
        sys.exit()




def convert(s):
    oras = search(s)
    start_time, end_time = oras.upper().split(" TO ")


    #convert the clock-in time or the start time for the shift
    if "AM" in start_time:
        start_time = am_converter(start_time)

    else:
        start_time = pm_converter(start_time)


    if "AM" in end_time:
        end_time = am_converter(end_time)

    else:
        end_time = pm_converter(end_time)

    return f"{start_time} to {end_time}"



def am_converter(s):
    oras = s.removesuffix("AM").strip()
    if ":" in oras:
        hour, minute = oras.split(":")
        try:
            hour = int(hour)
            minute = int(minute)

        except ValueError:
            sys.exit("ValueError")

        if hour == 12:
            hour = 0

        if minute > 59 or hour > 12:
            raise ValueError("ValueError")
            sys.exit()

        return f"{hour:02}:{minute:02}"


    else:
        try:
            hour = int(oras)
            if hour > 12:
                raise ValueError("ValueError")

            if hour == 12:
                hour = 0
        except ValueError:
            sys.exit("ValueError")

        return f"{hour:02}:00"




def pm_converter(s):
    oras = s.removesuffix("PM").strip()
    if ":" in oras:
        hour, minute = oras.split(":")
        try:
            hour = int(hour)
            minute = int(minute)

        except ValueError:
            sys.exit("ValueError")

        if hour == 12:
            hour = 0

        if minute > 59 or hour > 12:
            raise ValueError("ValueError")
            sys.exit()


        return f"{(hour) + 12:02}:{minute:02}"

    else:
        try:
            hour = int(oras)
            if hour > 12:
                raise ValueError("ValueError")
                sys.exit()

            if hour == 12:
                hour = 0

        except ValueError:
            sys.exit("ValueError")

        return f"{(hour) + 12:02}:00"


if __name__ == "__main__":
    main()