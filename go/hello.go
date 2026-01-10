package main

import "fmt"

func main() {
	// Print Hello World to the console
	fmt.Println("Hello World")
	/*Variables*/
	var name string = "Deepak"
	var age = 10
	fmt.Println(name)
	fmt.Println(age)
	x := true
	fmt.Println(x)
	/* Multi line variable declaration*/
	// var a, b, c int = 1, 2, 3
	// fmt.Println(a, b, c)
	// var a, myName = 1, "Deepak"
	// var b, isAdult = 18, true
	// fmt.Println(b, isAdult)
	// fmt.Println(a, myName)

	/* Block scope variable declaration*/
	var (
		city        string = "New York"
		country     string = "USA"
		countryCode int    = 1
	)
	fmt.Println(city)
	fmt.Println(country)
	fmt.Println(countryCode)
	//Constants Typeed UnTyped
	//Output Funcitons
	//Formatting Go Verbs
	//Basics Data Types
	//Integers 
	   //Signed
	   	//int int8 int16 int32 int64
	   //Unsigned
	   	//uint uint8 uint16 uint32 uint64 uintptr
	//Float
	//Bool
	//String
	

}
