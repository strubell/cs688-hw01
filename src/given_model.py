'''
CS688 HW01: Given Bayes net

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

# define the mapping from variable to idx in data
data_idx = { \
"A": 0, \
"G": 1, \
"CP": 2, \
"BP": 3, \
"CH": 4, \
"ECG": 5, \
"HR": 6, \
"EIA": 7, \
"HD": 8 \
}

# define the domain of each variable
domains = { \
"A": 3, \
"G": 2, \
"CP": 4, \
"BP": 2, \
"CH": 2, \
"ECG": 2, \
"HR": 2, \
"EIA": 2, \
"HD": 2 \
}

# define the dependencies between variables
graph = { \
"A": [], \
"G": [], \
"CP": ["HD"], \
"BP": ["G"], \
"CH": ["A", "G"], \
"ECG": ["HD"], \
"HR": ["HD", "BP", "A"], \
"EIA": ["HD"], \
"HD": ["BP", "CH"] \
}

# provide names for the categorical variables
variable_map = { \
"A": ["< 45", "45--55", "\geq 55"], \
"G": ["Female", "Male"], \
"CP": ["Typical", "Atypical", "Non-Anginal", "None"], \
"BP": ["Low", "High"], \
"CH": ["Low", "High"], \
"ECG": ["Normal", "Abnormal"], \
"HR": ["Low", "High"], \
"EIA": ["No", "Yes"], \
"HD": ["No", "Yes"] \
}