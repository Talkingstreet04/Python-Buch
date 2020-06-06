import getopt
import sys


args = sys.argv[1:]
try:
    optionen, restargumente = getopt.getopt(args, "abc:", ["alpha", "betta", "gamma="])  # Jede option wird zurückgegeben; zusammen mit den eigenen Argumenten
except getopt.GetoptError:
    sys.exit("Argument Error")
    #sys.exit(2)
#nach einem argument welches keine option ist,gelten alle folgenden argumente auch nur als argumente auch wenn sie eine option sein könnten. AUßER man benutzt .gnu_getopt statt nur .getopt
for current_options, current_value in optionen:
    if current_options == "-a":
        print("Alpha aktiviert") # man könnte von hier aus natürlich funktionen über funktionen triggern
    elif current_options == "-b":
        print("Betta aktiviert")
    elif current_options == "-c":
        print("Dein Argument für c war \"", current_value, "\"")
