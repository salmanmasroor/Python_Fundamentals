"""
Definition: A string is an immutable sequence of characters in Python.
"""

# Creating Strings
name = "Ali"
city = "Lahore"
Address = """XYZ,
Lahore"""
print(name,city,Address)

#Access Characters — Indexing
print(name[0])
print(city[-1])

#Slicing
print(city[0:4])
print(Address[-3:])
print(Address[-5:-1])

#Strings Are Immutable
language = "Urdu"
#language[0] = "A" # we can not change 
#print(language)

#Instead, create a new string:
new_string = "A"+language[1:]
print(new_string)

#Loop Through a String
for char in language:
    print(char)

#Check Character
print("A" in new_string)
print("a" in new_string) #case_sensitive

#Check length
print(len(language))

# string methods

#lower() and upper()  
country = "paKistan"
country_one = country.lower() #STRING ARE IMMUTABLE THATS WHY WE ASSIGN VARIABLE
print(country_one)
countryTwo = country.upper()
print(countryTwo)  

#strip  
a = "  python  "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#join 
words1 = ["Python", "is", "easy"]
words = " ".join(words1)
print(words)
word_one = "-".join(words1)
print(word_one)
#replace
sentence = "I like apple"
sentence = sentence.replace("apple","pineapple")
print(sentence)

#count
sentence = "I like pineapple"
print(sentence.count("i"))
print(sentence.count("I"))
print(sentence.count("p"))


#split
text = "apple,banana,mango"
text = text.split(",")
print(text)
text1 = "he going to school"
print(text1.split())

#find
print(text1.find("a")) # -1 if not found
print(text1.find("o")) # it give number according to how many character exit in a string.

#startswith()
print(text1.startswith("h"))
print(text1.endswith("ol"))
print(text1.startswith("p")) # false beacuse it take full string not one word 
#print(text1.startswith("h").endswith("l")) it not work give error
print(text1.startswith("h") and text1.endswith("l")) # return True

