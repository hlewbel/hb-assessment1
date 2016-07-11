"""List Assessment - Definitions of functions that modify input arguments such as lists

Functions are:
all_odd - return a list of only the odd numbers in the input list
print_indicies - Print index of each item in list, followed by item itself.
foods_in_common - Find foods in common.
every_other_item - Return every other item in `items`, starting at first item.
largest_n_items - Return the `n` largest integers in list, in ascending order.


Hannah Lewbel
Hackbright Summer 2016 - Grace
2016_07_10 - Assessment 1: List Assessment
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    # numbers = [1,2,3,4,5,6] -- test numbers for checking functionality
    odd_numbers = []
    all_numbers = []

    all_numbers = numbers    #assign variable all_numbers to list passed into the function
    print all_numbers

    #iterate over the list of all_numbers and extract only odd numbers and store them in the odd_numbers list
    for number in all_numbers:
        if number % 2 == 1:     #if mod returns a 1 then number is odd
            odd_numbers.append(number)

    # print odd_numbers -- printed to screen for checking functionality
    
    return odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    # test code:
    # items = ["Toyota", "Jeep", "Volvo"]

    #loop over list and print out index and item name
    for item in items:
        print items.index(item), " ", item

    return None #assume returning None since it wasn't stated in the DocString comments

def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # Trying a few ways to do this:
    # Option 0: Add all items in both function args to a single set which eliminates dupes, alphabetize as list
    # Option 1: Try working this with tuples... 
    # Option 2: Iterate over two lists and compare each item in first list to all the items in second
        # then second item in first list to all the elements in second list, and iterate... seems inefficient
        # also would have issues unless determine which list is longer to make sure don't miss elements while looping

    # CODE FOR OPTION 0:        -- try to do it first with a set but output is not in specific order

    all_foods_list = []                     # create a list we can use to alphabetically sort foods list

    all_foods_set = set()                   # define set of all_foods and initialize it to eliminate dupes
                                            # NOTE: tried using both ([]) and {} for original declaration


    #test code for debugging
    #foods1 = (["cheese", "bagel", "cake", "kale"])
    #foods2 = (["hummus", "beets", "bagel", "lentils", "kale"])

    all_foods_set = foods1 + foods2         #create single set of all foods, which eliminates dupes
    #print set(all_foods_set)               # test code to sort and alphabetize set and print onscreen

    all_foods_list = set(all_foods_set)     # add the contents of the set to a list
    #print all_foods_list                   #test code

    all_foods_list = sorted(all_foods_list) #sort list alphabetically
    #print all_foods_list                   #test code

    return all_foods_list


 # CODE FOR OPTION 1:      --- started working with tuples and went back to option 0

    #all_foods = []                          # define tuple of all_foods and initialize it

    #test code for simple test - works
    #foods1 = ("cheese", "bagel", "cake", "kale")
    #foods2 = ("hummus", "beets", "bagel", "lentils", "kale")

    #all_foods = foods1 + foods2            #create single set of all foods, which eliminates dupes
    #print sorted(all_foods)          # test code to sort and alphabetize set and print onscreen

    #print all_foods
    
    #return (sorted(all_foods))


    # CODE FOR OPTION 2: -- * * * DID NOT COMPLETE BECAUSE GOT CODE WORKING IN OPTION 1 * * *

    # consider using a tuple because don't need to iterate over 
    # test code - ensure some match by position and some match by letter, and both lists are diff lengths
    # define these as tuples in order to check "in" the tuple to see if there's a match
    #foods1 = ('q', 'r', 'b', 'c', 'a', 'd')
    #foods2 = ('q', 'r', 'd', 'b', 'a')

    #new_foods1 = foods1
    #new_foods2 = foods2

    #sorted(foods1)

    # try "if foods1 is in foods2" -- may need to do also "if foods2 is in foods1" after...
    # check if foods1 is greater or less than length of foods2 so do that number of checks
    # can do this by running the for loop twice and then removing any duplicates - seems inefficient

    # if food are in common then add to output list
        #alphabetize list - maybe do at end - try both ways
    #for food1 in foods1 & food2 in foods2:
    #    if (food1 in foods1) == (food2 in foods2):
    #        common_items_alpha.append(food1)

        # else if no foods in common return empty list
    #    else:
    #        common_items_alpha = []

    # alphabetize list
    #sorted(common_items_alpha)

    #return common_items_alpha


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    return items[::2]       # return every other item in items starting at the first item


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    # Outline:
    # take passed in items and n from function args
    # sort list of integers by greatest to smallest (descending order)
    # take descending list from beginning to n in order and return these values again in reverse
    # NOTE: seems like it should be n+1 since a [:n] shouldn't include n, but when run the code seems to produce
    # the desired output of correct number of elements

    #test code
    #n = 5
    #n = 0

    largest_n_items_reversed = []
    largest_items_ascending = []
    
    #test code
    #items = (2, 6006, 700, 42, 6, 59)
    #items = (2, 6006, 700, 42, 6, 59, 3, 6, 7, 877, 898797)
    #items = (3, 3, 3, 2, 1)
    #print items

    largest_n_items_reversed = sorted(items, reverse=True)
    #print largest_n_items_reversed[:]


    largest_items_ascending = sorted(largest_n_items_reversed[:n], reverse=False)
    #print largest_items_ascending

    return largest_items_ascending


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
