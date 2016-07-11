# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def item_total_cost(tax_default, state, item_cost):
""" Program to calculate item cost including tax

Function checks which state (by abbreviation), determines tax rate, and cost amount.
Function returns the total cost of the item including tax
"""

    tax = 0.0
    item_total_cost = 0


    #test code
    #state = "CA"
    #item_cost = 20
    #state = "TX"
    #state = ""
    #tax_default = 5

    #determine state and set appropriate tax rate

    if state == "CA":
		tax = 0.07
	else:                          # * * * Python shell keeps erroring on indent... can't seem to fix it
                                   # even though I switched to spaces entirely and retyped multiple times
		tax = tax_default * 0.01

	item_total_cost = item_cost + (item_cost * tax)
	
	print "Total cost of item is: $", item_total_cost

	return item_total_cost


#item_total_cost(5, "CA", 20)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


#1a

def is_berry(fruit_name):
""" Fruit berry name checker

Takes a fruit name as a string and returns a boolean if the fruit is a
"strawberry", "cherry", or "blackberry"
"""
    #fruit_name = "cherry"
    ret_value = False

    if fruit_name == "strawberry":
        ret_value = True
    elif fruit_name == "cherry":
        ret_value = True
    elif fruit_name == "blackberry":
        ret_value = True
    else:
        ret_value = False

    return ret_value

#1b

def shipping_cost(fruit_name):
""" Calculate shipping cost

Calculates shipping cost by taking a fruit name as a string, calling the `is_berry()` function 
within the `shipping_cost()` function and returns `0` if ``is_berry()== True``,
and `5` if ``is_berry() == False``.
"""
    is_berry_ret_value = True

    is_berry_ret_value = is_berry("blackberry")

    if is_berry_ret_value == True:
        shipping_cost_ret_value = 0
    else:
        shipping_cost_ret_value = 5

    return shipping_cost_ret_value


#2a

def is_hometown(town_name):
""" Hometown Checker

Function takes a town name as a string and evaluates to `True` if it is your hometown, and `False` otherwise.
"""
    hometown = ""

    print  "Please enter your hometown name: "
    hometown = raw_input()
    
    if town_name = hometown:
        is_hometown_ret_value = True
    else:
        is_hometown_ret_value = False

    # If I had time I could add error handling to see if they actually enter in a name
    # fail if they enter a number, or a town name that starts with a number or a non-letter character

    return is_hometown_ret_value

#2b

def full_name(first_name, last_name):
""" Full Name Merger

Function takes a first and last name as arguments as strings and returns the concatenation
"""
    full_name = ""
    
    #test code
    #first_name = "Hannah"
    #last_name = "Lewbel"

    full_name = first_name + " " + last_name

    #print full_name

    return full_name

#2c

def hometown_greeting(hometown, first_name, last_name):
"""    Hometown Greeting

Takes a home town, a first name, and a last name as strings as arguments, calls both
`is_hometown()` and `full_name()` and prints "Hi, 'full name here',
we're from the same place!", or "Hi 'full name here', where are you 
from?" depending on what `is_hometown()` evaluates to.
"""
    same_place = ""
    full_name = ""

    same_place = is_hometown(hometown)
    full_name = full_name(first_name, last_name)

    print "Hi", full_name
    if same_place == True:
        print "We\'re from the same place!"
    else:
        print "Where are you from?"
        new_hometown = raw_input()

    return None

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x):
"""


"""

    def add(y):
        z = 0

        z = x + y

        return z


    addition_function = add(y)

# ******************** RAN OUT OF TIME HERE *******************




# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################