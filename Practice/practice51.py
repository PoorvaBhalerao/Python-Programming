# Write a program to accept a character from user if character is small display its corresponding capital character and if character is capital display its small character.
# I/p: a 
# O/p: A



def CaseConversion(ch):

    if('a' <= ch <='z'):
        ch = ch.upper()
    elif('A' <= ch <='Z'):
        ch= ch.lower()

    print(f"Output is: {ch}")
    

def main():

    while True:
        user_input = input("Please enter exactly one character: ")
        if len(user_input) == 1:
            char = user_input
            break
        print("Error: You must enter only one character.")


    CaseConversion(char)


if __name__ == "__main__":
    main()