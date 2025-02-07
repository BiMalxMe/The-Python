#concept of Noraml data distribution
'''The function np.random.normal(170, 10, 250) is a call to the normal function from the numpy.random module, 
which generates random numbers from a normal (Gaussian) distribution. Here's a breakdown of its parameters:

Mean (170): This is the mean of the normal distribution. In this case, the mean is 170. This is the central value 
around which the values are distributed.

Standard Deviation (10): This represents the spread or dispersion of the distribution. A standard deviation of
 10 means that most of the generated values will fall within 10 units of the mean (i.e., between 160 and 180), 
 with fewer values falling further away.

Number of Samples (250): This is the number of random values you want to generate from the distribution.
 Here, 250 random numbers will be generated.

So, np.random.normal(170, 10, 250) generates an array of 250 random numbers drawn from a normal distribution 
with a mean of 170 and a standard deviation of 10.
'''

import numpy as np
import matplotlib.pyplot as plt

# x = np.random.normal(170, 10, 250)#Explanation upwards
# print(x)#prints the values 




# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show() 




x = np.random.normal(170, 10, 10000)
plt.hist(x)
plt.show() 








