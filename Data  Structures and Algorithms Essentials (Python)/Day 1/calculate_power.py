try:
  x, y = tuple(map(int, input().split()))
except ValueError:
  print("Please enter valud numbers")
else:
  print(x**y)
