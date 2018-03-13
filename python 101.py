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
