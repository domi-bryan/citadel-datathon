# ===== OBESITY DATA =====
setwd("./Clean Obesity Data")

# Main Cleaned Dataset
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

# ===== MEAT AND LIVESTOCK DATA =====
setwd("./Clean Meat Consumption Data")

# Red Meat and Poultry Production
meatProduction <- read.csv("meatProduction.csv")

# Slaughter Count
slaughterCount <- read.csv("slaughterCount.csv")

# Slaughter Weights (Live Weights: The weight of livestock or poultry at the time of slaughter before any processing. Dressed Weights: The weight of the carcass after slaughter and removal of inedible parts (such as head, hide, and organs).)
slaughterWeight <- read.csv("slaughterWeight.csv")

# Cold Storage
coldStorage <- read.csv("coldStorage.csv")

# ===== STOCK MARKET DATA =====
setwd("./Clean Stock and Commodities Data")

# Stocks & ETFs
stocks <- read.csv("stocks.csv")

# Commodities
commodities <- read.csv("commodities.csv")

# Descriptions
description <- read.csv("description.csv")

# ===== AMERICAN COMMUNITY SURVEY DATA =====
setwd("./Clean ACS Data")

# Main Cleaned Dataset
acs <- read.csv("acs.csv")

# Different Classes/Types of Workers
classOfWorker <- read.csv("classOfWorker.csv")

# Method of Transportation to Work
commutingToWork <- read.csv("commutingToWork.csv")

# Employment Status
employmentStatus <- read.csv("employmentStatus.csv")

# Percentage Of Families And People Whose Income In The Past 12 Months Is Below The Poverty Level
familyPovertyRate <- read.csv("familyPovertyRate.csv")

# Level of Health Insurance Coverage
healthInsuranceCoverage <- read.csv("healthInsuranceCoverage.csv")

# Industry of Employment
industry <- read.csv("industry.csv")

# Occupation
occupation <- read.csv("occupation.csv")

# Year on Year Nominal Income in Various Categories
nominalIncome <- read.csv("nominalIncome.csv")