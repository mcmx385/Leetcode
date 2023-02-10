/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    if (!x) return 0
    if (!x % 10) x /= 10
    let tmpX = x
    let length = tmpX.toString().length
    let neg = x < 0
    if (neg) {
        tmpX = -tmpX
        --length
    }
    let res = 0;
    for (let i = 0; i < length; ++i) {
        let pos = Math.pow(10, length - i - 1)
        let rem = Math.floor(tmpX / pos)
        res += rem * Math.pow(10, i)
        tmpX -= rem * pos
    }
    if (neg) res = -res
    let bound = Math.pow(2, 31)
    if (res >= bound || res < -bound) return 0
    return res
};

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    let neg = x < 0
    if (neg) x = -x
    let res = 0;
    while (x > 0) {
        let rem = x % 10
        x = Math.floor(x / 10)
        res = rem + res * 10
    }
    if (res >= Math.pow(2, 31) || res < -Math.pow(2, 31)) return 0
    if (neg) res = -res
    return res
};