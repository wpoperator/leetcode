// Leetcode 2529: Maximum Count of Positive Integer and Negative Integer

var maximumCount = function(nums) {
    // counter for positive numbers
    let pos = 0;
    //counter for negative numbers
    let neg = 0;

    // loop through nums
    for (n of nums) {
        // skip any zeroes
        if (n == 0) {
            continue;
        }
        // check if current value of n is greater than zero
        else if (n > 0) {
            // increment pos everytime n is greater
            pos++;
        }
        else {
            // increment everytime n is less
            neg++;
        }
    }
    // Return the maximum number between pos, neg
    return Math.max(pos, neg)
};
