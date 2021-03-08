from math import factorial

silnia = factorial(1000)

lz = list(str(silnia))

for i in range(len(lz)):
    if i < len(lz)-1:
        lz[i] = lz[i] + lz[i+1]

print("00 - występuje",lz.count('00'),"razy")
print("01 - występuje",lz.count('01'),"razy")
print("02 - występuje",lz.count('02'),"razy")
print("03 - występuje",lz.count('03'),"razy")
print("04 - występuje",lz.count('04'),"razy")
print("05 - występuje",lz.count('05'),"razy")
print("06 - występuje",lz.count('06'),"razy")
print("07 - występuje",lz.count('07'),"razy")
print("08 - występuje",lz.count('08'),"razy")
print("09 - występuje",lz.count('09'),"razy")

for x in range(10, 100):
    print(x, "- występuje", lz.count(str(x)), "razy")