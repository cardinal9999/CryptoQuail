function charCodeAt(input){
  var keys = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#%&()*^$@`~-_=][+{\ }|</>,.;:'\"" ;
  var values = [];
  for (var k = 0; k < keys.length; k++){
    values.push(k);
  }
  for (var i = 0; i < keys.length; i++){
    if (keys[i] === input){return values[i]}
  }
}
function encode(string) {
    var number = "0x";
    var length = string.length;
    for (var i = 0; i < length; i++)
        number += charCodeAt(string[i]).toString(16);
    return number;
}
export function crypt(input, key) {
    var key = key.split('');
    var output = [];
    int1 = encode(key);
    for (var i = 0; i < input.length; i++) {
        var charCode = charCodeAt(charCodeAt(input[i]) ^ (key[i % key.length] ^ int1)[0]);
        output.push(String.fromCharCode(charCode));
        }
    return output.join("");
}

