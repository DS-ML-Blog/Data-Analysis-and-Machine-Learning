library(ggplot2)
library(dplyr)

# 1. Boxplot Genre vs. Revenue

# Data preperation
# a) Spreading genre vectors into separate rows
revenue_data = data %>% select(Genre, Revenue) %>% na.omit
genre_rev_spread = data.frame(Genre = c(0), Revenue = c(0))

r = 1
for (i in 1:nrow(revenue_data)){
   for (j in revenue_data[i,'Genre'][[1]]){
       
       genre_rev_spread[r,] = c(j,revenue_data[i,'Revenue'])
       r = r+1
   } 
}
genre_rev_spread$Genre <- genre_rev_spread$Genre %>% as.factor()
genre_rev_spread$Revenue <- genre_rev_spread$Revenue %>% as.double()

# b) Selecting most popular and top revenue genres

# b1: top n popular genres
top_n_popular_genres_mx <- genre_rev_spread %>% group_by(Genre) %>% summarise(n = n()) %>% 
                           arrange(desc(n)) %>% top_n(6,n) %>% as.matrix

top_pop_rev_df <- genre_rev_spread %>% filter(Genre %in% top_n_popular_genres_mx[,'Genre']) %>% droplevels

genre_limits_pop <- top_pop_rev_df %>% group_by(Genre) %>%     # for boxplot limits setting
                    summarise(limit = (quantile(Revenue)[[4]] - quantile(Revenue)[[2]])*1.5+quantile(Revenue)[[4]])


# level reordering
pop_top_levels_ordered_pop <- 0
pop_top_levels_ordered_money <- 0

money_ordered_genres_vec <- genre_rev_spread %>% group_by(Genre) %>% summarise(median = median(Revenue)) %>% 
                            arrange(desc(median)) %>% select(-2) %>% as.matrix() %>% as.vector()

top_pop_levels <- top_pop_rev_df$Genre %>% levels

pop_top_levels_ordered_pop <- top_n_popular_genres_mx[,'Genre']

pop_top_levels_ordered_money <- c(0)
i = 1
for (genre in money_ordered_genres_vec){
    if (genre %in% pop_top_levels_ordered_pop){
        pop_top_levels_ordered_money[i] <- genre
        i = i+1 
    }
}

# Levels' reorganization 
pop_result_1 <- top_pop_rev_df
pop_result_1$Genre <- factor(top_pop_rev_df$Genre, levels = pop_top_levels_ordered_money)

pop_result_2 <- top_pop_rev_df
pop_result_2$Genre <- factor(top_pop_rev_df$Genre, levels = pop_top_levels_ordered_pop)


# b2: top n money genres
top_n_money_genres_mx <- genre_rev_spread %>% group_by(Genre) %>% summarise(median = median(Revenue)) %>% 
                             arrange(desc(median)) %>% top_n(6,median) %>% as.matrix

top_money_rev_df <- genre_rev_spread %>% filter(Genre %in% top_n_money_genres_mx[,'Genre']) %>% droplevels

genre_limits_money <- top_money_rev_df %>% group_by(Genre) %>%     # for boxplot limits setting
                      summarise(limit = (quantile(Revenue)[[4]] - quantile(Revenue)[[2]])*1.5+quantile(Revenue)[[4]])

# level reordering
money_top_levels_ordered_money <- 0
money_top_levels_ordered_pop <- 0

pop_ordered_genres_vec <- genre_rev_spread %>% group_by(Genre) %>% summarise(n = n()) %>% 
                          arrange(desc(n)) %>% select(-2) %>% as.matrix() %>% as.vector()

top_money_levels <- top_money_rev_df$Genre %>% levels   

money_top_levels_ordered <- top_n_money_genres_mx[,'Genre']

money_top_levels_ordered_money <- c(0)
i = 1
for (genre in money_ordered_genres_vec){
    if (genre %in% money_top_levels_ordered){
        money_top_levels_ordered_money[i] <- genre
        i = i+1 
    }
}

money_result_1 <- top_money_rev_df
money_result_1$Genre <- factor(top_money_rev_df$Genre, levels = money_top_levels_ordered_money)

money_top_levels_ordered_pop <- c(0)
i = 1
for (genre in pop_ordered_genres_vec){
    if (genre %in% money_top_levels_ordered){
        money_top_levels_ordered_pop[i] <- genre
        i = i+1 
    }
}

