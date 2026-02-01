

def main():
    try :
        fobj = open("Hello.txt", "r")
        print("File gets successfully opened")

        print("Current Offset is : ", fobj.tell())

        Data = fobj.read(6)

        print("Current Offset is : ", fobj.tell())

        print("Data from file is : ", Data)

        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as their is no such file")
        
    finally:
        print("END OF APPLICATION")
        
if __name__ == "__main__":
    main()