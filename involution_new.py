import numpy as np
import random
import math
import csv
from copy import deepcopy


np.random.seed(2021)
m, n = 100, 100  # m个人，n个资源点
num_m = list(range(m))
num_n = list(range(n))
zero_n = dict(zip(num_n, np.zeros(n)))

a = np.random.rand(m) / 5 + 0.4  # m个人的资源获取能力：0.4-0.6均匀分布
a = dict(zip(num_m, a))
G = dict.fromkeys(range(n), [])  # 网络
T = dict.fromkeys(range(m), zero_n.copy())  # 每个人在每个节点上的时间t
level = dict.fromkeys(range(m), zero_n.copy())  # 每个人在节点上的个人水平值
loc = np.random.randint(n, size=m)  # 每个人的出生点
loc = dict(zip(num_m, loc))
'''
person_num=dict(zip(num_n, np.zeros(n)))
for i in range(m):
    person_num[loc[i]]+=1
'''

p=0.05


def init_G(G):
    for i in range(n):
        e = np.random.randint(2, 16)  # 可以生成2-15条边
        list = random.sample(range(n), e)
        for j in range(e):
            if i == list[j] or list[j] in G[i]:
                continue
            # 这样可以
            temp = G[i].copy()
            temp.append(list[j])
            G[i] = temp.copy()

            temp = G[list[j]].copy()
            temp.append(i)
            G[list[j]] = temp.copy()

            # 这样不行
            #G[i].append(list[j])
            #G[list[j]].append(i)
    return G


def f(t, mu=1, sigma=0.5):
    res = math.exp(-(math.log(t) - mu) ** 2 / (2 * sigma ** 2)) / (t * sigma * math.sqrt(2 * math.pi))
    return res


def search(G):
    global level
    global T
    global loc
    max_iter = 200
    iter = 0
    file_name='m'+str(m)+'n'+str(n)+'p'+str(p)+'round'+str(max_iter)+'.csv'
    while True:
        print('round',iter+1,":",n)
        # 先更新累计时间和水平值
        for i in range(m):
            # 当前时刻T=1,2,...
            temp = T[i].copy()
            temp[loc[i]] += 1
            T[i] = temp.copy()   # 在当前位置的时间+1
            temp = level[i].copy()
            temp[loc[i]] += a[i] * f(T[i][loc[i]])
            level[i] = temp.copy()

        # 用更新后的水平值更新真实收益
        profit = []
        # 首先计算每个节点的总水平
        total_level = np.zeros(n)
        for i in range(n):
            for j in range(m):
                total_level[i] += level[j][i]
        for i in range(m):
            t = list(level[i].values())
            k = np.array(t)
            temp = np.divide(k ** 2, total_level, out=np.zeros_like(total_level, dtype=np.float64), where=total_level != 0)
            profit.append(np.sum(temp))
        if iter == 0:
            with open(file_name, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(profit)
        else:
            with open(file_name, "a+", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(profit)

        # 判断下一步位置
        for i in range(m):
            cur = loc[i]
            # 停留
            #person_num[loc[i]]-=1
            max_loc = cur
            max_net_earning=a[i] * f(T[i][cur] + 1)
            max_prof = (level[i][cur] + max_net_earning) / (total_level[cur] + a[i] * f(T[i][cur] + 1))
            
            # neighbors = np.nonzero(G[cur])[0]
            neighbors = G[cur]
            for j in range(len(neighbors)):
                cur = neighbors[j]
                net_earning=a[i] * f(T[i][cur] + 1)
                prof = (level[i][cur] + net_earning) / (total_level[cur] + a[i] * f(T[i][cur] + 1))
                if prof > max_prof or (prof==max_prof and net_earning>max_net_earning):
                    max_prof = prof
                    max_loc = cur
                    max_net_earning=net_earning
            loc[i] = max_loc
            #person_num[loc[i]]+=1

        iter += 1
        if iter >= max_iter:
            '''
            wrote=False
            for i in range(n):
                if person_num[i] != 0:
                    if not wrote:
                        with open('node_result.csv','w',newline='') as csvfile:
                            writer=csv.writer(csvfile)
                            writer.writerow([i+1,person_num[i]])
                        wrote=True
                    else:
                         with open('node_result.csv','a+',newline='') as csvfile:
                            writer=csv.writer(csvfile)
                            writer.writerow([i+1,person_num[i]])
            '''
            return

        add_node()


def add_node():
    global n,G
    old_n=n
    for i in range(old_n):
        rand_num=np.random.rand()
        if rand_num<=p:
            G[n]=[]
            G[n].append(i)
            G[i].append(n)
            '''
            e = np.random.randint(2, 16)  # 可以生成2-15条边
            list = random.sample(range(n), e)
            for j in range(e):
                if i == list[j] or n==list[j]:
                    continue
                temp = G[n].copy()
                temp.append(list[j])
                G[n] = temp.copy()

                temp = G[list[j]].copy()
                temp.append(n)
                G[list[j]] = temp.copy()
            '''
            #person_num[n]=0
            for j in range(m):
                T[j][n]=0
                level[j][n]=0
            n+=1



G = init_G(G)
search(G)
