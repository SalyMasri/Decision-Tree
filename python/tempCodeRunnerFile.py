# Build trees for all datasets
tree_monk1 = d.buildTree(m.monk1, m.attributes, maxdepth=1000, min_samples_split=00, min_info_gain=0.5)
tree_monk2 = d.buildTree(m.monk2, m.attributes, maxdepth=1000, min_samples_split=00, min_info_gain=0.5)
tree_monk3 = d.buildTree(m.monk3, m.attributes, maxdepth=1000, min_samples_split=0, min_info_gain=0.5)