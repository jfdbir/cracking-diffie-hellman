package main

import (
	"fmt"
	"math/rand/v2"
)

func main() {

	// Alice and Bob choose SA and SB respectively (secret, never transmitted)
	var SA int = rand.IntN(10000)
	var SB int = rand.IntN(10000)

	fmt.Println(SA, SB)
}
