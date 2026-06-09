import numpy as np

# compute minimum, maximum, average, median, 95th pctile, 99th pctile of a file.
file = np.loadtxt("time_c.txt")
marks = np.array(file) 
mean_value = np.mean(marks) 
median_value=np.median(marks) 
p99p = np.percentile(marks, 99)
p95p = np.percentile(marks, 95)
mini = min(marks)
maxi = max(marks)
print("The array is:", marks)
print("Minimum:", mini)
print("Average:", mean_value)
print("Median:", median_value)
print("95th percentile:", p95p)
print("99th percentile:", p99p)
print("Maximum:", maxi)


