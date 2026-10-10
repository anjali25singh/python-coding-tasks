# tuple_immutability
t = (1, 2, 3)
try:
    t[1] = 99
except TypeError as e:
    print("Error:", e)