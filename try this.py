number = float(input("Enter a positive number containing a decimal: "))
right = str(number)[::-1].find('.')
print("%d digits to the right of decimal." %right)
left = str(number)[::1].find('.')
print("%d digits to the left of decimal." %left)