import pandas as pd
import os

# ===== OBESITY DATA =====
os.chdir('../citadel-datathon/Clean Obesity Data/')

# Main Cleaned Dataset
obesity = pd.read_csv("obesity.csv")

# "Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily"
dailyActivityKids = pd.read_csv("dailyActivityKids.csv")

# "Percent of students in grades 9-12 who have obesity"
obRateKids = pd.read_csv("obRateKids.csv")

# "Percent of students in grades 9-12 who participate in daily physical education"
dailyPEKids = pd.read_csv("dailyPEKids.csv")

# "Percent of students in grades 9-12 who have an overweight classification"
owRateKids = pd.read_csv("owRateKids.csv")

# "Percent of students in grades 9-12 who drank regular soda/pop at least one time per day"
dailySodaKids = pd.read_csv("dailySodaKids.csv")

# "Percent of students in grades 9-12 who consume vegetables less than 1 time daily"
dailyVegKids = pd.read_csv("dailyVegKids.csv")

# "Percent of students in grades 9-12 who consume fruit less than 1 time daily"
dailyFruitKids = pd.read_csv("dailyFruitKids.csv")

# "Percent of students in grades 9-12 watching 3 or more hours of television each school day"
dailyTVKids = pd.read_csv("dailyTVKids.csv")

# "Percent of adults who engage in no leisure-time physical activity"
leisureAdults = pd.read_csv("leisureAdults.csv")

# "Percent of adults aged 18 years and older who have obesity"
obRateAdults = pd.read_csv("obRateAdults.csv")

# "Percent of adults aged 18 years and older who have an overweight classification"
owRateAdults = pd.read_csv("owRateAdults.csv")

# "Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)"
weeklyActivityIntenseAdults = pd.read_csv("weeklyActivityIntenseAdults.csv")

# "Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week"
weeklyActivityLongAdults = pd.read_csv("weeklyActivityLongAdults.csv")

# "Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)"                                                 
weeklyActivityAdults = pd.read_csv("weeklyActivityAdults.csv")

# "Percent of adults who engage in muscle-strengthening activities on 2 or more days a week"
weeklyWorkoutAdults = pd.read_csv("weeklyWorkoutAdults.csv")

# "Percent of adults who report consuming fruit less than one time daily"
dailyFruitAdults = pd.read_csv("dailyFruitAdults.csv")

# "Percent of adults who report consuming vegetables less than one time daily" 
dailyVegAdults = pd.read_csv("dailyVegAdults.csv")

# ===== MEAT AND LIVESTOCK DATA =====
os.chdir('../citadel-datathon/Clean Meat Consumption Data/')

# Red Meat and Poultry Production
meatProduction = pd.read_csv("meatProduction.csv")

# Slaughter Count
slaughterCount = pd.read_csv("slaughterCount.csv")

# Slaughter Weights (Live Weights: The weight of livestock or poultry at the time of slaughter before any processing. Dressed Weights: The weight of the carcass after slaughter and removal of inedible parts (such as head, hide, and organs).)
slaughterWeight = pd.read_csv("slaughterWeight.csv")

# Cold Storage
coldStorage = pd.read_csv("coldStorage.csv")

# ===== STOCK MARKET DATA =====
os.chdir('../citadel-datathon/Clean Stock and Commodities Data/')

# Stocks & ETFs
stocks = pd.read_csv("stocks.csv")

# Commodities
commodities = pd.read_csv("commodities.csv")

# Descriptions
description = pd.read_csv("description.csv")

# ===== AMERICAN COMMUNITY SURVEY DATA =====
os.chdir('../citadel-datathon/Clean ACS Data/')

# Main Cleaned Dataset
acs = pd.read_csv("acs.csv")

# Different Classes/Types of Workers
classOfWorker = pd.read_csv("classOfWorker.csv")

# Method of Transportation to Work
commutingToWork = pd.read_csv("commutingToWork.csv")

# Employment Status
employmentStatus = pd.read_csv("employmentStatus.csv")

# Percentage Of Families And People Whose Income In The Past 12 Months Is Below The Poverty Level
familyPovertyRate = pd.read_csv("familyPovertyRate.csv")

# Level of Health Insurance Coverage
healthInsuranceCoverage = pd.read_csv("healthInsuranceCoverage.csv")

# Industry of Employment
industry = pd.read_csv("industry.csv")

# Occupation
occupation = pd.read_csv("occupation.csv")

# Year on Year Nominal Income in Various Categories
nominalIncome = pd.read_csv("nominalIncome.csv")