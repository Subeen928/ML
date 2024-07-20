import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# X=[-5,-4,-3,-2,-1,0,1,2,3,4,5]

# y=[]

# for x in X:
#     output = 3*x + 2
#     y.append(output)

# print("\t {x}, \t {y}")
# for x1,y1 in zip(X,y):
#     print(f'\t {x1},\t {y1}')

# plt.plot(X,y)


# /////////////////////////////////////////////////

# def loss_function(m, b, points):
#     total_error = 0
#     for i in range(len(points[0])):
#         x = points[0][i]
#         y = points[1][i]
#         total_error += (y - (m * x + b)) ** 2
#     return total_error / float(len(points[0]))

# def gradient_descent(m_now, b_now, points, L):
#     m_gradient = 0
#     b_gradient = 0

#     n = len(points[0])

#     for i in range(n):
#         x = points[0][i]
#         y = points[1][i]
                
#         m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
#         b_gradient += -(2/n) * (y - (m_now * x + b_now))
            
#     m = m_now - m_gradient * L
#     b = b_now - b_gradient * L
#     return m, b

# m = 0
# b = 0 
# L = 0.000000000000000000000000000000000000000001
# epochs = 1000

# for i in range(epochs):
#     if i % 50 == 0:
#         print(f'epochs {i}')
#     m, b = gradient_descent(m, b, (years, snowfall), L)

# print(epochs)
# print(m, b)

# plt.scatter(years, snowfall)
# plt.plot(years, [m * x + b for x in years], color='red')  # Line of best fit
# plt.xlabel('Years')
# plt.ylabel('Snowfall')
# plt.show()       

#////////////////////////////////////////////////////////////

years = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
snowfall = [0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]

X = np.array(years).reshape(-1, 1)
y = np.array(snowfall)

lr = LinearRegression()

lr.fit(X, y)

print(lr.coef_, lr.intercept_)
    
future_years = np.array([2024]).reshape(-1, 1)

future_snowfall = lr.predict(future_years)


plt.scatter(years, snowfall, color='blue', label='Historical Snowfall')
plt.plot(years, snowfall, color='blue')

# Plot future predictions
plt.scatter(future_years, future_snowfall, color='red', label='Predicted Snowfall')
plt.plot(future_years, future_snowfall, color='red', linestyle='dashed')

# Labels and legend
plt.xlabel('Year')
plt.ylabel('Snowfall (in meters)')
plt.title('Snowfall Prediction')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

