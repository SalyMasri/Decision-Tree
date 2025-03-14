import monkdata as m
import dtree as d
import drawtree_qt5 as dt




# Build trees for all datasets
tree_monk1 = d.buildTree(m.monk1, m.attributes, maxdepth=1000, min_samples_split=00, min_info_gain=0.5)
tree_monk2 = d.buildTree(m.monk2, m.attributes, maxdepth=1000, min_samples_split=00, min_info_gain=0.5)
tree_monk3 = d.buildTree(m.monk3, m.attributes, maxdepth=1000, min_samples_split=0, min_info_gain=0.5)

def compute_errors(tree, train_data, test_data):
    train_error = 1 - d.check(tree, train_data)
    test_error = 1 - d.check(tree, test_data)
    return round(train_error, 4), round(test_error, 4)  # Round to 4 decimal places

# Compute errors
e1_train, e1_test = compute_errors(tree_monk1, m.monk1, m.monk1test)
e2_train, e2_test = compute_errors(tree_monk2, m.monk2, m.monk2test)
e3_train, e3_test = compute_errors(tree_monk3, m.monk3, m.monk3test)

# Get dataset sizes
train_sizes = [len(m.monk1), len(m.monk2), len(m.monk3)]
test_sizes = [len(m.monk1test), len(m.monk2test), len(m.monk3test)]

# Print results in table format with dataset sizes
print("\nDecision Tree Performance:")
print("Dataset   | Train Size | Test Size | E_train  |  E_test  |")
print("------------------------------------------------------------")
print(f"MONK-1    |    {train_sizes[0]:<8} |  {test_sizes[0]:<8} |   {e1_train}   |   {e1_test}  |")
print(f"MONK-2    |    {train_sizes[1]:<8} |  {test_sizes[1]:<8} |   {e2_train}   |   {e2_test}  |")
print(f"MONK-3    |    {train_sizes[2]:<8} |  {test_sizes[2]:<8} |   {e3_train}   |   {e3_test}  |")




#monk2_tree = d.buildTree(m.monk2, m.attributes)

# Show and Save the Tree Image
#dt.drawTree(monk2_tree, save_image=True, filename="monk2_tree.png")

