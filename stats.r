library("ggplot2")

setwd("C:/Users/Michael/Projects/ThreadOptimizer")

compDat = read.csv("compThreadTestMaster.csv", header=T)
urlDat = read.csv("urlThreadTestMaster.csv", header=T)
rwDat = read.csv("readWriteThreadTestMaster.csv", header=T)

ggplot(urlDat, aes(threadCount, runTime)) + geom_point() + geom_smooth()
ggplot(compDat, aes(threadCount, runTime)) + geom_point() + geom_smooth()
ggplot(rwDat, aes(threadCount, runTime)) + geom_point() + geom_smooth()

dat1 = dat[ which(dat$threadCount==1 | dat$threadCount==2), ]
dat1$threadCount = as.factor((dat1$threadCount))

dat2 = dat[ which(dat$threadCount==2 | dat$threadCount==3), ]
dat2$threadCount = as.factor((dat2$threadCount))

dat3 = dat[ which(dat$threadCount==3 | dat$threadCount==4), ]
dat3$threadCount = as.factor((dat3$threadCount))

dat4 = dat[ which(dat$threadCount==4 | dat$threadCount==5), ]
dat4$threadCount = as.factor((dat4$threadCount))

dat5 = dat[ which(dat$threadCount==5 | dat$threadCount==6), ]
dat5$threadCount = as.factor((dat5$threadCount))

m1 = glm(threadCount ~ runTime, data = dat1, family = "binomial")
m2 = glm(threadCount ~ runTime, data = dat2, family = "binomial")
m3 = glm(threadCount ~ runTime, data = dat3, family = "binomial")
m4 = glm(threadCount ~ runTime, data = dat4, family = "binomial")
m5 = glm(threadCount ~ runTime, data = dat5, family = "binomial")

summary(m1)
summary(m2)
summary(m3)
summary(m4)
summary(m5)