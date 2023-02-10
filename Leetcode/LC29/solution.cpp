class Solution {
public:
    int divide(int dividend, int divisor) {
        int negative=(dividend<0) ^ (divisor<0);
        long dive = abs((long)dividend);
        long divs = abs((long)divisor);
        long result=0;
        long total;
        long factor;
        while(dive>=divs){
            total=divs;
            factor=1;
            while(dive>=(total<<1)){
                total<<=1;
                factor<<=1;
            }
            result+=factor;
            dive-=total;
        }
        if(negative)
            result=-result;
        if(result>INT_MAX)
            result=INT_MAX;
        else if(result<INT_MIN)
            result=INT_MIN;
        return (int)result;
    }
};