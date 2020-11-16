tekstPodstawowy = "mam 20 lat i nie wiem co dalej"
check = "mam" in tekstPodstawowy
check2 = "mam" not in tekstPodstawowy
print(len(tekstPodstawowy))
print(tekstPodstawowy.strip())
print(tekstPodstawowy.lower())
print(tekstPodstawowy.upper())
print(tekstPodstawowy.replace("m", "x"))
print(check)
print(check2)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

viking = "We are the so-called \"Vikings\" from the north."
print(viking)


#escape characters used in Python
''' 
Code 	Result 	Try it
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
'''
#metody do stringa

'''
Method 	            Description
capitalize()	    Converts the first character to upper case
casefold()      	Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()  	Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle() 	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
'''