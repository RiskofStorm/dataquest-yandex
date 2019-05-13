from sentiment_classifier import LoadedModel

"""

You can copy-paste those reviews and test it in browser or just RUN model_test.py
It seems that short reviews likely be assigned as negative. I didn't check train data, but it seems every review got
a lot words. 

"""

test = LoadedModel()


hate = test.process("Man, this film stinks. Fuck I hate those actors")
love = test.process("It's such a good picture, Actors plays are astonishing")

positive = test.process(""" """)

negative = test.process(""" """)

print(hate)
print(love)
print(positive)
print(negative)
