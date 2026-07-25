print("--- Set Creation and Basic Operations ---")

# Creating a set from a list (duplicates are removed)
my_list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(my_list_with_duplicates)

print(f"Original list: {my_list_with_duplicates}")
print(f"Set from list (duplicates removed): {unique_numbers}")

# Creating a set directly
vowels = {"a", "e", "i", "o", "u"}
print(f"Vowels set: {vowels}")

# Important: To create an empty set, use set()
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")

# Note: {} creates an empty dictionary, not an empty set

print("\n--- Adding and Removing Elements from a Set ---")

vowels.add("y")  # Add an element
print(f"After adding 'y': {vowels}")

vowels.add("a")  # Adding an existing element has no effect
print(f"After adding 'a' again: {vowels}")

vowels.remove("y")  # Remove an existing element
print(f"After removing 'y': {vowels}")

try:
    vowels.remove("z")  # Removing a non-existent element with remove() causes an error
except KeyError as e:
    print(f"Error trying to remove 'z' with remove(): {e}")

vowels.discard("z")  # discard() does not raise an error if element not found
print(f"After trying to discard 'z': {vowels}")

# Pop an arbitrary element (sets are unordered)
popped_item = vowels.pop()
print(f"Popped item: {popped_item}")
print(f"Set after pop: {vowels}")

# vowels.clear()  # Empties the set
# print(f"After clear: {vowels}")

print("\n--- Set Mathematical Operations ---")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: all unique elements from both sets
print(f"Union (A | B): {set_a.union(set_b)}")
print(f"Union (A | B) operator: {set_a | set_b}")

# Intersection: common elements in both sets
print(f"Intersection (A & B): {set_a.intersection(set_b)}")
print(f"Intersection (A & B) operator: {set_a & set_b}")

# Difference: elements in A but not in B
print(f"Difference (A - B): {set_a.difference(set_b)}")
print(f"Difference (A - B) operator: {set_a - set_b}")

# Symmetric Difference: elements in either set, but not in both
print(f"Symmetric Difference (A ^ B): {set_a.symmetric_difference(set_b)}")
print(f"Symmetric Difference (A ^ B) operator: {set_a ^ set_b}")

print("\n--- Membership Testing and Subset/Superset ---")

my_skills = {"Python", "SQL", "Git", "Cloud"}
required_skills = {"Python", "SQL"}
extra_skills = {"Linux", "Python", "SQL", "Cloud", "API"}

print(f"'SQL' in my_skills: {'SQL' in my_skills}")  # True
print(f"'Java' in my_skills: {'Java' in my_skills}")  # False

print(
    f"Is required_skills a subset of my_skills? "
    f"{required_skills.issubset(my_skills)}"
)  # True

print(
    f"Is my_skills a superset of required_skills? "
    f"{my_skills.issuperset(required_skills)}"
)  # True

print(
    f"Are my_skills and extra_skills disjoint? "
    f"{my_skills.isdisjoint(extra_skills)}"
)  # False (they share elements)