## 1. Introduction ##


df <- read.csv("scores.csv")
head(df)
str(df)

## 2. Concatenating Strings ##


add_2014 <- paste(df$match_date, "-2014")

## 3. Updating a Column in a Dataframe ##

paste(df$match_date, "-2014")
df$match_date <- paste(df$match_date, "-2014")
update_2014 <- df$match_date

## 4. Extracting a Substring ##


months <- substr(df$match_date,3,8)

## 5. Splitting a String ##


df$match_date <- as.character(df$match_date)
date_split <- strsplit(df$match_date, split=" ")
df$match_date

## 6. Replacing a Value in a String ##


df$match_date <- sub("June", "-06", df$match_date)
df$match_date <- sub("July", "-07", df$match_date)
updated_dates <- df$match_date

## 7. Removing the Whitespaces from our String ##


df$match_date <- gsub(" ", "", df$match_date)
remove_space <- df$match_date

## 8. Converting a String into a Date Format ##


df$match_date <- as.Date(df$match_date, format="%d-%m-%Y")
date_convert <- df$match_date

## 9. Extracting Parts of the Date ##


df$match_date <- as.POSIXlt(df$match_date)
pos_obj <- df$match_date

## 10. Extracting Values from our date column ##


dayofweek <- df$match_date$wday

## 11. Creating a new column in our dataframe ##

dayofweek <- df$match_date$wday
df$dayofweek <- df$match_date$wday
dayofweek <- df$dayofweek

## 12. Building your own news headline generator ##


df$month <- df$match_date$mon
df$month<- sub(5, "June",df$month)
df$month<- sub(6, "July",df$month)



df$headline <- paste("On",df$month, sub(" ","", paste(df$match_date$mday, "th,")), df$win_country, 
                     "won the match", gsub(" ", "", paste(df$home_goals, "-", df$away_goals)))
headline <- df$headline