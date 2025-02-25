function numJewelsInStones(jewels, stones) {
    // create response variable
    let res = 0;
    // loop through each character of stones
    for (let s of stones) {
        // check if current character is included in jewels
        if (jewels.includes(s))
            // increment res by one each time if condition passes
            res++;
    }
    // return the res variable value
    return res;
}
