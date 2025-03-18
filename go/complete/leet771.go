package main

import "fmt"

func numJewelsInStones(jewels string, stones string) int {
	// create response variable
	res := 0

	// create a map for faster jewel lookup
	jewelMap := make(map[rune]bool)
	for _, j := range jewels {
		jewelMap[j] = true
	}

	// loop through each character of stones
	for _, s := range stones {
		// check if current character is a jewel
		if jewelMap[s] {
			// increment res by one each time if condition passes
			res++
		}
	}

	// return the res variable value
	return res
}

//Test Cases
func main() {
	fmt.Println(numJewelsInStones("aA", "aAAbbbb")) // 3
	fmt.Println(numJewelsInStones("z", "ZZ"))       // 0
}
