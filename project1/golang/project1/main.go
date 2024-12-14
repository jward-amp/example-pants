package main

import (
	"fmt"
	"os"
)

func main() {
	name := "Pants Build"
	if len(os.Args) >= 2 {
		name = os.Args[1]
	}
	fmt.Printf("Hello, %s!\n", name)
}
