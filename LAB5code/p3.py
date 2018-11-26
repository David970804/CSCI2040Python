import matplotlib.pyplot as plt
import numpy as np

#histogram
random_numbers = np.random.normal(0,1,1000)
plt.hist(random_numbers,bins=15,density = True, ec = 'black')
plt.xlabel("x")
plt.ylabel("Density")
plt.grid(True)
plt.savefig("histogram.png")
plt.close()
#pie chart
plt.pie(np.array([3400,3147,3272],dtype = int), labels = ['NA','CC','UC'],autopct='%1.1f%%',shadow = True)
plt.axis('equal')
plt.savefig('pie.png')
plt.close()
#bar chart
college_name = ['mc','sh','cw','uc','cc','na','sc','wys','ws']
college_number = [300,600,300,3272,3147,3400,3441,1200,1389]
plt.bar(college_name,college_number)
plt.xlabel("college")
plt.ylabel("number of peaple")
plt.savefig("bar.png")
plt.close()
#scatter plot and line chart
x_list = np.linspace(0, 1, 100)
y_list = x_list + np.random.rand(100)
plt.scatter(x_list,y_list)
plt.plot(x_list,x_list)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('scatter_line.png')
plt.close()