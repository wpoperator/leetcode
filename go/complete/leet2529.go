package main

import (
	"fmt"
	"math"
)

func maximumCount(nums []int) int {
	// counter for positive numbers
	pos := 0
	// counter for negative numbers
	neg := 0

	// loop through nums
	for _, n := range nums {
		// skip any zeroes
		if n == 0 {
			continue
		} else if n > 0 {
			// increment pos everytime n is greater
			pos++
		} else {
			// increment everytime n is less
			neg++
		}
	}

	// Return the maximum number between pos, neg
	return int(math.Max(float64(pos), float64(neg)))
}

func main() {
	// Test cases
	fmt.Println(maximumCount([]int{-2, -1, -1, 1, 2, 3}))    // 3
	fmt.Println(maximumCount([]int{-3, -2, -1, 0, 0, 1, 2})) // 3
	fmt.Println(maximumCount([]int{5, 20, 66, 1314}))        // 4
}
