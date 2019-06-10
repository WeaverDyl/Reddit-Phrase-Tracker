library(tidyverse)
library(anytime)
library(scales)

# Load!
data_match <- read_csv("matched_comments.csv")
data_all <- read_csv("all_comments.csv")

# Create new date column from epoch
data_match <- data_match %>%
  mutate(datetime=as.POSIXct(Time, origin="1970-01-01"))

data_all <- data_all %>%
  mutate(datetime=as.POSIXct(Time, origin="1970-01-01"))

# Combine the data
data_combined <- bind_rows('Comments Matching Phrase' = data_match, 'All Comments' = data_all, .id="Color")

# Plot!
data_combined %>%
  ggplot(aes(x=datetime, y=ID)) +
  geom_line() +
  geom_area(aes(fill=Color, color=Color), position = "identity") +
  scale_fill_manual(values=c("All Comments"="dodgerblue", "Comments Matching Phrase"="pink2")) +
  scale_color_manual(values=c("All Comments"="dodgerblue4", "Comments Matching Phrase"="red")) +
  scale_x_datetime(expand=c(0,0), date_label="%H:%M", breaks=date_breaks("4 min")) +
  scale_y_sqrt(expand=c(0,0), breaks=trans_breaks(identity, identity, n = 10)) +
  theme(axis.text.x=element_text(angle = 90, vjust = 0.5), legend.position="bottom") +
  labs(x="Time", y="Uses Per Minute", title="Uses of the Word ____ Reddit Thread ____")

# Save!
ggsave(filename="finalPlot.png", plot = last_plot(),
       width = 10, height = 5, 
       units = "in",
       dpi = 300
)

