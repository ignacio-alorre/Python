import matplotlib.pyplot as plt

# Global population for some years
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
revenue = [1.1, 1.2, 1.2, 1.5, 1.6, 1.8, 2.0, 2.3, 2.6, 2.9, 3.2]

# Plot the year-population
plt.plot(year, revenue)
plt.show()
plt.clf()

# Enriching the Plot
plt.plot(year, revenue)
plt.xlabel('year')
plt.ylabel('revenue')

plt.title('Company revenue per year')
plt.yticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5],
           ['0.5B', '1.0B', '1.5B', '2.0B', '2.5B', '3.0B', '3.5B'])

plt.show()


##########

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)
# After customizing, display the plot
plt.show()

