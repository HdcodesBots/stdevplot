import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random


df = pd.read_csv("charts/newdata.csv")
data = df["average"].tolist()
#code to find the mean and stdev of 100 points 
ds = []

for i in range(0,100):
    r_index = random.randint(0,len(data))
    val = data[r_index]
    ds.append(val)
    
mean = statistics.mean(ds)
stdev = statistics.stdev(ds)

print("The mean of sample : \n" , mean)
print("The standard deviation of sample : \n" , stdev)

# function to get mean of the given data samples
def rand_set_of_mean(counter):
    ds = []

    for i in range(0,counter):
        r_index = random.randint(0,len(data))
        val = data[r_index]
        ds.append(val)
        
    mean = statistics.mean(ds)
    return mean

# function to plot the mean on the graph 
def plot_mean(mean_list):
    df = mean_list 
    fig = ff.create_distplot([df] , ["average"], show_hist=False)
    fig.show()

# funtion to get mean of 100 data points 1000 times and plot the graph     

def setup():
    mean_list = []
    
    for i in range(0,1000):
        set_of_means = rand_set_of_mean(100)
        mean_list.append(set_of_means)
        
    plot_mean(mean_list)
    mean1 = statistics.mean(mean_list)
    print(mean1)

setup()

population_mean = statistics.mean(data)
print(population_mean)

def st_dev ():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = rand_set_of_mean
        mean_list.append(set_of_mean)
        
    stdev1 = statistics.stdev(mean_list)
    print(stdev1)
    
st_dev()