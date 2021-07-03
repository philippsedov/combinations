from itertools import combinations


syllables = ['A', 'B', 'C', 'D']

for variant in combinations(syllables, 2):
 print(variant)
 print(variant[::-1])

# output:
# ('A', 'B')
# ('B', 'A')
# ('A', 'C')
# ('C', 'A')
# ('A', 'D')
# ('D', 'A')
# ('B', 'C')
# ('C', 'B')
# ('B', 'D')
# ('D', 'B')
# ('C', 'D')
# ('D', 'C')
