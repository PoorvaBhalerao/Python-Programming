# Write a program to accept a character from user if character is small display its corresponding capital character and if character is capital display its small character.
# I/p: r 
# O/p: r    s   t   u   v   w   x   y   z
# I/p: T
#O/p:  T    U   V   W   X   Y   Z

def Display(ch):

    if('a' <= ch <='z'):
        for i in range(ord(ch), ord('z')+1):
            print(chr(i), end ="  ")

    elif('A' <= ch <='Z'):
        for i in range(ord(ch), ord('Z')+1):
            print(chr(i), end ="  ")
    

def main():

    while True:
        user_input = input("Please enter exactly one character: ")
        if len(user_input) == 1:
            char = user_input
            break
        print("Error: You must enter only one character.")


    Display(char)


if __name__ == "__main__":
    main()