import matplotlib.pyplot as plt

year = [1950,1970,1980,1990,2000,2010]
pop = [100,200,300,400,500,600]
"""
plt.plot(year,pop)
plt.show()
"""
plt.scatter(year,pop)
plt.show()
#print (pop[year.index(1990)])  # this will give us the population of the year