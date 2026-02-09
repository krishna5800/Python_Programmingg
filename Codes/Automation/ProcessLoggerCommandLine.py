# COMMD LINE INPUT

import psutil
import sys

def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance Systems ----")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Execute periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processes")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about Secondary storage")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :")
            print("ScriptName.py Time-Interval DirectoryName")
            print("Time-Interval : The time in minutes for periodic scheduling")
            print("DIrectoryName : Name of directory to create auto-logs")

        else :
            print("Unable to proceed as their is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Marvellous
    elif len(sys.argv) == 3:
        print("Inside project logic")
        print("Time Interval is : ", sys.argv[1])
        print("Directory Name is :", sys.argv[2])

    else:
        print("Invalid number of cammand line arguemts")
        print("Unable to proceed as their is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank You For Using Our Script ---------")
    print(Border)

if __name__ == "__main__":
    main()