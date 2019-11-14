# HW

1. Create car:

    * Use input for get:
        * Brand
        * Model
        * Color
        * Year
        * Engine volume
        * Odometer
        * Phone number
    * Create rating value for car and increase or decrease at each step 
    * Check that brand (model, color) not in your favourite, print brand name, 
    and in finally clause print your favourite.
    * Try to change year type to int and catch exception, else print year 
    and finally decrease year by 1 and print
    * Change Engine volume type to float and add 0.1 to value 
    (print to user), (use try, except, else)
    * Change odometer type to int check that odometer value less than 1000, 
    greater than 50000, greater or equal to 100000 and 
    set different value for rating
    * Get final rating for your car by your criterion (3-4 if cases)

2. 
    * Input: credit card number (fake data), cvv, mm/yy
    * Check that credit card number length has 16 symbols in other case call exit()
    * Try to make credit card number to int() if error output "OK", in other case call exit()
    * Check length of cvv if less than 3 symbols, print error and call exit()
    * If all checks passed print "Everything fine"