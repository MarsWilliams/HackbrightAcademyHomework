#opens my_file (user-defined), and prints a report containing only lines from that file that match the day_sorted (user-defined) argument
def main():
    my_file = open(raw_input("What file would you like to open?"))
    day_sorted = raw_input("By which day would you like to sort?")
    for line in my_file:
        line = line.rstrip()
        day = line[0:3].lower()
        if day == day_sorted[0:3].lower():
            print line

#calls the function and passes it the argument variable
main()
