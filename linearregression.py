# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jDDQgw_XZD_2t53CA5GNQE-zOLrShqow
"""

df <- read.csv("/content/advertising.csv")

head(df)

summary (df)

require(ggplot2)

ggplot (df, aes(x=TV, y=Sales)) + geom_point(color="blue")

cor ( df$Sales, df$TV)

splitFactor <- sample(2, nrow(df), replace=T, prob=c(0.8,0.2))

train <- df[splitFactor == 1, ]
test <- df[splitFactor == 2, ]

model <- lm(Sales ~ TV, data=train)
model

summary (model)

ggplot (df, aes(TV, Sales)) + geom_point() + stat_smooth(method=lm)

confint (model)

sigma(model) * 100/mean(df$Sales)

