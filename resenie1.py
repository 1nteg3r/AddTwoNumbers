#prvo resnie koristejki tehnika string slicing [::-1]
l1 = [2,4,3]
l2 = [5,6,4]

val1 = int("".join([str(i) for i in l1]))
val2 =int("".join([str(i) for i in l2]))

num = val1+val2

print(f"List1 = {val1}")
print(f"List2 = {val2}")
print("Sobirokot na dvata broja dobieni od listata treba da bide vo obraten redosled")
print("Output: " + str(num)[::-1])
