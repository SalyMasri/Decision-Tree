import monkdata as m  # Contains the MONK datasets
import dtree as d     # Contains the entropy function

e1 = d.entropy(m.monk1)  # Entropy of MONK-1
e2 = d.entropy(m.monk2)  # Entropy of MONK-2
e3 = d.entropy(m.monk3)  # Entropy of MONK-3

print("Entropy of MONK-1: ", e1)
print("Entropy of MONK-2: ", e2)
print("Entropy of MONK-3: ", e3)