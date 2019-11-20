# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.


age = int(input('Enter your age: '))

lon = []

if age % 2 == 1:
    for i in range(1, age+1):
        if i % 2 == 1:
            lon.append(i)
elif age % 2 == 0:
    for i in range (1, age+1):
        if i % 2 == 0:
            lon.append(i)
print(lon)