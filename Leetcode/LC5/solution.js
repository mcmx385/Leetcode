/**
 * @param {string} s
 * @return {string}
 */
var longestNearby = function (s, left, right) {
    if (s.length === 1) return 1
    let len = 0
    while (left >= 0 && right <= s.length) {
        // console.log(s.substring(left,left+1),s.substring(right,right+1))
        if (s.substring(left, left + 1) === s.substring(right, right + 1)) {
            --left
            ++right
        } else {
            break
        }
    }
    return right - left - 1
}
var longestPalindrome = function (s) {
    let most = 0
    let left = 0
    let right = 0
    for (let i = 0; i < s.length; ++i) {
        let result1 = longestNearby(s, i - 1, i + 1)
        let result2 = longestNearby(s, i, i + 1)
        let result = Math.max(result1, result2)
        // console.log(result1,result2,result)
        if (result > most) {
            most = result
            left = i - Math.floor((result - 1) / 2)
            right = i + Math.floor(result / 2)
        }
    }
    return s.substring(left, right + 1)
};