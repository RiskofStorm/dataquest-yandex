from sentiment_classifier import LoadedModel

"""

You can copy-paste those reviews and test it in browser or just RUN model_test.py
It seems that short reviews likely be assigned as negative. I didn't check train data, but it seems every review got
a lot words. 

"""

test = LoadedModel()

hate = test.process("Man, this film stinks. Fuck I hate those actors")
love = test.process("It's such a good picture, Actors plays are astonishing")

positive = test.process("""i was fortunate enough to attend an advance screening for the upcoming thriller conspiracy 
theory .this was , of course , a big deal for me because reviewing movies is basically just a
hobby for me and i never get a chance at something like this . not only did i get to 
see an advance screening , i was able to see an advance screening of a * very good * movie .
the very fast - paced film stars mel gibson as jerry fletcher , a fast - talking , witty , comical 
taxi driver in new york city . gibson \' s performance is terrific , and his character is similar to
 that of martin riggs in the lethal weapon films . gibson again teams up with richard donner , as he
  did in the lethal weapon films and maverick , and this time around , 
the combination works even better . the character of jerry fletcher is indeed unique . 
try to imagine a toned - downed version of travis bickle who , this time around , 
is a jittery guy with knowledge of government conspiracy cover - ups . 
if you can imagine that , then you \' ve basically got jerry fletcher . in many ways , 
i was surprised by this movie . to begin with , i was surprised at how good it was . don \' 
t get me wrong , it \' s not going to be accepting any gold trophies next spring , 
but it was a very enjoyable movie . secondly , i was surprised at mel gibson \' s 
performance . he provided a fantastic""")

negative = test.process("""funny how your expectations can be defeated , and not in good ways . the ghost and the 
darkness promised ( at least , it seemed to me to promise ) a hemingwayesque showdown between men and nature . what it 
delivered was mystery science theater 3000 - level material -- an inadvertently hilarious story that made me scream 
advice at the characters . " get new jobs ! " was one line , if i remember correctly . at the end of the 19th century ,
col . patterson ( val kilmer , whose irish accent comes and goes like an african zephyr ) is an engineer who has been 
hired to build a british railway bridge across the tsavo river in uganda . he is having immensely stereotypical 
problems: the natives are restless , his boss is a jerk , and now two man - eating lions are stalking the work camp and 
killing people off . patterson tries to handle the situation himself , incompetently , and then turns to charles 
remington ( michael douglas ) , a hunter of world reknown ( or something like that ) . the movie stacks the deck so 
heavily in favor of the lions , they should have gotten top billing and co - starred with siegfried and roy . they are 
nigh - invulnerable , as one comic book put it , and this is of course just the excuse the movie needs to have one 
native after another stepping forth to solmenly recite lines about the power of nature """)

print(hate)
print(love)
print(positive)
print(negative)
