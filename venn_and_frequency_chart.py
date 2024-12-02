import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3, venn2_circles, venn3_circles

# Number of people in each domain
domain_sizes = [15, 20, 10, 8, 12, 18, 14]

# Define the overlaps between domains for Venn diagram of three domains
venn_labels = {
    '100': 15,  # Only in A
    '010': 20,  # Only in B
    '110': 5,   # In A and B
    '001': 10,  # Only in C
    '101': 2,   # In A and C
    '011': 3,   # In B and C
    '111': 1    # In A, B, and C
}

# Create Venn diagram for three domains (A, B, C)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
venn3(subsets=venn_labels, set_labels=('A', 'B', 'C'))
plt.title('Venn Diagram for Domains A, B, and C')

# Create Frequency Chart
plt.subplot(1, 2, 2)
domains = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
plt.bar(domains, domain_sizes, color='skyblue')
plt.xlabel('Domains')
plt.ylabel('Number of People')
plt.title('Frequency Chart - Assignment of 50 People to 7 Domains')

plt.tight_layout()
plt.show()

