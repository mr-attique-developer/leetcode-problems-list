/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let n = nums.length
    k = k % n;
    temp = new Array(n)
  for(let i = 0; i< n; i++){
    temp[(i+k)% n] = nums[i]
  } 
  for(let i = 0; i< n; i++){
    nums[i] = temp[i]
  } 
};

