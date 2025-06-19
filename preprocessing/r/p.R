datasets=read.csv('data.csv')
datasets$Age  = ifelse(is.na(datasets$Age),ave(datasets$Age,FUN = function(x) mean(x,na.rm=TRUE)),
                                               datasets$Age
                       )
datasets$Salary  = ifelse(is.na(datasets$Salary),ave(datasets$Salary,FUN = function(x) mean(x,na.rm=TRUE)),
                       datasets$Salary
)

datasets$Country=factor(datasets$Country,levels = c('France','Spain','Germany'),labels = c(1,2,3))
datasets$Purchased=factor(datasets$Purchased,levels = c('No','Yes'),labels = c(0,1))

install.packages("caTools")

library(caTools)

set.seed(123)
split=sample.split(datasets$Purchased,SplitRatio=0.8)
# true=training set and false= test sets
training_set=subset(datasets,split==TRUE)
test_set=subset(datasets,split==FALSE)
#feature scaling 
training_set[,2:3]=scale(training_set[,2:3])
test_set[,2:3]=scale(test_set[,2:3])