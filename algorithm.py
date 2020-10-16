
# # 1. Print 1-255
# # Print1To255()
# # Print all the integers from 1 to 255.
# def print_1_255():
#     for i in range(1, 256):
#         print(i)


# print_1_255()

# # ----------------------------------------------------------------
# # 2. Print Odds 1-255
# # PrintOdds1To255()
# # Print all odd integers from 1 to 255.


# def print_1_255():
#     for i in range(1, 256, 2):
#         print(i)


# print_1_255()
# # ----------------------------------------------------------------

# # 3. Print Ints and Sum 0-255
# # PrintIntsAndSum0To255()
# # Print integers from 0 to 255, and with each integer print the sum so far.


# def printIntsAndSum0To255():
#     sum = 0
#     for i in range(0, 256):
#         sum += i
#         print(sum, i)
# # ----------------------------------------------------------------

# # 4. Iterate and Print Array
# # Iterate through a given array, printing each value.
# # PrintArrayVals(arr)


# def printArrayVals(arr):
#     for i in range():
#         pass


# # ----------------------------------------------------------------

# # 5. Find and Print Max
# # PrintMaxOfArray(arr)
# # Given an array, find and print its largest element.


# def printMaxOfArray(list):
#     max = list[0]
#     for i in range(len(arr)):
#         if list[i] > max:
#             max = list[i]
#     print(max)


# printMaxOfArray([1, 2, 4, 5, 6])

# # ----------------------------------------------------------------

# # 6. Get and Print Average
# # PrintAverageOfArray(arr)
# # Analyze an array’s values and print the average.


# def printAverageOfArray(list):
#     sum = 0
#     for i in range(0, len(list)):
#         sum += list[i]
#     if sum == 0:
#         avg = 0
#     else:
#         avg = sum/len(list)
#     print(avg)


# printAverageOfArray([1, 2, 3])
# printAverageOfArray([])
# # ----------------------------------------------------------------

# # 7. Array with Odds
# # ReturnOddsArray1To255()
# # Create an array with all the odd integers between 1 and 255 (inclusive).
# # ----------------------------------------------------------------

# # 8. Square the Values
# # SquareArrayVals(arr)
# # Square each value in a given array, returning that same array with changed values.


# def SquareArrayVals(arr):
#     for i in range():

#         # ----------------------------------------------------------------

#         # 9. Greater than Y
#         # ReturnArrayCountGreaterThanY(arr, y)
#         # Given an array and a value Y, count and print the number of array values greater than Y.

#         # ----------------------------------------------------------------

#         # 10. Zero Out Negative Numbers
#         # ZeroOutArrayNegativeVals(arr)
#         # Return the given array, after setting any negative values to zero.


# def zero_out(list):
#     for i in range(0):
#         pass
# # ----------------------------------------------------------------

# # 11. Max, Min, Average
# # PrintMaxMinAverageArrayVals(arr)
# # Given an array, print the max, min and average values for that array.


# def max_Min_Avg(list):

#     max = list[0]
#     min = list[0]
#     avg = 0
#     sum = 0
#     for i in list:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#         avg += i
#     avg = avg // len(list)
#     print(max, min, avg)


# max_Min_Avg([1, 2, 3, 4, 5, 6, 7, -8, 9])


# # ----------------------------------------------------------------
# # Acronyms
# # Create a function that, given a string, returns the string’s acronym
# # (first letter of each word capitalized).
# # Input: " there's no free lunch - gotta pay yer way. "
# # Output: "TNFL-GPYW"

# def acronyms(str):
#     ans = ""
#     for i in str.split():
#         ans += i[0].upper()
#     return ans


# print(acronyms(" there's no free lunch - gotta pay yer way. "))

# # ----------------------------------------------------------------


# def reversed_string(str):
#     reversed_string = ""
#     for i in range(len(str), 0, -1):
#         reversed_string += str[i - 1]
#     return reversed_string


# print(reversed_string("creature"))
# print(reversed_string("dog")


#       # String: Is Palindrome
#       # Create a function that returns a boolean whether the string is a strict palindrome.
#       # - palindrome = string that is same forwards and backwards
#       # Do not ignore spaces, punctuation and capitalization
#       # Input: "a x a"
#       # Output: True
#       # Input: "racecar"
#       # Output: True
#       # Input: "Dud"
#       # Output: False

# def Palindrome(input):
#     for char in input:
#         if input[::-1] == input:
#             return True
#         else:
#             return False
# print(Palindrome('racecar'))
# print(Palindrome('a * a'))
# print(Palindrome('Dud'))


