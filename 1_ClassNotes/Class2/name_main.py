


print("name is: ", __name__)


# defining some functions
def fun(x,y):
    return x+y


# this code will always run:
print("this is outside the name:main blocK")


if __name__ == "__main__":
    # this will only run if run as a script
    print("this is inside the name:main block")

    # and you can call functions here
    print("The result is:",fun(45,32))

