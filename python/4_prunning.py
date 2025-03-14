import random
import statistics
import numpy as np
import matplotlib

from tabulate import tabulate
import matplotlib.pyplot as plt

import dtree as dtree
import monkdata as m

matplotlib.use('Agg')  # Use a non-interactive backend

def get_best_tree(currtree):
    found_better_tree = False

    for newtree in dtree.allPruned(currtree):
        if dtree.check(newtree, monkval) > dtree.check(currtree, monkval):
            found_better_tree = True
            currtree = newtree

    if found_better_tree:
        currtree = get_best_tree(currtree)
    return currtree


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


if __name__ == '__main__':
    dataset_names = ('MONK-1', 'MONK-3')
    datasets = (m.monk1, m.monk3)
    datasets_test = (m.monk1test, m.monk3test)

    fractions = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999)
    decimals = 3
    n = 10

    header = ['Dataset', 'Fraction', 'Mean error (n = {})'.format(n), 'Standard deviation']

    # New style settings
    plt.style.use('dark_background')  # Switch to a dark background
    plt.figure(figsize=(10, 6))  # Bigger figure for better visibility

    # Define unique colors, markers, and line styles
    colors = ['#ff5733', '#33ff57']  # Neon Orange & Neon Green
    markers = ['D', '^']  # Diamond & Triangle markers
    linestyles = ['dashed', 'dotted']  # Different line styles

    for idx, (dataset_name, dataset, dataset_test) in enumerate(zip(dataset_names, datasets, datasets_test)):
        data = []
        mean_errors = []
        stdev = []

        for fraction in fractions:
            errors = []
            for i in range(n):
                monktrain, monkval = partition(dataset, fraction)
                built_tree = dtree.buildTree(monktrain, m.attributes)
                best_tree = get_best_tree(built_tree)
                errors.append(1 - dtree.check(best_tree, dataset_test))
            
            mean_error = round(statistics.mean(errors), decimals)
            mean_errors.append(mean_error)
            stdev.append(round(statistics.stdev(errors), decimals))
            data.append([dataset_name, fraction, mean_error, statistics.mean(stdev)])

        print(tabulate(data, header), '\n')

        # Modernized plotting with a fresh style
        plt.errorbar(
            fractions, mean_errors, yerr=stdev,
            marker=markers[idx], linestyle=linestyles[idx], linewidth=2.5,
            markersize=10, capsize=6, color=colors[idx], label=dataset_name
        )

    # Improve aesthetics
    plt.grid(True, linestyle=':', linewidth=0.8, alpha=0.7)  # Grid with dotted lines
    plt.title(f'MONK Dataset Performance (n = {n})', fontsize=16, fontweight='bold', color='white')
    plt.xlabel('Fraction of Training Data', fontsize=14, color='white')
    plt.ylabel('Mean Error Rate', fontsize=14, color='white')
    plt.xticks(fontsize=12, color='white')
    plt.yticks(fontsize=12, color='white')
    plt.legend(loc='upper right', fontsize=12, frameon=True, edgecolor='white')

    # Save the improved plot
    plt.savefig('monk_error_bars_new_repetetions10.png', dpi=400, bbox_inches='tight')
    print("Plot saved as monk_error_bars_new_repetetions10.png")
