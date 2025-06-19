datasets=read.csv('Salary_Data.csv')
install.packages("caTools")

library(caTools)

set.seed(123)
split=sample.split(datasets$Salary,SplitRatio=2/3)
# true=training set and false= test sets
training_set=subset(datasets,split==TRUE)
test_set=subset(datasets,split==FALSE)

#fitting  Simple Linear Regression to the training set

regressor=lm(formula = Salary ~ YearsExperience,data = training_set)

y_pred=predict(regressor,newdata = test_set)

install.packages("ggplot2")
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),colour='red')+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set)),
            colour='blue')+
  ggtitle('Salary VS Exerience(training set)')
xlab('Years of experience')+
  ylab('Salary')

ggplot()+
  geom_point(aes(x=test_set$YearsExperience,y=test_set$Salary),colour='red')+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set)),
            colour='blue')+
  ggtitle('Salary VS Exerience(test set)')
xlab('Years of experience')+
  ylab('Salary')


  
