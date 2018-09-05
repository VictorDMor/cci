# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(word):
    unique = True
    for i in range(len(word)-1):
        if sorted(word)[i] == sorted(word)[i+1]:
            unique = False
            break
    return unique

print(is_unique("root"))
print(is_unique("algorithm"))