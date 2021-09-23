package cryptoquail
func crypt(input, key string) (output string) {
	L := len(key)
	for i := range input {
		output += string(input[i] ^ key[i%L])
	}
	return output
}