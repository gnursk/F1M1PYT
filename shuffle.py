import random

word1 = input ("Welk woor zou je willen husselen: ")
word2 = input ("Welk woor zou je willen husselen: ")
word3 = input ("Welk woor zou je willen husselen: ")

randomised1 = ''.join(random.sample(word1, len (word1)))
print (randomised1)
randomised2 = ''.join(random.sample(word1, len (word1)))
print (randomised2)
randomised3 = ''.join(random.sample(word1, len (word1)))
print (randomised3)