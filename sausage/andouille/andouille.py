pork_ratio_weight=4535.92

ingredient_weights = {
  "salt": 90,
  "fresh_garlic": 50,
  "cayenne": 30,
  "black_pepper": 30,
  "fresh_thyme": 10,
  "powdered_milk": 120,
  "dry_white_wine": 400
}
# EcoCure wants you to include the weight of the spices
ingredient_weights["eco_cure"] = (sum(ingredient_weights.values())+pork_ratio_weight)*0.01

ratios = dict()
for k, v in ingredient_weights.items():
  ratios[k] = v/pork_ratio_weight

pork_weight=3402.4
for k, v in ratios.items():
  print(f"{k}: {pork_weight*v}")
