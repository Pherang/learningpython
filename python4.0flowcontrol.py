#Simple while loop.
a=0
b=5
while (a<b):
    print("Dog doo!")
    a = a + 1


#if elif and else. Note that indentation is required and hard coded to 4 spaces.
try:
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('Mo!')
except ValueError:
    print('Enter an integer!')


#for loop over a list Also prints the length of the word
words = ['cat', 'window', 'defecate']
for w in words:
    print(w, len(w))
print(words)


#Slice notation allows modification of the sequence we're iterating over.
#slice notation is [:] we should make a copy of the original list.
#interesting that I make a copy of the list but both get modified.
#Need to figure out why. April 6 2015
modwords = words
for w in modwords[:]:
    if len(w) > 6:
        modwords.insert(0, w)
print(words)
print(modwords)
print('')


#Range function can be used with numbers
for i in range(10):
    print(i)
    print('fart')
print('')


#Ranges can start at another number and use different increments.
#First parameter in range() function is the start.
#Second parameter is the end.
#Third parameter is the increment.
for i in range(20, 40, 2):
    print(i, 'fart')
    

#We can combine the range function with lists.
#Enumerate() function is more convenient to use in this case.
poem = ['Old','McDonald','had','a','farm','eee I','eee I','ohhh']
for i in range(x,len(poem)):
    print('Line',i, poem[i])


#printing a range just returns an object with the required parameters for the range
print(range(2,10,2))

#listing a range creates the list of values of the range function
#There are uses for this but seem to be more advanced.
print('Make a list out of the above range')
print(list(range(2,10,2)))
print('')           

#The break statement breaks out of the smallest enclosing FOR or WHILE loop.
#Not the IF statement in this example.
#NOTE that ranges operate as "Start at 2, stop before 10" 2,3,4,5,6,7,8,9
#Range(2,2) is an empty range since you start at 2 stop before 2. Not possible.
#This results in the 'for x' loop not even running.
#Note that using continue instead of break causes inner loop to run with
#next interation of range this includes the else portion of the 4 loop.
for n in range(2, 10):
        for x in range (2,n):
            if n % x == 0:
                print('Found non prime!')
                print(n, 'equals',x,'*', n//x)
                continue #break 
        else:
            print(n, 'is a prime number')


#The pass statement can be used as a place holder and allow code to execute.
#And not crash. Without the pass statement below, running this script would crash.

for i in range(2,100):
    pass #Remember to implement something here!


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


