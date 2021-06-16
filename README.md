# 内卷问题建模与分析
## 内卷问题简介

内卷本意是一类文化模式达到了某种最终的形态以后, 既没有办法稳定下来, 也没有办法转变为新的形态, 而只能不断地在内部变得更加复杂的现象. 

目前, "内卷"已经成为流行语. 日常讨论中的"内卷"与学术概念"内卷"是不同的? 从网上一些流行文字中可窥一斑. 有人说, "什么叫作内卷? 说白了就是过剩的人口投入到有限资源的争夺之中". 有人把"内卷"用在了教育竞争上, 如招生名额是一定的, 报考人数也是一定的, 但有的学校开始补课, 其余学校担心考分落后都跟着补课, 结果所有人的考分都提高了, 但录取分数线也随之提高了. 也有人把"内卷"用于职场竞争, 如一些人为了在领导面前表现努力工作, 经常不按时下班, 其他人也如法炮制, 最后形成大家都故意加班的局面. 

对于上述对"内卷"现象的描述, 我们可以概括性地定义为: 同行间竞相付出更多努力以争夺有限资源, 从而导致个体"收益努力比"下降的现象, 可以看作是努力的"通货膨胀". 

本文接下来会建立内卷现象的社会网络模型与模型演化规则, 并论述该模型对实际社会描述时的合理性. 接下来通过一系列模拟实验, 探究在不同的初始化条件下, 模型最终的演化状态, 并分析结果所对应的实际社会中的现象, 与相应现象所产生的原因.

## 模型构造

我们建立的第一个网络模型是以群体中的每个人为研究对象, 每个人是一个节点, 人与人之间所连的边表示两人间存在关系. 当节点上的人"不卷"时, 节点被赋值为 $0$; 当节点上的人"卷"时, 节点被赋值为 $1$. 随着时间 $t$ 的演化规则如下:

1. 初始状态下, 网络中占比 $0<w<1$ 的节点值为 $1$ , 剩余的占比 $1-w$ 的节点的值都为 $0$.
2. 每次演化时, 网络中的每个节点根据其所有邻居的行为进行状态选择. 若他的邻居中有占比超过 $q$ 的值为 1, 他也会转变为 1.

这个模型和课上所讲的网络级联模型很像, 可以说是网络级联的一个实例. 其中初值为 $1$ 的节点即为初用节点集合, $q$ 即对应着网络级联中"门槛值"的定义.

这个模型较为简单, 不同的初值与演化规则所导致的不同结果也在课上已有诸多讨论. 并且, 所有将人作为节点并互相影响的模型都可以看作是网络级联模型的拓展和延申: 每个人根据自己的现有收益, 目标收益与他人的行为来改变自我的行为. 这是对真实的社会的一个较为简单的抽象, 在本文中不再赘述.

我们建立第二个模型时改变了思路, 不再将人作为网络中的节点, 而将"资源点"作为网络中的节点. 节点可以被考虑为现实社会中有限资源的载体, 边被考虑为可以互通的资源载体. 人们可以在某个资源点上进行积累, 也可以从某个资源点转移到相邻的资源点. 一个例子如下: 考虑一片由 $n$ 块农田组成的土地. 每个人可以选择在自己当前的农田上进行开垦, 也可以转移到与之相邻的农田上进行开垦. 但每块农田所能提供的资源是有上限的, 人们不可能无条件地一直开垦并受益, 因此随着开垦次数的增加, 农田的出产能力应当是递减的; 且每块农田上可能会有多个人在开垦, 随着人数增多, 每个人的获益也是递减的. 在这个例子中, 农田是网络的节点, 相互可达的农田是网络的边; 人作为外力介入到模型中 (每次搜索一块最优的农田进行开垦), 从而影响整个网络的演化.

我们接下来给出基于上述模型的一些基本设定, 论述其合理性, 并给出网络模型与演化规则的形式化描述.

