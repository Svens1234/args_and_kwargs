#def myfunc(a,b,c=0,d=0,e=0):
    #return sum((a,b,c,d,e)) * 0.05


#print(myfunc(40, 60, 100, 100, 3))


#def myfunc(a,b,c=0,d=0,e=0):
    #return sum((a,b,c,d,e)) * 0.05


#print(myfunc(40, 60, 100, 100, 3,4))


#def myfunc(*args):
    #return sum(args) * 0.05


#print(myfunc(40,60))
#print(myfunc(40,60,100))


#def myfunc(*args):
    #print(args)


#myfunc(40,60,100)


#def myfunc(*args):
    #for item in args:
        #print(item)


#myfunc(40,60,100,58,79)


#def myfunc(**kwargs):
    #print(kwargs)
    #if 'fruit' in kwargs:
        #print('My fruit of choice is {}'.format(kwargs['fruit']))
    #else:
        #print('I did not find any fruit here')


#myfunc(fruit='apple', veggie = 'lettuce')


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'. format(args[0], kwargs['food']))


myfunc(10,20,30, fruit='orange', food = 'eggs', animal = 'dog')

