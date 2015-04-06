#Defining functions! The indentation pattern for functions is the same
#as loops, if statements. One difference is the first line can be a
#documentation String that is read by document producing tools.
def fibby(n):
    "This is a fibonacci function"
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a,b=b,a+b
    #print()

#A function that returns the value instead of printing it.
#By default a function returns None even if a return value isn't defined anywhere.
def fibbyreturns(n):
    "This is a fibonacci function"
    result=[]
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b=b,a+b
    return result

#try:
#    n = int(input('Give me a number:'))
#    fibby(n)
#except ValueError:
#    print("You need to enter a number!")

#Call fibbyreturns and assign the value to the variable f50
f50 = fibbyreturns(50)
print(f50)

#Functions can also have a variable number of arguements.
#The raise statement seems to exit the function and return an exception named
#OSError which can be caught in a 'try except' statement.
#The following function has variables with defaults except prompt.
#prompt appears to be a string.
def ask_ok(prompt, retries=4, complaint ='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            print('Returning true')
            return True
        if ok in ('n','no','nop','nope'):
            print('Returning false')
            return False
        retries = retries - 1
        print('Retries left:',retries)
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


#Try and catch the error returned by the function. 
try:
    ask_ok('Boogie!:')
except OSError:
    print('You used all the retries!')


#Default values defined within a function are evaluated or assigned its value
#at point the function is defined. IF the variable is assigned a new variable
#after the function has been defined. The variable within the function
#will have the value before it was redefined.
i=5
def f(b,a=i):
    c = a + b
    print('The value of a is',a)
    a = a + b
    print('The value of c defined in the function is',c)
i=90

#Note that the function modifies a but the value of a is not retained
#between function calls. This is due to the scope of the variable and that its
#not mutable. 
f(3)
print('')
f(4)

#If a new value for args is assigned when the function is called, it will accept it.
#f(10)

#If the value of i is changed it will not update the default value of arg in the function.
#i=100
#f(1000)

#If one of the argument variables is a mutable object like
#a list, dictionary or the values of the mutable object will be retained.
#It will NOT revert to its default.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


#If a list is passed to the function, the function will not set the list to empty.
#Mutable objects 
#The default value of a list can be reset using the following statements.

def g(b, L=None):
    if L == None:
        L=[]
    L.append(b)
    return L
print('')
thelist = g(1)
print('No list passed to g()')
print(g(1))
print('Calling function g(1,thelist) and passing thelist to it')
print(g(1,thelist))
print('Assigning list multiple values but not passing it to g(5)')
thelist = [1,2,3,4]
print(g(5))
print('Calling g(5,thelist) but passing thelist')
print(g(5,thelist))


#Keyword Arguments
#
