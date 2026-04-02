class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    for (let i=0;i<nums.length;i++){
    let k=nums[i]
    let j=i+1
    for(j;j<nums.length;j++){
     let m=nums[j]
     if(k==m){
    return true
}}}
    
    return false}
}
