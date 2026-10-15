languages = ["Python", "Java", "C++", "JavaScript"] 
 
print("Original List:", languages) 

languages.insert(1, "C") 
print("After insert():", languages)

print("Length of list:", len(languages))

languages.pop()
print("After pop():", languages)

# languages.clear() 
# print("After clear():", languages) 

del languages[1]
print("After delete (del):", languages)