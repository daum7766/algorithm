class Solution {
    public long solution(int w, int h) {
        long x = w;
        long y = h;
        return  (x * y) - (x + y - gcd(x, y));
    }
    
    private long gcd(long a, long b) {
        while (b != 0) {
            long r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
