hello = "Hello"
world = 'World'

hello_world = (hello + " " + world)
print(hello_world)      # Note: you should print "Hello World"
#hello world string !
#string indexing
python = "Python"
print("h " + python[3])     # Note: string indexing starts with 0

p_letter = python[0]
print("P " + p_letter[0])

#********slicing strings using #:# *********
monty_python = "Monty Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:]
print(python)

#f you want to check whether a string contains a specific letter or a substring, you can use the in keyword. 

ice_cream = "ice cream"
print("cream" in ice_cream)    # print boolean result directly

contains = "ice" in ice_cream
print(contains)

y = "u cre" in ice_cream
print(y)
#add The len() function is used to count how many characters a string contains. 

Get the first half of the string stored in the variable phrase. 
# understaing \ and breaking the "" or ''
dont_worry = "Don't worry about apostrophes"
print(dont_worry)
print("\"Sweet\" is an ice-cream")
print('The name of the ice-cream is "Sweet\'n\'Tasty"')

q = len(dont_worry)
print(q)

#The % operator after a string is used to combine a string with variables. The % operator will replace %s in a string
#with the string variable that comes after it. The %d special symbol is used as a placeholder for numeric or decimal values. 

name = "John"
print("Hello, PyCharm! My name is %s!" % name)     # Note: %s is inside the string, % is after the string

print("I'm %d years old" % 28)
