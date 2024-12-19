def interchange_three_integers(a, b, c):

  temp_a = a
  temp_b = b
  temp_c = c

  a = temp_c
  b = temp_a
  c = temp_b

  return a, b, c


a = 1
b = 2
c = 3

a, b, c = interchange_three_integers(a, b, c)

print(f"After interchanging: a = {a}, b = {b}, c = {c}")