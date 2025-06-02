cure_ratio=0.03
salmon_weight=1154.393

salmon_cure = {
  'salt': 900,
  'sugar': 400,
  'garlic': 30,
  'pepper': 30,
  'sage': 10,
  'redPeppperFlake': 10
}
salmon_cure_sum = sum(salmon_cure.values())

cure_amount=(salmon_weight*cure_ratio)
final_ratio = cure_amount / salmon_cure_sum

for k, v in salmon_cure.items():
  print(f'{k}:\t{v*final_ratio}')
