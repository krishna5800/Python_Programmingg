# 1. Write a program which accepts one character and checks whether it is vowel or consonant.

# Input: a

# Output: Vowel

def ChkVowelOrConsonent(Value):
    Flag = False

    if(Value == 'a' or Value == 'e' or Value == 'i' or Value == 'o' or Value == 'i' or 
       Value == 'A' or Value == 'E' or Value == 'I' or Value == 'O' or Value == 'U'):
        Flag = True

    return Flag

def main():
    Ret = False

    Ret  = ChkVowelOrConsonent('A')

    if(Ret == True):
        print("It is a vowel")
    else:
        print("It is a consonant")

if __name__ == "__main__":
    main()