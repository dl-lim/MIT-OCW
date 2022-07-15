# Part A: Creating Models

![Figure A-1](PS5/Figure_A-1.png)

![Figure A-2](PS5/Figure_A-2.png)

### What difference does choosing a specific day to plot the data for versus calculating the yearly average have on our graphs (i.e., in terms of the R2 values and the fit of the resulting curves)? Interpret the results.
```
Choosing a specific day may not be representative of the temperatures of the entire year. It may well have been an outlier too, if not carefully chosen. Here, the R2 value is 0.05, and hence the chosen model only explains 5% of the observed values, which isn't a lot.

Choosing an average ensures that all data points are taken into account. The R2 value with this model is marginally higher than the first model, since it is higher at 0.19. Again, it only explains 19% and is still not a great model to use.
```
### Why do you think these graphs are so noisy? Which one is more noisy?
```
The noise is a result of random daily temperatures and can have a wide range of factors that determine it, from cloud cover, rain, daylight hours etc. I don't know, I'm not a geologist.

The first graph is more noisy since it only takes one day of the year, as opposed to taking an average, which should smooth out the observed values.
```
### How do these graphs support or contradict the claim that global warming is leading to an increase in temperature? The slope and the standard error-to-slope ratio could be helpful in thinking about this. 
```
The standard error over slope ratio of the first graph is 0.61 and 0.3 for the second one. The second graph shows generally lower noise. Both graphs do not strongly suggest any claim due to their low R2 values.
```


# Part B: Incorporating More Data

![Figure B](PS5/Figure_B.png)

### How does this graph compare to the graphs from part A (i.e., in terms of the R2 values, the fit of the resulting curves, and whether the graph supports/contradicts our claim about global warming)? Interpret the results.
```
It has a much higher R2 value, explaining 75% of the observed values. The standard error is also relatively lower, which shows a better fit.

The graph now can be used in supporting the claim, but it requires further thought.
```

### Why do you think this is the case?
```
As more cities are added into the dataset, the averages are spread out across a wider geographical region, hence more "global" in the warming.
```

### How would we expect the results to differ if we used 3 different cities? What about 100 different cities?
```
3 cities would likely have a lower R2 and 100 cities would likely have a higher R2, but there may be a risk of overfitting.
```

### How would the results have changed if all 21 cities were in the same region of the United States (for ex., New England)?
```
The resultant curves may only then be representative of the region and not of the "global" region.
```


# Part C: 5-year Moving Average

![Figure C](PS5/Figure_C.png)

### How does this graph compare to the graphs from part A and B (i.e., in terms of the R2 values, the fit of the resulting curves, and whether the graph supports/contradicts our claim about global warming)? Interpret the results.
```
C demonstrates the highest R2 and lowest standard error thus far, and strongly supports our claim.
```

### Why do you think this is the case? 
```
The moving average eliminates noise over time and generates a curve much closer to the trend of the data.

As such, it is a great method to understand the direction in which the data is moving over time.
```

# Part D: Predicting the Future

## I Generate more models 

![Figure D-1 1 degree](PS5/Figure_D-1-1deg.png)

![Figure D-1 2 degree](PS5/Figure_D-1-2deg.png)

![Figure D-1 20 degree](PS5/Figure_D-1-20deg.png)


### How do these models compare to each other?
```
They are all fairly accurate
```

### Which one has the best R2 ? Why?
```
The 3 degree model has the best R2. A higher order polynomial will typically fit the graph better.
```

### Which model best fits the data? Why? 
```
Although the 20-degree curve has the best R2, it is at a very high risk of overfitting.

Hence, of the 3 models available, the 2-degree model should be the best here.
```


## II Predict the results

![Figure D-2 1 degree](PS5/Figure_D-2-1deg.png)

![Figure D-2 2 degree](PS5/Figure_D-2-2deg.png)

![Figure D-2 20 degree](PS5/Figure_D-2-20deg.png)


### How did the different models perform? How did their RMSEs compare?
```
The root mean squared error increased as the number of degrees of polynomial increased
```

### Which model performed the best? Which model performed the worst? Are they the same as those in part D.2.I? Why? 
```
From the results here, the 1-degree polynomial has the lowest RMSE and thus should fit best.

This is as opposed to selecting the 2-degree polynomial in D.2.I. From the findings, I would make the judgment call to select the second model as it does not overfit, but still produces a relatively high R2 and low RMSE compared to the other models.
```

### If we had generated the models using the A.4.II data (i.e. average annual temperature of New York City) instead of the 5-year moving average over 22 cities, how would the prediction results 2010-2015 have changed? 
```
The training model had a lot more noise in A.4.II than in D. As such, the expected RMSE should be much higher and the R2 much lower.

Also, the training model in A.4.II were not trained with other cities' data, and would only explain well for New York City.
```

# Part E: Modeling Extreme Temperatures

![Figure E](PS5/Figure_E.png)

### Does the result match our claim (i.e., temperature variation is getting larger over these years)?
```
No, there is evidence of negative correlation between the year and temperature in this graph.
```

### Can you think of ways to improve our analysis? 
```
Increasing the number of degrees of polynomial may help.

We may also consider that there may be more factors other than the variation of temperatures in explaining global warming.
```