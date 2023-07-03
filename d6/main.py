x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


grade = 92

# First way to do this
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")

# Second way to do this
if 100 >= x >= 90:
    print("A")
elif 90 > x >= 80:
    print("B")
elif 80 > x >= 70:
    print("C")
elif 70 > x >= 60:
    print("D")
else:
    print("F")

# Third way to do this
if 100 >= x and x >= 90:
    print("A")
elif 90 > x and x >= 80:
    print("B")
elif 80 > x and x >= 70:
    print("C")
elif 70 > x and x >= 60:
    print("D")
else:
    print("F")

