import matplotlib.pyplot as plt
import json
dataa = None
with open('stage1.json', 'r') as fin:
    dataa = json.load(fin)

data = []
print("a", len(dataa[2]))
for i in range(6):
    summ = 0
    for j in range(10):
        summ = summ+dataa[i][j]
        print(dataa[i][j])
    data.append(summ/10.)

plt.bar(range(1, 7), data, edgecolor='black')

# Add labels and title
plt.xlabel('Judge')
plt.ylabel('Average Score')
plt.title('Score for \'correction\'')
bar_names = ['K.T.', 'K.C.', 'L.T.', 'L.C.', 'L.M.', 'L.M. 2']
plt.xticks(range(1, 7), bar_names)

plt.show()

