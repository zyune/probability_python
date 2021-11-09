import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
# n=20
# p=0.2
# x=np.arange(0,21,1)
# y_pmf= stats.binom.pmf(x,n,p)
# y_cdf=stats.binom.cdf(x,n,p)
# plt.bar(x,y_pmf)
# plt.plot(x,y_cdf,color="#fc4f30")
# plt.title('binomial distriburion : n=%i,p=%.2f'%(n,p))

# 第二个实验 参数p固定为0.2，参shun0de时候二项分布的概率分布曲线
# In probability and statistics, a probability mass function is a function that gives the probability that a discrete random variable is exactly equal to some value.[1] Sometimes it is also known as the discrete density function. The probability mass function is often the primary means of defining a discrete probability distribution, and such functions exist for either scalar or multivariate random variables whose domain is discrete.

# A probability mass function differs from a probability density function(PDF) in that the latter is associated with continuous rather than discrete random variables. A PDF must be integrated over an interval to yield a probability.[2]

# The value of the random variable having the largest probability mass is called the mode.
# n = 10
# p = 0.2
# x = np.arange(0, 11, 1)
# y_pmf = stats.binom.pmf(x, n, p)
# plt.plot(x, y_pmf, "o-")

# plt.show()

# 第三个实验 固定n=10,p=0.25,0.5,0.75时的二项分布的概率分布曲线
n = 10
x = np.arange(0, 11, 1)
plt.plot(x, stats.binom.pmf(x, n, 0.25), "o-", color="blue")
plt.plot(x, stats.binom.pmf(x, n, 0.5), "o-", color="red")
plt.plot(x, stats.binom.pmf(x, n, 0.75), "o-", color="green")
plt.show()
