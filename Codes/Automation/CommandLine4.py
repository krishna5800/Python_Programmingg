# python  CommandLine4.py  11  10

import sys

def main():
    print("Command line arguments are : ")
    
    print(int(sys.argv[1]) + int(sys.argv[2]))

if __name__ == "__main__":
    main()