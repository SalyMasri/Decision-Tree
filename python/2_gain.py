import monkdata as m
import dtree as d

# Training datasets
monk1_train = m.monk1
monk2_train = m.monk2
monk3_train = m.monk3

# Attributes (a1 to a6)
attributes = [m.attributes[0], m.attributes[1], m.attributes[2], 
              m.attributes[3], m.attributes[4], m.attributes[5]]

def compute_gains(dataset):
    gains = []
    for attr in attributes:
        gain = d.averageGain(dataset, attr)
        gains.append(round(gain, 4))  # Round to 4 decimal places
    return gains

# Compute gains for all datasets
gains_monk1 = compute_gains(monk1_train)
gains_monk2 = compute_gains(monk2_train)
gains_monk3 = compute_gains(monk3_train)

# Print the results in table format
print("\nInformation Gain Table:")
print("Dataset   |   a1    |   a2    |   a3    |   a4    |   a5    |   a6    |")
print("------------------------------------------------------------------------")
print(f"MONK-1    |  {gains_monk1[0]}  |  {gains_monk1[1]}  |  {gains_monk1[2]}  |  {gains_monk1[3]}  |  {gains_monk1[4]}  |  {gains_monk1[5]}  |")
print(f"MONK-2    |  {gains_monk2[0]}  |  {gains_monk2[1]}  |  {gains_monk2[2]}  |  {gains_monk2[3]}  |  {gains_monk2[4]}  |  {gains_monk2[5]}  |")
print(f"MONK-3    |  {gains_monk3[0]}  |  {gains_monk3[1]}  |  {gains_monk3[2]}  |  {gains_monk3[3]}  |  {gains_monk3[4]}  |  {gains_monk3[5]}  |")