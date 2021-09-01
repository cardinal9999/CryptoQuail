function encode(string) {
    var number = "0x";
    var length = string.length;
    for (var i = 0; i < length; i++)
        number += string.charCodeAt(i).toString(16);
    return number;
}
export function crypt(input, key) {
    var key = key.split('');
    var output = [];
    int1 = encode(key);
    for (var i = 0; i < input.length; i++) {
        var charCode = input.charCodeAt(i) ^ (key[i % key.length] ^ int1).charCodeAt(0);
        output.push(String.fromCharCode(charCode));
        }
    return output.join("");
}

