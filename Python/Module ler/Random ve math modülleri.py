import random
import math

# RANDOM MODULE PART
#help(random>>>>>>> modüller hakkında bilgi almak için kullanabilrsin bu kodu)
liste=[*range(6)]
print(random.random())
print(random.randint(0,10)) 
random.shuffle(liste)
print(liste)
print(random.choice(liste))
print(random.sample(liste,k=4))

#MATH MODULE
print(math.ceil(7.4))
print(math.floor(7.4))
print(math.factorial(5))
print(int(math.pow(3,5)))