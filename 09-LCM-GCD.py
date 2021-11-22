
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

if a <= b:
  for n in range(2, a+1):
    if (a % n == 0) and (b % n == 0):
      gcd = n

elif a > b:
  for n in range(2, b+1):
    if (a % n == 0) and (b % n == 0):
      gcd = n

lcm = (a * b) // gcd

print("LCM =", lcm)
print("GCD =", gcd)