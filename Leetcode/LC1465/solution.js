/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
  let arr = [];
  for (let tn = 0; tn < h; ++tn) {
    for (let tm = 0; tm < w; ++tm) {
      arr.push({ x: [tm, tm + 1], y: [tn, tn + 1] });
    }
  }
  let maxarea = 0;
  for (let i = 0; i < horizontalCuts.length; ++i) {
    let th = horizontalCuts[i];
    let tv = verticalCuts[i];
    for (let block of arr) {
      if (block["x"][0] === th) block["x"][0] -= 1;
      if (block["x"][1] === th) block["x"][1] += 1;
      if (block["y"][0] === tv) block["y"][0] -= 1;
      if (block["y"][1] === tv) block["y"][1] += 1;
      let hor = block["x"][1] - block["x"][0];
      let ver = block["y"][1] - block["y"][0];
      let tmparea = hor * ver;
      if (tmparea > maxarea) maxarea = tmparea;
    }
  }
  return maxarea;
};

/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
var maxArea = function(h, w, horizontalCuts, verticalCuts) {
  let arrx = [];
  let arry = [];
  for (let i = 0; i < h; ++i) {
    arrx[i] = 1;
  }
  for (let i = 0; i < w; ++i) {
    arry[i] = 1;
  }
  let maxx = 0,
    maxy = 0,
    tmpx = 0,
    tmpy = 0;
  for (let th = 0; th < horizontalCuts.length; ++th) arrx[horizontalCuts[th]] = 0;
  for (let tv = 0; tv < verticalCuts.length; ++tv) arry[verticalCuts[tv]] = 0;
  for (let i = 0; i < arrx.length; ++i) {
    if (arrx[i]) tmpx = 0;
    else {
      ++tmpx;
      maxx = tmpx > maxx ? tmpx : maxx;
    }
  }
  for (let i = 0; i < arry.length; ++i) {
    if (arry[i]) tmpy = 0;
    else {
      ++tmpy;
      maxy = tmpy > maxy ? tmpy : maxy;
    }
  }
  return (maxx + 1) * (maxy + 1);
};