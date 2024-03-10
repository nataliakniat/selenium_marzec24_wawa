import sys

evenNumbers = [element
                for element in range(10001)
                if element % 2 == 0]

print(evenNumbers)

evenNumbersGenerator = (element
                for element in range(10001)
                if element % 2 == 0)

print(evenNumbersGenerator)

for item in evenNumbersGenerator:
    print(item)

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))