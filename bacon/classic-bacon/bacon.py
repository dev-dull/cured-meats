ingredient_percents = {
  "salt": 0.0225,
  "sugar": 0.0125,
  "garlic powder": 0.005,
  "pepper": 0.005,
  "sage": 0.0025,
  "red pepper flakes": 0.0025,
}

weight_for_cure_calc = 0
pork_weight=2027.558
for k, v in ingredient_percents.items():
  weight_for_cure_calc += pork_weight * v
  print(f"{k:<20} {pork_weight * v:>10.2f}g")

# EcoCure wants you to include the weight of the spices
print(f"{k:<20} {(pork_weight + weight_for_cure_calc) * v:>10.2f}g")
