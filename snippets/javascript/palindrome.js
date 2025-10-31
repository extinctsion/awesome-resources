//A palindrome is a word, phrase, number, or sequence that reads the same backward as forward
//Example: "madam", "racecar", "A man, a plan, a canal, Panama"
//This code checks if the given string is plindrome or not 

function isPalindrome(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return str === reversed;
}

console.log(isPalindrome("madam")); // true
console.log(isPalindrome("hello")); // false