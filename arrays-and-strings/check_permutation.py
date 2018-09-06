# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(a, b):
    is_permutation = False
    if sorted(a) == sorted(b): is_permutation = True
    return is_permutation

print(check_permutation('bus', 'sub'))
print(check_permutation('python', 'algorithm'))