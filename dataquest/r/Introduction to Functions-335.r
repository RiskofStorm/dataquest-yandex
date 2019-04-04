## 1. Introduction to Functions ##

# Goals scored for entire season 
thunderbirds <- c(4,3,5,1,0,2,4,3,2,2,1,4)
flamethrowers <- c(2,4,6,0,3,4,2,3,3,2,1,0)
thunderbirds_mean <- mean(thunderbirds)
flamethrowers_mean <- mean(flamethrowers)

## 2. Understanding the Components of a Function ##

thunderbirds <- 3
flamethrowers <- 1
get_sum <- function(x,y){
    x + y
}

total_goals <- get_sum(thunderbirds, flamethrowers)

## 3. Function Scoping ##

get_sum <- function(x,y){
    x + y
}


## 4. Functions Inside of Functions ##

thunderbirds <- c(4,3,5,1,0,2,4,3,2,2,1,4)
flamethrowers <- c(2,4,6,0,3,4,2,3,3,2,1,0)
get_mean <- function(x){
    sum(x)/length(x)
}

thunderbirds_mean <- get_mean(thunderbirds)
flamethrowers_mean <- get_mean(flamethrowers)

## 5. Writing Your Own Function ##

thunderbirds <- c(4,3,5,1,0,2,4,3,2,2,1,4)
flamethrowers <- c(2,4,6,0,3,4,2,3,3,2,1,0)
get_predictions <- function(x, y){
    x_mean <- mean(x)
    y_mean <- mean(y)
    predictions <- c(x_mean, y_mean)
    return(predictions)
}

predicted_score <- get_predictions(thunderbirds,flamethrowers)

## 6. Adding Control Structures to our Function ##

thunderbirds <- c(4,3,5,1,0,2,4,3,2,2,1,4)
flamethrowers <- c(2,4,6,0,3,4,2,3,3,2,1,0)
predict_winner <- function(x, x_name, y, y_name){
    x_mean <- mean(x)
    y_mean <- mean(y)
    
    if (x_mean > y_mean){
        return(x_name)
    } else {
        return (y_name)
    }
}

winner <- predict_winner(thunderbirds, "thunderbirds", flamethrowers, "flamethrowers")