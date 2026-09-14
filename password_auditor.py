import math
import sys


def check_password(password):
  length = len(password)
  has_upper = any(c.isupper() for c in password)
  has_lower = any(c.islower() for c in password)
  has_digit = any(c.isdigit() for c in password)
  has_special = any(not c.isalnum() for c in password)

  pool = 0
  if has_lower:
    pool += 26
  if has_upper:
    pool += 26
  if has_digit:
    pool += 10
  if has_special:
    pool += 32

  entropy = length * math.log2(pool) if pool > 0 else 0
  print(f"Password Length: {length}")
  print(f"Character Pool Size: {pool}")
  print(f"Estimated Entropy: {entropy:.2f} bits")
  if entropy < 40:
    print("Strength: Weak")
  elif entropy < 70:
    print("Strength: Moderate")
  else:
    print("Strength: Strong")


if __name__ == "__main__":
  pwd = input("Enter password to audit: ")
  check_password(pwd)