library(dplyr)
library(stringr)
library(visdat)
library(ggplot2)

setwd('C:\\Path\\to\\project')
data = read.csv('data.csv')


# Deletes unneeded columns and changes names 
data$Description = NULL
data$Director = NULL
data$Title = NULL
data$Votes = NULL
data$Actors = NULL
data$Rank = NULL
names(data)[3] <- 'Runtime'
names(data)[5] <- 'Revenue'

# Types conversion
data$Year <- as.factor(data$Year)
data$Genre <- as.character(data$Genre) 

# Extracting genres names
data$Genre <- strsplit(data$Genre, ',')
 
# Rating normalization
data$Rating <- data$Rating*10

# Missing data visualization
vis_miss(data)
ggsave('plots/missing_data.png', width = 7, height = 7, dpi = 300)

vis_dat(data[-c(2,3)])

# Covariance and correlation
data_no_na <- data %>% filter(Metascore %>% is.na == F)
cov(data_no_na$Rating, data_no_na$Metascore)
cor(data_no_na$Rating, data_no_na$Metascore)


