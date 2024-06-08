i = 1

def fun():
    global i
    print("Inside fun", i)  # error if global i is not mentioned above
    i = i + 1
    fun()           # recursive call


def main():
    fun()


if __name__ == "__main__":
    main()

# Traceback (most recent call last):
#   File "C:\Users\admin\Desktop\Python\Rec5.py", line 15, in <module>
#     main()
#   File "C:\Users\admin\Desktop\Python\Rec5.py", line 11, in main
#     fun()
#   File "C:\Users\admin\Desktop\Python\Rec5.py", line 7, in fun
#     fun()           # recursive call
#     ^^^^^
#   File "C:\Users\admin\Desktop\Python\Rec5.py", line 7, in fun
#     fun()           # recursive call
#     ^^^^^
#   File "C:\Users\admin\Desktop\Python\Rec5.py", line 7, in fun
#     fun()           # recursive call
#     ^^^^^
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded