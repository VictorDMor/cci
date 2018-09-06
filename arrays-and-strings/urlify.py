# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can 
# perform this operation in place.)

def urlify(url):
    new_url = []
    for character in url:
        if character == ' ':
            new_url.append('%20')
            continue
        new_url.append(character)
    for i in range(len(new_url)-1, -1, -1):
        if new_url[i] == '%20': new_url.pop(i)
        else: break
    return ''.join(new_url)

print(urlify("churros e salgadinhos"))
