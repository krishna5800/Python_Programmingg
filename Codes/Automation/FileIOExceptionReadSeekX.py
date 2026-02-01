# seek(Kuthe, Kuthun)
# Kuthun : 0 / 1 / 2
# 0 : Starting
# 1 : Current
# 2 : End

def main():
    try :
        fobj = open("Hello.txt", "r")
        print("File gets successfully opened")

        print("Current Offset is : ", fobj.tell())      # 0

        fobj.seek(7, 0)

        print("Current Offset is : ", fobj.tell())      # 7

        Data = fobj.read(10)

        print("Current Offset is : ", fobj.tell())      # 17

        print("Data from file is : ", Data)

        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as their is no such file")
        
    finally:
        print("END OF APPLICATION")
        
if __name__ == "__main__":
    main()