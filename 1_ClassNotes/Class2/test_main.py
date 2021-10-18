

"""
an example of putting simple tests in a __name__ == "__main__"
"""

"""
when import as module, name becomes file name
if run as script in terminal, name is still main

if run as module can do test_main.fun(4,5)
"""



# defining some (trivial) functions here
def fun(x,y):
    return x+y


def fun2(x,y):
    return x-y


if __name__=="__main__":
    # this will only run if run as a script
    print("Running the test")

    assert fun(3,4)==7

    assert fun2(3,4)==-1

    print("the test pass")

