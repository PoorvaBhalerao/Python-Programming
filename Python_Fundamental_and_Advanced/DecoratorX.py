# Predefined function
def sub(A, B):  # 0x100(hashcode)
    print(A-B)

# Decorator for sub fun
def SmartSub(fptr):     # 0x200
    def Inner(A, B):    # 0x300
        if A < B:
            A,B = B,A       # swap
        return fptr(A,B)
    return Inner        # return 0x300

sub = SmartSub(sub)     # at first this line runs because it is at indentation 0
                        # SmartSun(0x100)
                        # (0x100) copied to fptr
                        
def main():     # 0x400
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    sub(No1, No2)       # 0x300(1990, 1992)

if __name__ == "__main__":
    main()