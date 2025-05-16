// Leetcode 1550: Three Consecutive Odds

var maximumCount = function(nums) {
    // counter
    let counter = 0;
    // loop
    for (n of nums) {
        if (n % 2 === 0) {
            counter = 0
        }
        if (counter == 3) {
            return true
        }
    }
};
