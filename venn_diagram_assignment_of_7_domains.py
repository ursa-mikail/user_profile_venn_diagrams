import matplotlib.pyplot as plt
from matplotlib_venn import venn3

import numpy as np
from matplotlib_venn import venn3

def venn_diagram(a, b, c, labels=['Infra', 'System', 'Platform']):
    a = set(a)
    b = set(b)
    c = set(c)

    only_a = len(a - b - c)
    only_b = len(b - a - c)
    only_c = len(c - a - b)

    only_a_b = len(a & b - c)
    only_a_c = len(a & c - b)
    only_b_c = len(b & c - a)

    a_b_c = len(a & b & c)

    venn3(subsets=(only_a, only_b, only_a_b, only_c, only_a_c, only_b_c, a_b_c), set_labels=labels)

a, b, c = np.round(np.random.rand(3, 50000), 5)
venn_diagram(a, b, c)

plt.title('Venn Diagram - Assignment of 7 Domains')
plt.show()

# Ref: https://stackoverflow.com/questions/10804432/proportional-venn-diagram-for-more-than-3-sets

