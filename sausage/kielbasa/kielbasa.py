kielbasa = {
'salt:\t': lambda g: (15/1000) * g,
'black pepper:': lambda g: (2.5/1000) * g,
'garlic:\t': lambda g: (5.5/1000) * g,
'marjoram:': lambda g: (1/1000) * g,
'sugar:\t': lambda g: (2.5/1000) * g,
'eco-cure:': lambda g: (10/1000) * g,
'milk powder:': lambda g: (10/1000) * g,
'liquid:\t': lambda g: (100/1000) * g
}

grams = float(input("Weight of meat in grams: "))

for k,v in kielbasa.items():
  print(f'{k}\t{v(grams)}')
