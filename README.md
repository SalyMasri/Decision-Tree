#  Decision Trees & Information Gain

## 📌 Project Overview
This project explores **decision tree learning** using the **MONK datasets**, analyzing **entropy, information gain, tree depth effects, and pruning**. The study evaluates **overfitting risks**, **bias-variance trade-offs**, and **cross-validation performance** to optimize generalization.

## 🛠️ Technologies & Tools Used
- **Programming Language**: Python
- **Libraries**: NumPy, Matplotlib
- **Algorithms**: ID3 Decision Trees, Entropy Calculation, Information Gain
- **Evaluation Metrics**: Train/Test Error, Cross-Validation, Pruning Analysis

## 🔍 Key Features
### **📊 Entropy & Information Gain Analysis**
- Calculated entropy values for each MONK dataset.
- Measured information gain to determine **optimal splitting attributes**.
- Analyzed how **entropy reduction affects tree depth and performance**.

### **🌳 Building & Evaluating Decision Trees**
- **Built full decision trees** for all MONK datasets.
- **Evaluated train & test errors** to detect overfitting.
- Tested the **effect of tree depth, min samples split, and min info gain**.

### **✂️ Pruning & Cross-Validation**
- **Pruned trees** to optimize bias-variance tradeoff.
- Used **cross-validation (5-fold, 10-fold)** to enhance generalization.
- Plotted **classification error vs. dataset split fraction** to analyze impact.

## 📊 Results
✔️ **Overfitting occurs with deep trees**, leading to **high variance**.  
✔️ **Pruning improves test accuracy**, particularly for MONK-3.  
✔️ **Optimal cross-validation (10-fold) stabilizes results**, reducing variance.  
✔️ **Setting min info gain too high leads to underfitting**, increasing bias.  

## 🔄 Future Improvements
- Implement **Random Forests** for ensemble-based decision-making.
- Explore **Gini Impurity** as an alternative to entropy for splits.
- Experiment with **hyperparameter tuning** for better model optimization.

---
