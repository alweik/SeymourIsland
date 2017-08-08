import csv
import numpy
import matplotlib.pyplot as mpl
import seaborn as sns

reader = csv.reader(open("/Users/aweik/Documents/working/UA_Data_modified.csv", "rb"), delimiter = ",")
x = list(reader)
result = numpy.array(x)

print result
result

sns.set_style("whitegrid")
result = sns.load_dataset("result")
ax = sns.stripplot(x = "taxa", y = "UA", data = result)