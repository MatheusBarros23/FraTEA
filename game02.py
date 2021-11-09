import random

subjects = ['CARLOS', 'MATHEUS', 'ANA']
verbs = ['COMEU', 'GOSTA DE', 'COMPROU']
object = ['MAÇÃ', 'PIZZA', 'FEIJÃO']

answer = (f'{random.choice(subjects)} {random.choice(verbs)} {random.choice(object)}')

print(answer)
