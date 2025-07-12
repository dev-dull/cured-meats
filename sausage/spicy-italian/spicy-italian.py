pork_ratio_weight=2722

ingredient_weights = {
  "milk_powder": 50,
  "salt": 45,
  "italian_herb_mix": 20,
  "white_sugar": 35,
  "fennel": 20,
  "granulated_garlic": 20,
  "paprika": 20,
  "red_pepper_flakes": 16,
  "black_pepper": 10,
  "tumeric": 5,
  "parsley": 5,
  "coriander": 10,
  "liquid": 250,
}

# EcoCure wants you to include the weight of the spices
ingredient_weights["eco_cure"] = (sum(ingredient_weights.values())+pork_ratio_weight)*0.01

ratios = dict()
for k, v in ingredient_weights.items():
  ratios[k] = v/pork_ratio_weight

pork_weight=3402.4
for k, v in ratios.items():
  print(f"{k:<20} {pork_weight * v:>10.2f}")
