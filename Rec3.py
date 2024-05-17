def fun():
    print("Inside fun")
    fun()           # recursive call


def main():
    fun()


if __name__ == "__main__":
    main()