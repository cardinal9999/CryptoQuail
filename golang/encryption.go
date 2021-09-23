package cryptoquail
// UNFINISHED!
import (
	"encoding/hex"
	"fmt"
	"math/big"
)
func crypt(input, key string) (output string) {
	L := len(key)
	u1 := hex.EncodeToString([]byte(key)) 
	u := new(big.Int)
	u.SetString(u1, 16)
	for i := range input {
		output += string(input[i] ^ key[i%L] ^ (u.Int64() % 100)) // Fix this: convert the bytes (key [i%l]) to integer
	}
	return output
}
