# python  CommandLine3.py  11  21  krishna  hitnalikar  98.0897

import sys

def main():
    print("Command line arguments are : ")
    
    for i in range(len(sys.argv)):              # len(sys.argv) -> 6
        print(sys.argv[i])

if __name__ == "__main__":
    main()