# bounce.py
#
# Exercise 1.5

height = 100 # altura en metros
bounce = 0 # número de rebotes 

for i in range (10):
    height = (height * 0.6) # Pregunta de lógica... si se supone que va decreciendo, por que debo multiplicar 0.6?
    bounce = bounce + 1
    print(bounce, round(height, 4))



