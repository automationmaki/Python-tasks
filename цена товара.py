rubles = float(input())
kopeks = round(rubles * 100)
print(*divmod(kopeks, 100))
