import argparse
import random

##### Arg Parsing #####

parser = argparse.ArgumentParser(description='Generate a Password.')

parser.add_argument('--length', '-l', action='store_true', help='Length of the password')
parser.add_argument('--specialchars', '-s', action='store_false', help='Exclude special chars in password.')
parser.add_argument('--lowercase', '-lc', action='store_false', help='Exclude lowercase letters in password.')
parser.add_argument('--uppercase', '-u', action='store_false', help='Exclude uppercase letters in password.')
parser.add_argument('--integers', '-i', action='store_false', help='Exclude integers in password.')

args = parser.parse_args()


##### Setting Variables #####

lowercaseList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
integersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialcharsList = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


##### Creating character list to select chars for password #####

passCharList = []

if args.lowercase:
    passCharList += lowercaseList
if args.uppercase:
    passCharList += uppercaseList
if args.integers:
    passCharList += integersList
if args.specialchars:
    passCharList += specialcharsList


##### Print Password #####

if __name__ == "__main__":
    if args.length == False:
        print("Since no length argument was stated, the default length was set to: 9")
        args.length = 9
        
    print()
    print("Generated Password: " + "".join(random.sample(passCharList, args.length)))
    print()

    input("Press ENTER Key to Exit...")

    exit()