money_result_2 <- top_money_rev_df
money_result_2$Genre <- factor(top_money_rev_df$Genre, levels = money_top_levels_ordered_pop)



# c) Visualization 

# c1: Top n popular genres
boxplot_1_1 <- ggplot(pop_result_1, aes(x = Genre, y = Revenue)) + geom_boxplot(fill = 'orange') +
             labs(x = 'Gatunek', y = 'Wartoœæ przychodów [mln $]', title = 'Rozk³ad przychodów dla poszczególnych gatunków') +
             theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5))

boxplot_1_1
ggsave('plots/boxplot_pop_1.png', width = 7, height = 7, dpi = 300)
# ---

boxplot_1_2 <- ggplot(pop_result_1, aes(x = Genre, y = Revenue)) + 
    geom_boxplot(fill = 'orange', outlier.size = -1, fill = 'orange') +
    labs(x = 'Gatunek', y = 'Wartoœæ przychodów [mln $]', title = 'Rozk³ad przychodów dla poszczególnych gatunków') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) + ylim(0,1.05*max(genre_limits_pop$limit))

boxplot_1_2
ggsave('plots/boxplot_pop_2.png', width = 7, height = 7, dpi = 300)
# ---

boxplot_1_3 <- ggplot(pop_result_2, aes(x = Genre, y = Revenue)) + geom_boxplot(fill = 'orange', outlier.size = -1) +
    labs(x = 'Gatunek', y = 'Wartoœæ przychodów [mln $]', title = 'Rozk³ad przychodów dla poszczególnych gatunków') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) + ylim(0,1.05*max(genre_limits_pop$limit))

boxplot_1_3
ggsave('plots/boxplot_pop_3.png', width = 7, height = 7, dpi = 300)

# c2: Top n money genres
boxplot_2_1 <- ggplot(money_result_1, aes(x = Genre, y = Revenue)) + geom_boxplot(fill = 'orange', outlier.size = -1) +
    labs(x = 'Gatunek', y = 'Wartoœæ przychodów [mln $]', title = 'Rozk³ad przychodów dla poszczególnych gatunków') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) + ylim(0,1.05*max(genre_limits_money$limit))

boxplot_2_1
ggsave('plots/boxplot_money_1.png', width = 7, height = 7, dpi = 300)
# --
boxplot_2_2 <- ggplot(money_result_2, aes(x = Genre, y = Revenue)) + geom_boxplot(fill = 'orange', outlier.size = -1) +
    labs(x = 'Gatunek', y = 'Wartoœæ przychodów [mln $]', title = 'Rozk³ad przychodów dla poszczególnych gatunków') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) + ylim(0,1.05*max(genre_limits_money$limit))

boxplot_2_2
ggsave('plots/boxplot_money_2.png', width = 7, height = 7, dpi = 300)



# 2. Genre vs. Year
# a) Data prepearation
genre_year_data = data %>% select(Genre, Year) %>% na.omit

genre_year_spread = data.frame(Genre = c(0), Year = c(0))

r = 1
for (i in 1:nrow(genre_year_data)){
    for (j in genre_year_data[i,'Genre'][[1]]){
        
        genre_year_spread[r,] = c(j,genre_year_data[i,'Year'])
        r = r+1
    } 
}
genre_year_spread$Genre <- genre_year_spread$Genre %>% as.factor() 
genre_year_spread$Year <- genre_year_spread$Year %>% as.factor() 

genre_year_spread <-  genre_year_spread %>% filter(Genre %in% pop_top_levels_ordered_pop)
# reorder:
jitter_result <- genre_year_spread
jitter_result$Year <- factor(jitter_result$Year, levels = c(1,2,3,4,5,6,7,8,9,10,11) )


jitter_plot <- ggplot(jitter_result, aes(x = Year, y = Genre)) + geom_jitter(fill = 'orange') + 
    labs(x = 'Rok', y = 'Gatunek', title = 'Iloœæ filmów najpopularniejszych gatunków \n w kolejnych latach') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) +
    scale_x_discrete(labels=seq(2006,2016)) 



jitter_plot
ggsave('plots/year_genre_plot.png', width = 7, height = 7, dpi = 300)



