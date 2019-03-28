library("ggplot2")
library("gridExtra")

setwd("C:/Users/Michael/Projects/ThreadOptimizer")

compDat = read.csv("compThreadTestMaster.csv", header=T)
urlDat = read.csv("urlThreadTestMaster.csv", header=T)
rwDat = read.csv("readWriteThreadTestMaster.csv", header=T)

p1 = ggplot(compDat, aes(threadCount, runTime), main) + geom_point() + 
       geom_smooth() + ggtitle("Computationally Intensive Load")
p2 = ggplot(urlDat, aes(threadCount, runTime)) + geom_point() + 
       geom_smooth() + ggtitle("Url Request Intensive Load")
p3 = ggplot(rwDat, aes(threadCount, runTime)) + geom_point() +
       geom_smooth() + ggtitle("Input/Output Intensive Load")

grid.arrange(p1, p2, p3, ncol=2)
