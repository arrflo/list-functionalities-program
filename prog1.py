mylist_ = ['9','5','7','8','3','27','16','11','13','24']
print (f"This is the original list: ", mylist_)
print (f"Menu \n 1 - add an element \n 2 - insert an element \n 3 - modify an element")
print (f" 4 - delete an element \n 5 - arrange in ascending order \n 6 - arrange in descending order")
user_in = int(input ("What do you want to do? (choose from 1 to 6) "))

# functions
def option_1():
    user_in1 = input ("What element do you wish to add? ")
    mylist_.append (user_in1)
    print (f"The element has been added.")
    print (f"This is the new array: ", mylist_)

def option_2():
    user_in1 = input ("What element do you wish to insert? ")
    user_in2 = int(input ("At what placement? (choose from 1 to 10) ")) - 1
    mylist_.insert(user_in2,user_in1)
    print (f"The element has been inserted.")
    print (f"This is the new array: ", mylist_)

def option_3 ():
    user_in1 = int(input ("Which element do you wish to modify? (elements are ordered; choose from 1 to 10) ")) - 1
    user_in2 = input ("What would you like it to be changed into? ")
    mylist_ [user_in1] = user_in2
    print (f"The element has been modified.")
    print (f"This is the new array: ", mylist_)

def option_4 ():
    user_in1 = input ("Which element do you wish to delete? ")
    mylist_.remove (user_in1)
    print (f"The element has been deleted.")
    print (f"This is the new array: ", mylist_)

def option_5():
    mylist_1 = [9,5,7,8,3,27,16,11,13,24]
    mylist_1.sort()
    print (f"The elements are now arranged in ascending order.")
    print (f"This is the new array: ", mylist_1)

def option_6():
    mylist_1 = [9,5,7,8,3,27,16,11,13,24]
    mylist_1.sort()
    mylist_1.reverse ()
    print (f"The elements are now arranged in descending order.")
    print (f"This is the new array: ", mylist_1)

if user_in == 1:
    option_1 ()
elif user_in == 2:
    option_2 ()
elif user_in == 3:
    option_3 ()
elif user_in == 4:
    option_4 ()
elif user_in == 5:
    option_5 ()
else:
    option_6
    