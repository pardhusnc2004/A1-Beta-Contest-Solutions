class Solution {
    public:
        bool checkPerfectNumber(int num) {
            if(num == 1) return 0;
            int n = 1;
            for(int i=2; i<num/2+1; i++) {
                if(num%i == 0) n+=i;
            }
            return n==num;
        }
};