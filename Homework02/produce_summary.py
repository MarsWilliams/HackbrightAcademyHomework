#imports an argument variable from a Python module
from sys import argv

def main(argv):
    argv = tuple(argv)
    argv = argv[1:]
    my_file = argv[0]
    for i in argv:
        print "Day", i
        my_file = open(my_file)
        report(my_file)
    
def report(my_file):
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0].upper()
        count = words[1]
        amount = words[2]
        
        print "DELIVERED %s %s FOR A TOTAL OF: $%s" % (count,melon, amount)
    my_file.close()
    print "\n",

if __name__ == "__main__":
    main(argv)
