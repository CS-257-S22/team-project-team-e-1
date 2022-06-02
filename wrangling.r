library(tidyverse)
library(readr)

masterTitles <- read_csv("movie_database.csv")
masterTitles <- masterTitles %>%
  group_by(title) %>% 
  dplyr::mutate(streaming_service = ifelse(n()>1,paste(streaming_service, collapse = ", "),streaming_service))

write_csv(masterTitles, "movie_database2.csv")
