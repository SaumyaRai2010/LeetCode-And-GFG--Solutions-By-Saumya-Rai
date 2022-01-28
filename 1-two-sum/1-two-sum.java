// import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] nums2 = Arrays.copyOf(nums, nums.length);
        Arrays.sort(nums2);
        int res[]=new int[2];
        int i=0;
        int j=nums.length-1;
        int a=0;
        int b=0;
        while (i<j){
            int sum=nums2[i]+nums2[j];
            if(sum < target)
	    			i++;
	    		else if(sum > target)
	    			j--;
	    		else{
	    			a = nums2[i]; 
                    b = nums2[j];
	    			break;
        }
        
    }
        for (i=0;i<nums.length;i++){
            if (nums[i]==a){
                res[0]=i;
                break;
            }
        }
        if (a!=b){
            for( i = 0; i < nums.length; i++)
            {
		    		if(nums[i] == b){
		    			res[1] = i;
		    			break;
        }}}
        else
        {
            for( i=0;i<nums.length;i++)
            {
                if (nums[i]==b && i!=res[0])
                {
                    res[1]=i;
                    break;
                }
            }
        }
        return res;
}}