#vtoro resenie koristejki while loop
l1 = [2,4,3]
l2 = [5,6,4]

val1 = int("".join([str(i) for i in l1]))
val2 =int("".join([str(i) for i in l2]))

num = val1+val2

reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"List1 = {val1}")
print(f"List2 = {val2}")
print("Sobirokot na dvata broja dobieni od listata treba da bide vo obraten redosled")
print(f"Output : {reversed_num}")
