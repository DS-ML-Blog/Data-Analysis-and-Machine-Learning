library(ggplot2)

# Year distribution
year_dist_plot <- ggplot(data, aes(x = Year)) + geom_bar(color = 'black', fill = 'orange') + 
                  labs(x = 'Rok produkcji', y = 'Liczba filmów', title = 'Liczba wyprodukowanych filmów w kolejnych latach') + 
                  theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5))

year_dist_plot
ggsave('plots/year_dist.png', width = 7, height = 7, dpi = 300)

# Runtime distribution
runtime_dist_plot <- ggplot(data, aes(x = Runtime)) + geom_histogram(color = 'black', fill = 'orange', binwidth = 10) +
                    labs(x = 'Czas trwania [min]', y = 'Liczba filmów', title = 'Rozk³ad czasu trwania filmu') +
                    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) +
                    scale_x_continuous(breaks = scales::pretty_breaks(n = 15))
  
runtime_dist_plot
ggsave('plots/runtime_dist.png', width = 7, height = 7, dpi = 300)

# Rating & metascore distribution 
rating_score_plot <- ggplot(data, aes(x = Rating, y = Metascore)) + geom_point() +
                     labs(x = 'Ocena widzów', y = 'Ocena krytyków', title = 'Ocena krytyków vs. ocena widzów') +
                     theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) +
                     xlim(0, 100) + ylim(0, 100) + coord_fixed() + 
                     geom_abline( aes(slope=1, intercept=0, color = 'a1'), size = 1.5) +
                     geom_smooth(method = 'lm', se = F, aes(color = 'a2'), size = 1.5) + 
                     scale_colour_manual('',values=c(a1="red", a2="blue"), 
                                         labels = c('y=x','Linia trendu'))

rating_score_plot
ggsave('plots/rating_score_dist.png', width = 7, height = 7, dpi = 600)

# Revenue distribution
revenue_dist_plot <- ggplot(data, aes(x = Revenue)) + 
    geom_histogram(color = 'black', fill = 'orange', bins = 50) +
    labs(x = 'Przychody z filmu [mln $]', y = 'Liczba filmów', title = 'Rozk³ad przychodów z filmu') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) +
    scale_x_continuous(breaks = scales::pretty_breaks(n = 5))

revenue_dist_plot
ggsave('plots/revenue_dist.png', width = 7, height = 7, dpi = 300)


# Rating & metascore distribution vs. revenue
rating_score_revenue_plot <- ggplot(data, aes(x = Rating, y = Metascore)) + 
    geom_point(aes(color = Revenue, size = Revenue)) +
    labs(x = 'Ocena widzów', y = 'Ocena krytyków', title = 'Ocena krytyków vs. ocena widzów') +
    theme_classic(base_size = 15) + theme(plot.title = element_text(hjust = 0.5)) +
    xlim(0, 100) + ylim(0, 100) + coord_fixed() +
    scale_fill_gradientn(colours=c("red","green","blue"))
    
rating_score_revenue_plot
ggsave('plots/score_revenue_dist.png', width = 7, height = 7, dpi = 600)