#       # Zip List into Map
#       # Given two lists, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
#       # Associative lists are sometimes called maps because a key (string) maps to a value
#       # Input: ["abc", 3, "yo"], [42, "wassup", true]
#       # Output: {
#       #   abc: 42,
#       #   3: "wassup",
#       #   yo: true,
#       # }


# You have a 3 and a 5 litre water container, each
# container has no markings except for that which
# gives you it’s total volume. You also have a running
# tap. You must use the containers and the tap in such
# away as to exactly measure out 4 litres of water.

# How is this done?

# fill the 5 litre container
# use the 5 litre to fill the 3 litre container
# empty 3 ltr container - leaving 2 litre in the 5ltr container
# pour the last 2 litr into 3 litre leaving  1 litre of space
# then you fill up the 5 litrs conatineer and pour another  litre in the 3 litre
# leaving 4 litre left in the 5 ltr container


# A windowless room contains three identical light fixtures,
# each containing an identical light bulb or light globe. Each
# light is connected to one of three switches outside of the
# room. Each bulb is switched off at present. You are outside
# the room, and the door is closed. Before opening the door you
# may play around with the light switches as many times as you
# like. But once you’ve opened the door, you may no longer touch a
# switch. After this, you go into the room and examine the lights.

# How can you tell which switch goes to which light?
#     "Switch on switches 1 &amp; 2, wait a moment and switch off number 2.
#     Enter the room. Whichever bulb is on is wired to switch 1,
#      whichever is off and hot is wired to switch number 2,
#       and the third is wired to switch 3."


#       / *
#       Given an array of strings
#       return a sum to represent how many times each array item is found(a frequency table)
#       Useful methods:
#       Object.hasOwnProperty("keyName")
#       - returns true or false if the object has the key or not
#       Python: dict.has_key(key)
#       * /
#       function frequencyTable(arr){

#     ['A', 'A', 'B', 'C', 'C', 'C', 'D', 'D']=> {"A": 2, "B": 1, "C": 3, "D": 2}
#      ['A', 'C', 'C', 'C', 'D', 'D', 'A', 'B', ]= > {"A": 2, "B": 1, "C": 3, "D": 2}
def frequencyTable(list):
    myDict = {}
    for key in list:
        if key in myDict:
            myDict[key] += 1
        else:
            myDict[key] = 1
    return myDict


print(frequencyTable(['A', 'A', 'B', 'C', 'C', 'C', 'D', 'D']))


#     / *
#     Reverse Word Order
#     Create a function that, given a string of words(with spaces), returns new string with words in reverse sequence.
#     split()
#     * /
#     function reverseWordOrder(string){

# }
#     "THIS IS A TEST"= > "TEST A IS THIS"

# ============================================================
# Parens Valid
# Given an str that has parenthesis in it
# return whether the parenthesis are valid
# Input: "(()())"
# Output: True
# Input: "N(0)t ) 0(k"
# Output: False

