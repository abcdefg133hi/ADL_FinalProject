import matplotlib.pyplot as plt
import json
dataa = None
with open('stage2.json', 'r') as fin:
    dataa = json.load(fin)

data = []
print("a", len(dataa[2]))
for i in range(7):
    summ = 0
    for j in range(10):
        summ = summ+dataa[i][j]
        print(dataa[i][j])
    data.append(summ/10.)

plt.bar(range(1, 8), data, edgecolor='black')

# Add labels and title
plt.xlabel('Judge')
plt.ylabel('Average Score')
plt.title('Score for \'Celebrity Traits\'')
bar_names = ['K.T.', 'K.C.', 'L.T.', 'L.C.', 'L.M.', 'K.T. 2', 'L.M. 2']
plt.xticks(range(1, 8), bar_names)

plt.show()

