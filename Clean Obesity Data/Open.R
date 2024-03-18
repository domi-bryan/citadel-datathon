getwd()
setwd("./Clean Obesity Data")

# Main CLEANED Dataset
obesity <- read.csv("obesity.csv")

# "Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily"
dailyActivityKids <- read.csv("dailyActivityKids.csv")

# "Percent of students in grades 9-12 who have obesity"
obRateKids <- read.csv("obRateKids.csv")

# "Percent of students in grades 9-12 who participate in daily physical education"
dailyPEKids <- read.csv("dailyPEKids.csv")

# "Percent of students in grades 9-12 who have an overweight classification"
owRateKids <- read.csv("owRateKids.csv")

# "Percent of students in grades 9-12 who drank regular soda/pop at least one time per day"
dailySodaKids <- read.csv("dailySodaKids.csv")

# "Percent of students in grades 9-12 who consume vegetables less than 1 time daily"
dailyVegKids <- read.csv("dailyVegKids.csv")

# "Percent of students in grades 9-12 who consume fruit less than 1 time daily"
dailyFruitKids <- read.csv("dailyFruitKids.csv")

# "Percent of students in grades 9-12 watching 3 or more hours of television each school day"
dailyTVKids <- read.csv("dailyTVKids.csv")

# "Percent of adults who engage in no leisure-time physical activity"
leisureAdults <- read.csv("leisureAdults.csv")

# "Percent of adults aged 18 years and older who have obesity"
obRateAdults <- read.csv("obRateAdults.csv")

# "Percent of adults aged 18 years and older who have an overweight classification"
owRateAdults <- read.csv("owRateAdults.csv")

# "Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)"
weeklyActivityIntenseAdults <- read.csv("weeklyActivityIntenseAdults.csv")

# "Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week"
weeklyActivityLongAdults <- read.csv("weeklyActivityLongAdults.csv")

# "Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)"                                                 
weeklyActivityAdults <- read.csv("weeklyActivityAdults.csv")

# "Percent of adults who engage in muscle-strengthening activities on 2 or more days a week"
weeklyWorkoutAdults <- read.csv("weeklyWorkoutAdults.csv")

# "Percent of adults who report consuming fruit less than one time daily"
dailyFruitAdults <- read.csv("dailyFruitAdults.csv")

# "Percent of adults who report consuming vegetables less than one time daily" 
dailyVegAdults <- read.csv("dailyVegAdults.csv")

