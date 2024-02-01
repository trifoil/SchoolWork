import math
l = int(input("longueur"))
periode = (math.pi*2) * math.sqrt(l/9.81)
print("%.3f secondes" % periode)