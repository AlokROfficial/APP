part={
    "Noun": ["teacher", "Mysuru", "computer"],
    "Verb": ["generate", "append", "calculate", "print", "return"],
    "Adjective": ["recent", "edited", "new", "previous", "current"],
     }
print("select a word from the following Dictionary:")
for words in part.values():
    for word in words:
        print(word,end=", ")
word=input("\nEnter a word from the above dictionary: ")
match word:
    case "teacher"|"mysuru"|"computer":
        print("The word is a Noun")
    case "generate"|"append"|"calculate"|"print"|"return":
        print("The word is a Verb")    
    case "recent"|"edited"|"new"|"previous"|"current":
        print("The word is a Adjective")
    case _:
        print("The word is not in the dictionary")