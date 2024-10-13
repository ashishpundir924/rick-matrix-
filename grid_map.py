import matplotlib.pyplot as plt
import itertools

# Parameters
m, n = 3, 1  # Grid size

# Generate all possible paths (combinations of 'R' and 'U' moves)
moves = ['R'] * m + ['U'] * n
all_paths = set(itertools.permutations(moves))

# Function to convert a path of moves into coordinates
def path_to_coords(path):
    x, y = 0, 0
    coords = [(x, y)]
    for move in path:
        if move == 'R':
            x += 1
        else:
            y += 1
        coords.append((x, y))
    return coords

# Create figure
fig, axes = plt.subplots(1, len(all_paths), figsize=(15, 5), sharey=True)

# Plot each path on a separate subplot
for ax, path in zip(axes, all_paths):
    coords = path_to_coords(path)
    x_vals, y_vals = zip(*coords)
    
    ax.plot(x_vals, y_vals, marker='o', color='red')
    ax.set_title(f"Path: {''.join(path)}")
    ax.set_xlim(0, m)
    ax.set_ylim(0, n)
    ax.grid(True)
    ax.set_xticks(range(m+1))
    ax.set_yticks(range(n+1))

# Show all the plots
plt.tight_layout()
plt.show()
