price=float(input("сколько стоит товар ?\n"))
if price>5000:
    print("скидка 10%")
    total=price-price*0.1
else:
    print("нет скидки")
    total=price
print(f"итого {total} рублей")
