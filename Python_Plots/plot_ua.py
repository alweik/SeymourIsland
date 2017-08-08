import csv
import numpy

reader = csv.reader(open("UA_Data_modified.csv", "rb"), delimiter = ",")
x = list(reader)
result = numpy.array(x)

print result

