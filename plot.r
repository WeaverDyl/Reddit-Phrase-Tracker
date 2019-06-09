library(tidyverse)
library(anytime)
library(ggplot2)

# Load data
data <- read_csv("comments.csv")

# Create new date column from epoch
data <- data %>%
  mutate(datetime=as.POSIXct(Time, origin="1970-01-01"))

# Plot!
data %>%
  ggplot(aes(x=datetime, y=id)) +
  geom_line() +
  scale_x_datetime(expand=c(0,0), date_label="%H:%M", breaks=date_breaks("4 min")) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5)) +
  labs(x="Time", y="Uses Per Minute", title="Uses of the Word ___ in Reddit Thread: ____")
