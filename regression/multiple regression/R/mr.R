datasets=read.csv('50_Startups.csv')


datasets$State=factor(datasets$State,
                      levels = c('New York','California','Florida'),
                      labels = c(1,2,3))


install.packages("caTools")

library(caTools)

set.seed(123)
split=sample.split(datasets$Profit,SplitRatio=0.8)
# true=training set and false= test sets
training_set=subset(datasets,split==TRUE)
test_set=subset(datasets,split==FALSE)

re=lm(formula = Profit~R.D.Spend + Administration + Marketing.Spend + State,data=datasets)

re=lm(formula = Profit~R.D.Spend + Administration + Marketing.Spend ,data=datasets)

re=lm(formula = Profit~R.D.Spend  + Marketing.Spend ,data=datasets)

re=lm(formula = Profit~R.D.Spend   ,data=datasets)




y_pred=predict(re,newdata = test_set)
