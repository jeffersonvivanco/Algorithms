# longest common subsequence: the number of letters in a sequence that the two words have in common

word_a = 'fish'
word_b = 'fosh'

# grid
cell = []
l_c_sub_seq = 0

for a in range(0, len(word_a)):
    cell.append(list(0 for b in word_b))

for i in range(0, len(word_a)):
    for j in range(0, len(word_b)):
        if word_a[i] == word_b[j]:
            cell[i][j] = cell[i-1][j-1] + 1
            l_c_sub_seq = cell[i][j]
        else:
            cell[i][j] = max(cell[i][j-1], cell[i-1][j])

for c in cell:
    print(c)

print('longest common subsequence: {l}'.format(l=l_c_sub_seq))