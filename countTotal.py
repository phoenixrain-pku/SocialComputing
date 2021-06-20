import matplotlib.pyplot as plt

def get_data(filename):    
    f = open(filename,'r')
    res = []
    while True:
        strs = f.readline()
        if not strs:
            break
        nums = strs.split(',')
        nums = [float(i) for i in nums]
        res.append(sum(nums)/len(nums))
    return res

plt.plot(get_data('m100n100p0round200.csv'))

plt.plot(get_data('m100n100p0.001round200.csv'))

plt.plot(get_data('m100n100p0.005round200.csv'))

plt.plot(get_data('m100n100p0.01round200.csv'))

plt.plot(get_data('m100n100p0.02round200.csv'))

plt.plot(get_data('m100n100p0.03round200.csv'))

plt.plot(get_data('m100n100p0.05round200.csv'))
plt.legend(['p=0','p=0.001','p=0.005','p=0.01','p=0.02','p=0.03','p=0.05'])

plt.xlabel('time')
plt.ylabel('average profit per person')
plt.title('Profit-time curve for different p at m=100, n=100')
plt.show()
plt.cla()



plt.plot(get_data('m100n100p0round200.csv'))

plt.plot(get_data('m50n100p0round200.csv'))

plt.plot(get_data('m20n100p0round200.csv'))

plt.plot(get_data('m10n100p0round200.csv'))

plt.plot(get_data('m100n200p0round200.csv'))

plt.plot(get_data('m100n500p0round200.csv'))

plt.plot(get_data('m100n1000p0round200.csv'))
plt.legend(['m=100, n=100','m=50, n=100','m=20, n=100','m=10, n=100','m=100, n=200','m=100, n=500','m=100, n=1000'])
plt.xlabel('time')
plt.ylabel('average profit per person')
plt.title('Profit-time curve for different m and n')
plt.show()
plt.cla()
