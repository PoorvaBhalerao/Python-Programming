
def main():
    Ans = 0

    try:
        print("Enter first number: ")       
        No1 = int(input())

        print("Enter first number: ")
        No2 = int(input())

        Ans = No1 / No2

    except ZeroDivisionError as zobj:       #   Specific Exception handler
        print("Exception occured:",zobj)

    except ValueError as vobj:              #   Specific Exception handler
        print("Exception occured:",vobj)

    except Exception as eobj:               #  Generic Exception handler
        print("Exception occured:",eobj)

    finally:                                #   code Written in finally block irrespective of exception is handled or not
        print("Inside finally block")       #   finally block is optional
    
    print("Division is: ",Ans)


if __name__ == "__main__":
    main()