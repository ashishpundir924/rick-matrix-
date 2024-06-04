import matplotlib.pyplot as plt
import numpy as np

# Function to create a risk matrix
def create_risk_matrix(ax, title, data, row_labels, col_labels):
    c = ax.pcolor(data, edgecolors='k', linestyle='dashed', linewidths=2, cmap='Blues', vmin=0, vmax=16)
    ax.set_aspect('equal')

    # Set ticks in the middle of the cells
    ax.set_yticks(np.arange(len(row_labels)) + 0.5, minor=False)
    ax.set_xticks(np.arange(len(col_labels)) + 0.5, minor=False)
    
    ax.set_yticklabels(row_labels, minor=False)
    ax.set_xticklabels(col_labels, minor=False)

    # Rotate the tick labels for the x-axis
    plt.xticks(rotation=90)
    
    # Annotating the cells with risk labels
    for i in range(len(row_labels)):
        for j in range(len(col_labels)):
            text = ax.text(j + 0.5, i + 0.5, f'R{int(data[i, j])}',
                           ha='center', va='center', color='black')

    ax.set_title(title)
    plt.colorbar(c, ax=ax)  # Show color scale

# Define data for the matrices
data1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

data2 = np.array([
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
])

labels_probability = ['Very Low', 'Low', 'Medium', 'High']
labels_impact = ['Very Low', 'Low', 'Medium', 'High']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

create_risk_matrix(ax1, 'Risk Matrix-1', data1, labels_impact, labels_probability)
create_risk_matrix(ax2, 'Risk Matrix-2', data2, labels_impact, labels_probability)

plt.tight_layout()
plt.show()
