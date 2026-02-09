import sys
import os
import time
import schedule

def fun(DirName):
    pass

def main():
    Border = "-"*50
    print(Border)
    print("------------ Marvellous Data Schield -------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :")
            print("ScriptName.py Time-Interval SourceDirectory")
            print("Time-Interval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else :
            print("Unable to proceed as their is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Data
    elif len(sys.argv) == 3:
        print("Inside project logic")
        print("Time Interval is : ", sys.argv[1])
        print("Directory Name is :", sys.argv[2])

        # Apply the Scheduler 
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])

        print("Data Schield System Started Successfully")
        print("Directory Created With Name : ", sys.argv[2])
        print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("Invalid number of cammand line arguemts")
        print("Unable to proceed as their is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank You For Using Our Script ---------")
    print(Border)

if __name__ == "__main__":
    main()