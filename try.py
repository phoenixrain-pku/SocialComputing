import matplotlib.pyplot as plt
f = open('./total_profit.csv','r')
eachtime = []
for i in range(100):
    datas = f.readline()
    data = datas.split(',')
    data = [float(i) for i in data]
    eachtime.append(sum(data))
MA10 = []

for i in range(10,len(eachtime)):
    num = 0
    for j in range(i-10,i):
        num += eachtime[i]
    num /= 10
    MA10.append(num)

plt.plot(eachtime)
plt.show()