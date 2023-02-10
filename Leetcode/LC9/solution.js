/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    if (x < 0) return false
    let length = x.toString().length
    while (x > 0) {
        let frontLen = Math.pow(10, length - 1)
        let frontRem = Math.floor(x / frontLen)
        if (x % 10 !== frontRem) {
            return false
        }
        x -= frontRem * frontLen
        x = Math.floor(x / 10)
        length -= 2
    }
    return true
};