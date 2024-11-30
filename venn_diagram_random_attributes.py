import random
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the users
users = ['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8']

# Define the attributes
attributes = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']

# Assign random attributes to users
user_attributes = {user: set(random.sample(attributes, k=random.randint(1, len(attributes)))) for user in users}

# Print user attributes
print("User Attributes:")
for user, attrs in user_attributes.items():
    print(f"{user}: {attrs}")

# Create sets for different natures (e.g., A, B, C)
A = {user for user, attrs in user_attributes.items() if 'A1' in attrs}
B = {user for user, attrs in user_attributes.items() if 'A2' in attrs}
C = {user for user, attrs in user_attributes.items() if 'A3' in attrs}

# Print the sets
print("\nSet A (Users with A1):", A)
print("Set B (Users with A2):", B)
print("Set C (Users with A3):", C)

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
venn3([A, B, C], ('Users with A1', 'Users with A2', 'Users with A3'))

# Display the Venn diagram
plt.title("Venn Diagram of Users with Different Attributes")
plt.show()

"""
User Attributes:
User1: {'A1', 'A3', 'A2', 'A4', 'A5', 'A8', 'A6', 'A7'}
User2: {'A6', 'A5', 'A3'}
User3: {'A1', 'A4', 'A8', 'A6', 'A7'}
User4: {'A3'}
User5: {'A1', 'A3', 'A2', 'A7'}
User6: {'A1', 'A8', 'A2', 'A4'}
User7: {'A3', 'A4', 'A2', 'A8', 'A6', 'A7'}
User8: {'A1', 'A2', 'A4', 'A3', 'A8', 'A7'}

Set A (Users with A1): {'User1', 'User3', 'User5', 'User8', 'User6'}
Set B (Users with A2): {'User1', 'User5', 'User7', 'User8', 'User6'}
Set C (Users with A3): {'User2', 'User4', 'User5', 'User7', 'User1', 'User8'}

Intersection of A and B: {'User5', 'User1', 'User6', 'User8'}
Intersection of A and C: {'User5', 'User1', 'User8'}
Intersection of B and C: {'User5', 'User8', 'User1', 'User7'}
Intersection of A, B, and C: {'User5', 'User1', 'User8'}
"""