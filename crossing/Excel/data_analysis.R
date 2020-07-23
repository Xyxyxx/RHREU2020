scatter.smooth(x = my_data$p, y = my_data$u, main = "u - p")

cor(my_data$p, my_data$u) 
cor(my_data$p, my_data$v)

lm(my_data$p ~ my_data$u)

lm(my_data$p ~ my_data$v)

plot(my_data$p, my_data$u, main = "u plotted against p",
     xlab = "p",
     ylab = "u",
     pch = 16) +
  abline(lm(my_data$u ~ my_data$p), col = "red")

plot(my_data$p, my_data$v, main = "v plotted against p", 
     xlab = "p", 
     ylab = "v",
     pch = 16) +
    abline(lm(my_data$v ~ my_data$p), col = "blue") 

lm(my_data$v ~ my_data$p)

lm(my_data$u ~ my_data$p)

cor(my_data$p, my_data$average.length.of.L_1)
