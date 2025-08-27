n =int(input("Enter your number: "))
total = 0
for i in range(1, n+1):
    if i % 2 != 0:
        total += i
print(f"odd nnumbers from 1 to {n} is: {total}")