### 基本设定

记资源点构成的无向图为 $G=\lang V,E\rang$, 社会中人的集合为 $S$.

1. 不考虑其他人时, 每个人在每个资源点上能获取的资源, 随着时间的推进将先增高后降低. 这与现实社会情况是吻合的, 在进行技能的学习时, 入门与起步阶段的收益整体上较低, 学到一定程度后会逐渐增高, 但随着水平越来越高, 想再做出提升并取得收益的难度也会逐渐增加, 这也是一种边际递减效应. 将每个人在该资源点上不考虑其他人时的收益记为"个人水平值".

2. 每个资源点产出资源的能力, 随着它已产出资源的总量呈现边际递减效应. 这与现实社会情况是吻合的, 比如正在进行小升初的小学生群体中, "数学好"这一技能所能带来的优势被视为资源, 那么当会群体的数学水平不断上升, 想要通过数学学习上的提升来获得资源将会愈加困难. 我们将每个人在资源点上考虑其他人时的收益记为"真实收益值".

3. 由 $1$ 和 $2$, 不难想象, 每个人在每个资源点上会有一个"个人水平值"与"真实收益值", "个人水平值"只与个体有关, "真实收益值"与群体有关. 

   对于某个人 $P_i$ 与某个资源点 $V_j$, $P_i$ 在 $V_j$ 上的个人水平值可以被定义为:
   $$
   v_{i,j}(t) =a_i \int_{t=0}^{T_{i,j}} f_j(t){\rm d}t.
   $$
   此处 $T_{i,j}$ 是 $P_i$ 在 $V_j$ 上投入的总时长, $a_i$ 表明了他的资源获取能力, 在个体间有差异. $f_j(t)$ 是个人水平值的增长函数, 随 $t$ 先递增后递减, 且一致收敛. 这保证了 $\int_{t=0}^{+\infty}f_j(t){\rm d}t$ 有限.

   对于某个人 $P_i$ 与某个资源点 $V_j$, $P_i$ 在 $V_j$ 上的真实收益值可以被定义为:
   $$
   w_{i,j}(t) = v_{i,j}(t)\cdot\frac{v_{i,j}(t)}{\sum_{P_{i'}\in S}v_{i',j}(t)}.
   $$
   其中 $S$ 为所有人的集合. 上式中, $w_{i,j}(t)$ 表示真实收益值, 涵义是真实收益值乘以一个缩小因子, 该缩小因子为当前节点上 $P_i$ 的个人水平值与整个社会群体的个人水平值之和的比例.

4. 每个资源节点 $V_i$ 的可达节点为 $\{V_i\}\cup \{V_j\mid (V_i,V_j)\in E\}$, 即该节点与它的所有邻居.

5. 每个人 $P_i$ 在任意时刻 $T$ 都知道它所有可达节点上整个社会群体的个人水平值之和.

6. 每个人 $P_i$ 在选择下一步的资源获取点时是短视贪心的: $P_i$ 在他当前占据节点的所有可达节点中选择一个期望收益最高的节点, 并转移到该节点进行工作.

### 模型与演化规则

该模型中的无向图为 $G=\lang V,E\rang$, 其中 $|V|=n$; 社会中人的集合为 $S$, 其中 $|S|= m $; 社会中人的资源获取能力为 $m$ 维向量 $ A=(a_0,a_1,\cdots, a_{m-1})$. 演化过程是离散的, 即 $t = 0,1,2,\cdots$. 演化规则如下:

1. 第 $0$ 轮: 对图 $G$ 进行随机的初始化操作, 随机选择一定数量的节点对 $(V_i,V_j)$ 连边; 对 $S$ 进行初始化操作, 给每个人在 $V$ 中选择一个初始资源点. 对 $A$ 进行初始化操作, 以 $(0,1)$ 上的均匀分布对每一位进行独立赋值, 即 $a_i\sim U(0,1)$. 对所有的节点 $V_j$, 定义单个人的资源获取函数都为满足 $\mu=1,\sigma=0.5$ 的 $\log$ 正态分布函数. 这是一个积分有限且满足先增后减的函数. 其函数形式为:
   $$
   f(t) =\frac{\exp \left(-0.5\cdot\frac{1}{0.5^2}\cdot(\ln x - 1)^2\right)}{\sqrt{2\pi}\cdot 0.5}.
   $$

2. 第 $1$ 轮: 每个人在当前选择的节点上进行工作. 显然, 对任一人而言, 这一次其真实收益值与个人水平值是相等的, 都为 $a_if(1)$.

3. 第 $T$ 轮: 每个人在第 $T-1$ 轮的基础上进行短视贪心搜索, 在其所有可达节点中选择一个预估收益最大的节点, 并转移到该节点上进行工作. 但注意: 转移之后真实的收益和预估收益可能不同.

   对于人 $P_i$, 他在第 $T-1$ 轮结束时, 在节点 $V_j$ 的个人水平值为:
   $$
   v_{i,j}(T-1)=\sum_{t=0}^{t_{i,j}(T-1)}a_if(t).
   $$
   其中函数 $t_{i,j}(x)$ 表示第 $x$ 轮结束时, $P_i$ 在节点 $V_j$ 已工作的时间. 由于每轮只能选择一个节点进行工作, 因此应有: $\sum_{j}t_j(x)=x$.

   他在第 $T$ 轮如果选择节点 $V_j$ 进行工作, 在每个节点付出的时间变为:
   $$
   \overline t_{i,j'}(T) = t_{i,j'}(T-1)\quad {\rm if}~~j'\neq j,
   \\
   \overline t_{i,j'}(T) =t_{i,j'}(T-1)+1\quad {\rm if}~~j'= j.
   $$
   个人水平值变为:
   $$
   \overline v_{i,j}(T)=v_{i,j}(T-1)+a_if(t_{i,j}(T-1)+1).
   $$
   预估的收益应为:
   $$
   \overline w_{i,j}(T)=\frac{(v_{i,j}(T-1)+a_if(t_{i,j}(T-1)+1))^2}{{\sum_{P_{i'}\in S}v_{i',j}(T-1)}+a_if(t_{i,j}(T-1)+1)}.
   $$
   在计算预估收益时, $P_i$ 只会考虑该节点现有的总资源与自己带来的资源增加, 而不会考虑下一轮其他人可能带来的资源增加. 因此, 当所有人做完选择 (即按照演化规则, 在所有可达节点中选择了预期收益最大的), $P_i$ 在 $ V_j$ 真实的收益应为:
   $$
   w_{i,j}(T) =\sum_{t=0}^{t_{i,j}(T)}a_if(t)\cdot \frac{\sum_{t=0}^{t_{i,j}(T)}a_if(t)}{{\sum_{i\in S}v_{i,j}(T)}}.
   $$
   在第 $T$ 轮时, $P_i$ 的真实总收益为他在每个节点的真实收益之和, 应为:
   $$
   w_i(t) = \sum_{V_j\in V}w_{i,j}(T).
   $$

4. 重复步骤 $3$.

对于该模型而言, 网络演化规则的核心即为**短视贪心**的搜索, 每人在结束本轮资源获取后, 转移向预估的下一轮将能取得最多资源的节点. 但最终的结果也许并不如此, 因为如果人们都大量涌向某个资源点, 在这个节点的真实收益反而可能较低. 并且, 对于某些节点, 如果 $P_i$ 不在该节点继续工作下去, 而其他人加入了这个节点进行工作, 随着时间推移, 他能获得的收益也会逐渐降低. 这与现实资源分配中"不进则退"的现象也是非常吻合的. 因此, 本模型真实刻画了社会现实中的"内卷"情况.

## 理论分析

## 实验设计

## 实验结果

## 结论 