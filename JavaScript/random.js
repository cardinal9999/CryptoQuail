var cryptoObj;
cryptoObj = window.crypto || window.msCrypto;

var randbelow;
randbelow = function(max) {
    array = new Uint16Array(4);
    cryptoObj.getRandomValues(array);
    eeeeee = array[0] * array[1] * array[2];
    return eeeeee % max;
    }
var randint;
randint = function(min, max) {
  x = max - min;
  distance = randbelow(x);
  return max - distance;
}
var choice;
choice = function(group) {
  return group[randbelow(group.length)];
}
var token_alphanumeric;
token_alphanumeric = function(length) {
  var str = "";
  for(var i = 0; i < length; ++i){
    chars = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP1234567890";
    str += choice(chars);
  }
  return str;
}
