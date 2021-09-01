var cryptoObj;
cryptoObj = window.crypto || window.msCrypto;


export function randbelow(max) {
    array = new Uint16Array(4);
    cryptoObj.getRandomValues(array);
    eeeeee = array[0] * array[1] * array[2];
    return eeeeee % max;
    }

export function randint(min, max) {
  x = max - min;
  distance = randbelow(x);
  return max - distance;
}

export function choice(group) {
  return group[randbelow(group.length)];
}

export function alphanumeric(length) {
  var str = "";
  for(var i = 0; i < length; ++i){
    chars = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP1234567890";
    str += choice(chars);
  }
  return str;
}
