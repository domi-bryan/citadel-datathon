import pandas as pd
import os

print(os.getcwd())
PATH = '../citadel-datathon/Clean Obesity Data/'
os.chdir(PATH)

# Main CLEANED Dataset
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