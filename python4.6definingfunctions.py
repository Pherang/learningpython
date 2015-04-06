#Defining functions! The indentation pattern for functions is the same
#as loops, if statements. One difference is the first line can be a
#Documentation String that is read by document producing tools.
def fibby(n):
    "This is a fibonacci function"
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a,b=b,a+b
    #print()

#A function that returns the value instead of printing it.
#By default a function returns None even if it isn't defined anywhere.
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


