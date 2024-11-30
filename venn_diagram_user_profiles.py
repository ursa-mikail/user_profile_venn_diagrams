import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sets
A = {'User1', 'User2', 'User3', 'User4'}
B = {'User2', 'User3', 'User5', 'User6'}
C = {'User3', 'User4', 'User6', 'User7'}

# Print the sets
print("Set A (Training Completed):", A)
print("Set B (Background Check Passed):", B)
print("Set C (Application Fee Paid):", C)

# Find intersections
A_and_B = A.intersection(B)
A_and_C = A.intersection(C)
B_and_C = B.intersection(C)
A_and_B_and_C = A.intersection(B).intersection(C)

# Print intersections
print("\nIntersection of A and B:", A_and_B)
print("Intersection of A and C:", A_and_C)
print("Intersection of B and C:", B_and_C)
print("Intersection of A, B, and C:", A_and_B_and_C)

# Create Venn diagram
venn3([A, B, C], ('Training Completed', 'Background Check Passed', 'Application Fee Paid'))

# Display the Venn diagram
plt.title("Venn Diagram of User Profiles")
plt.show()

"""
Set A (Training Completed): {'User4', 'User2', 'User1', 'User3'}
Set B (Background Check Passed): {'User5', 'User2', 'User6', 'User3'}
Set C (Application Fee Paid): {'User4', 'User7', 'User6', 'User3'}

Intersection of A and B: {'User2', 'User3'}
Intersection of A and C: {'User4', 'User3'}
Intersection of B and C: {'User6', 'User3'}
Intersection of A, B, and C: {'User3'}
"""