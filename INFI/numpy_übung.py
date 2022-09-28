import numpy

print("1.1.1:")
print(numpy.arange(100,201,1))
print()

print("1.1.2:")
print(numpy.linspace(100,200,51))
print()

print("1.1.3:")
print(numpy.linspace(100,110,21))
print()

print("1.1.4:")
arr = numpy.random.normal(0,10,100)
print(arr)
print("---------")
print(numpy.random.randint(80,120,100))
print()

print("2.1:")
print("Mittelwert: " + str(arr.mean()))
print("Median: " + str(numpy.median(arr)))
print("Minimum: " + str(arr.min()))
print("Maximum: " + str(arr.max()))
print("Standardabweichung: " + str(numpy.std(arr)))
print()

print("2.2:")
print("Im Bereich zwischen " + str(numpy.mean(arr) - numpy.std(arr)*2) + " und " + str(numpy.mean(arr) + numpy.std(arr)*2) + " befinden sich 95% aller Werte!")
print()

print("2.3:")
print(arr*100)
print()

print("2.4:")
print(arr[:10])
print()

print("2.5:")
print(arr[numpy.argwhere(arr>=0)])