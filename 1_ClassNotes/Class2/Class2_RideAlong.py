## Reading Section

# test "identity" meaning
val1 = 20+30
val2 = 5*10
print(val1==val2)
print(val1 is val2)
print(id(val1))
print(id(val2))
val2 = 54
print(id(val2))

# test function spacing 4 vs tab
def a_func():
    pass
a_func()

def b_func():
    print("b_func worked")
b_func()
print(type(b_func))
print(b_func)

def c_func():
    return 11
    print("this is after return and doesn't get executed") 
answer = c_func()
print(answer)


#num_stars = 4
#for i in range(num_stars):
#    print('*', end=' ') #end= makes it stay in a row


## Video Section


#name is main
print("name is: ",__name__)


def test(a):
    if a == 5:
        print("that's the value I'm looking for!")
    elif a == 7:
        print("that's an OK number")
    else:
        print("that number won't do!")



def hello_name(name):
  return "Hello" and name and "!"


