package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	// Convert the int to string
	str := strconv.Itoa(x)

	// Reverse the string
	reversed := ""
	for i := len(str) - 1; i >= 0; i-- {
		reversed += string(str[i])
	}

	// Compare the reversed string with the original
	return reversed == str
}

func main() {
	// Test Cases
	fmt.Println(isPalindrome(121))  // true
	fmt.Println(isPalindrome(-121)) // false
	fmt.Println(isPalindrome(10))   // false
}
