# What substring do hish and fish have in common ?
# How about hish and vista ?
# Thats what we'll calculate


# grid
cell = []

word_a = 'fosh'
word_b = 'fort'

l_c_s = 0


# initiating with 0 values

for a in range(0, len(word_a)):
    cell.append(list(0 for b in word_b))


for i in range(0, len(word_a)):
    for j in range(0, len(word_b)):
        if word_a[i] == word_b[j]:
            cell[i][j] = cell[i-1][j-1] + 1
            # recording the longest common substring because answer is not always in last cell
            l_c_s = max(l_c_s, cell[i][j])
        else:
            cell[i][j] = 0


for c in cell:
    print(c)

print('Longest common substring: {l}'.format(l=l_c_s))