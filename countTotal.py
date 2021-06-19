import matplotlib.pyplot as plt
f = open('m100n100p0.001round500.csv','r')
res = []
while True:
    strs = f.readline()
    if not strs:
        break
    nums = strs.split(',')
    nums = [float(i) for i in nums]
    res.append(sum(nums))

plt.plot(res)
plt.show()