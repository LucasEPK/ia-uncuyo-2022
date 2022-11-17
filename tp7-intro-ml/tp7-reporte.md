# TP7 reporte
### Lucas Moyano

## 1. 
**For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.**

	(a) **The sample size n is extremely large, and the number of predictors p is small.**

	(b) **The number of predictors p is extremely large, and the number of observations n is small.**

	(c) **The relationship between the predictors and response is highly non-linear.**

	(d) **The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.**
	

a) The *flexible stastistical learning method* is gonna be better than the inflexible method, because, in general, fitting a more flexible model requires estimating a greater number of parameters.

b) The *inflexible stastistical learning method* is gonna be better than the flexible method, because since the number of observations is small then if we use flexible methods there's gonna be too much noise, making the function inaccurate to the real one

c) The *flexible stastistical learning method* is gonna be better than the inflexible method, because the flexible method is good at dealing with non linear functions

d) The *flexible stastistical learning method* is gonna be better than the inflexible method, because if a method has high variance then small changes in the training data can result in large changes in f~

## 2.
**Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.**

	(a) **We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.**

	(b) **We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.**

	(c) **We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.**
	
a) It's a *classification problem* and we are insterested in the *inference*. n=500 p=5

b) It's a *classification problem* and we are insterested in the *prediction*. n=20 p=14

c) It's a *regression problem* and we are insterested in the *prediction* n=52 p=4

## 5.
**What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?**

The advantages for using a *very flexible* approach is that it is accurate to the data but the disadvantage is that it's not accurate to the real function f while the less flexible one is more accurate to the function

A more flexible approach is preferred when we have a lot of data, while a less flexible approach is prefered when we don't.

## 6.
**Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?**

The main difference between a parametric statistical learning approach and a non parametric one is that the parametric one makes an explicit assumption about the function f while the non parametric one seeks an estimate of f that gets as close to the data points as possible without being too tough or wiggly.

The advantage of a parametric approach is that we only have to estimate a set of parameters instead of an entire function f, the disadvantage is that it could possibly not match the true form of f. While a non-parametric approach doesn't have the limitation of not matching the true form of f, it also has the disadvantage that we need a big number of observation for it to be accurate

## 7.
**The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.**

**Obs. X1 X2 X3 Y**

**1 0 3 0 Red**

**2 2 0 0 Red**

**3 0 1 3 Red**

**4 0 1 2 Green**

**5 −1 0 1 Green**

**6 1 1 1 Red**

**Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.**
	(a) **Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.**
	(b) **What is our prediction with K = 1? Why?**
	(c) **What is our prediction with K = 3? Why?**
	(d) **If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?**

a) E(1,2)= root(13)

E(1,3)= root(13)

E(1,4)= root(8)

E(1,5)= root(11)

E(1,6)= root(6)

E(2,3)= root(14)

E(2,4)= 3

E(2,5)= root(10)

E(2,6)= root(3)

E(3,4)= 1

E(3,5)= root(6)

E(3,6)= root(5)

E(4,5)= root(3)

E(4,6)= root(2)

E(5,6)= root(5)



E(1,0)= 3

E(2,0)= 2

E(3,0)= root(10)

E(4,0)= root(5)

E(5,0)= root(2)

E(6,0)= root(3)

b) our prediction with K=1 is *green* because the observation 5 is the nearest one

c) our prediction with K=3 is *red* because the 3 nearest observation are {5,6,2} which Y is {Green, Red, Red} in that order

d) We would expect the best value for K to be smaller because when K is small the decision boundary is more flexible so it's more fit for a nonlinear bayes boundary