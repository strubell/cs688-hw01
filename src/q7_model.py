'''
CS688 HW01: My Bayes net

Data format:

0: A     [1, 2, 3]
1: G     [1, 2]
2: CP    [1, 2, 3, 4]
3: BP    [1, 2]
4: CH    [1, 2]
5: ECG   [1, 2]
6: HR    [1, 2]
7: EIA   [1, 2]
8: HD    [1, 2]

@author: Emma Strubell
'''

# define the dependencies between variables
graph = { \
"A": [], \
"G": [], \
"CP": ["HD"], \
"BP": ["A"], \
"CH": [], \
"ECG": ["HD"], \
"HR": ["HD", "BP", "A", "G"], \
"EIA": ["HD"], \
"HD": ["BP", "CH"] \
}