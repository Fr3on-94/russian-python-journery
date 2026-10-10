weather=int(input("какая температура ?\n"))
if weather >25:
    print("жарко")
elif weather > 10:
    print("тепло")
elif weather > 0:
    print("прохладно")
else:
    print("холодно")