class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j= b.length() - 1;
        int carry=0;
        StringBuilder sb = new StringBuilder();
        while (i>=0||j>=0){
            int sum = carry;
            sum=sum+(i>=0?a.charAt(i)-'0':0);
            sum=sum+(j>=0?b.charAt(j)-'0':0);
            sb.append(sum%2);
            if (i>=0) i--;
            if (j>=0) j--;
            carry=sum/2;
        }
        if carry==1{
            sb.append(1);
        }
        return sb.reverse().toString();
    }
}