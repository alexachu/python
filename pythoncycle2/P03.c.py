#List of vowels selected from a given word
word=['apple']
l=[w[0] for w in word if w[0] in 'aeiou']
e=[w[4] for w in word if w[4] in 'aeiou']
print(l)
print(e)