def validParens(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


print(validParens("(()())"))
print(validParens('(('))
print(validParens("(()()()"))

# Braces Valid
# Given a string sequence of parentheses, braces and brackets,
# determine whether it is valid.
# Input: "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"
# Output: True
# Input: "D(i{a}l[ t]o)n{e"
# Output: False


def valid_braces(string):


parenOpen, parenClose, brakOpen, brakClose, curlOpen, curlClose = 0, 0, 0, 0, 0, 0
   for i in string:
        if i == '(':
        parenOpen += 1
    elif i == '[':
        brakOpen += 1
    elif i = '{':
        curlOpen += 1
    elif i == ')':
        parenClose += 1
    elif i == ']':
        brakClose += 1
    elif i == '}':
    curlClose += 1
if parenClose > parenOpen or (brakClose > brakOpen or curlClose > curlOpen):
return False


# There are 9 coins, all except one are the same weight,
# the odd one is heavier than the rest. You must determine
# which is the odd one out using an old fashioned balance.
# You may use the balance twice. Explain how this can be done.

Put 1,2 & 3 on the left side and 4,5 & 6 on the right side. There are three possible outcomes:
scale tilts left - means the heavy coin is in group 1,2 & 3
scale tilts right - means the heavy coin is in group 4,5 & 6
scale balances - means the heavy coin is in group 7,8 & 9
We need to do the same again and we will arrive at the final coin.

# Adam, Bob, Clair and Dave are out walking: They come
# to rickety old wooden bridge. The bridge is weak and
# only able to carry the weight of two of them at a time.
# Because they are in a rush and the light is fading they
# must cross in the minimum time possible and must carry
# a torch (flashlight,) on each crossing.

# They only have one torch and it can't be thrown. Because
# of their different fitness levels and some minor injuries
# they can all cross at different speeds.
# Adam can cross in 1 minute,
# Bob in 2 minutes,
# Clair in 5 minutes
# and Dave in 10 minutes.

# Adam, the brains of the group thinks for a moment
# and declares that the crossing can be completed in 17 minutes.
# There is no trick. How is this done?
#         Move	                    Time
# (1) & (2) Cross with Torch	        2
# (1) Returns with Torch	            1
# (5) & (10) Cross with Torch	       10
# (2) Returns with Torch	            2
# (1) & (2) Cross with Torch	        2
#  	    Total                          17




# Binary Search (non recursive)
# Given a sorted list and a value, return whether the list contains that value.
# Do not sequentially iterate the list. Instead, ‘divide and conquer’,
# taking advantage of the fact that the list is sorted .
# Input: [1, 3, 5, 6], 4
# output: False

# Input: [4, 5, 6, 8, 12], 5
# Output: True

# Input: [3, 4, 6, 8, 12], 3
# Output: True
def binary_search(list,value):
	first = 0
	last = len(list)-1








def binary_search(list,value):
	first = 0
	last = len(list)-1    
	while first < last:
	    mid = (first + last)//2
	    if list[mid] == value :
	        return True
	    if value < list[mid]:
	        last = mid - 1
	    else:
	        first = mid + 1    
	    return found	    
print(binary_search([1, 3, 5, 6], 4))


def binary_search(var,x):

  a = len(var)/2
  
  if x <= int(a):
    for i in range(int(a),0,-1 ):
      if var[i] == x:
        result = (f'found value {x} at index {i}')
        return(result)
  if x >= int(a):
    for i in range(int(a), len(var),1 ):
      if var[i] == x:
        result = (f'found value {x} at index {i}')
        return(result)
  else:
    result = (f'found value {x} at index {a}')
    return(result)

print(binary_search([1,3,5,6,9,10],3))

# Remove Duplicates

# Given a sorted list of integers, dedupe the list 
# Because list elements are already in order, all duplicate values will be grouped together.

# Ok to use a new list
# Bonus: do it in O(n) time (no nested loops, new list ok)
# Bonus: Do it in-place (no new list)
# Bonus: Do it in-place in O(n) time and no new list
# MEGA Bonus: Keep it O(n) time even if it is not sorted

# Input: [1, 1, 1, 1]
# Output: [1]

# Input: [1, 1, 2, 2, 3, 3]
# Output: [1, 2, 3]

# Input: [1, 1, 2, 3, 3, 4]
# Output: [1, 2, 3, 4]

def Remove_dup(list): 
    newlist = [] 
    for i in list: 
        if i not in newlist: 
            newlist.append(i) 
    return newlist 
list = [1, 1, 2, 3, 3, 4]
print(Remove_dup(list)) 



You have 3 bags of marbles. One bag is labelled all red marbles. One bag is labelled all blue marbles. 
# One bag is labelled as a mix between red and blue marbles. All the bags are labelled incorrectly. 
# You may only pick one marble from one bag at a time. 
# How many marbles do you need to pull before you can figure out the correct labels for the bags?



 Using only a 4 minute and 7 minute hourglass or egg timer how would you measure exactly 9 minutes? 



Given a list of integers
# return the first integer from the list that is not repeated anywhere else
# If there are multiple non-repeated integers in the list,
# the "first" one will be the one with the lowest index.

# Input: [3, 5, 5]
# Output: 3

# Input: [3, 3, 5]
# Output: 5

# Input: [3, 5, 4, 3, 4, 6, 5]
# Output: 6

def nonRepeat(arr):
    countDict = {}
    ansList = []
    for i in range(len(arr)):
        if arr[i] not in countDict:
            countDict[arr[i]] = 1
        else:
            countDict[arr[i]] += 1
    for key, value in countDict.items():
        if value == 1:
            ansList.append(key)
    print(ansList) 







# Given an int to represent how much change is needed
# calculate the fewest number of coins needed to create that change,
# using the standard US denominations

# Input: 25
# Output: { quarter: 1 }

# Input: 50
# Output: { quarter: 2 }

# Input: 9
# Output: { nickel: 1, penny: 4 }
def change(num):
    coins = {
        'quarter' : 0,
        'dime' : 0,
        'nickle' : 0,
        'penny' : 0
    }
    while(num > 0):
        if num >= 25:
            num -= 25
            coins['quarter'] += 1
        elif num >= 10 and num < 25:
            num -= 10
            coins['dime'] += 1 
        elif num >= 5 and num < 10:
            num -= 5
            coins['nickle'] += 1
        elif num >= 1 and num < 5:
            num -= 1
            coins['penny'] += 1   
    return coins
stuff = change(123)
print(stuff)
