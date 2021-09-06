public class Lv3KeyLock {

    // 회전 후 모든 홈이 맞는지 비교
    // 400 * 400 * 4 + @ 의 시간 복잡도로 추정
    // 벗어나는 범위를 처리하기 위해 배열의 크기를 증폭시킬 필요가 있어보임 3배
    // 돌기끼리 만나면 안되기 때문에 모든상황을 테스트 해야함.

    public boolean solution(int[][] key, int[][] lock) {
        int[][] scaleUpKey = scaleUp(key, lock.length - 1);
        if (match(scaleUpKey, lock)) {
            return true;
        }
        for (int i = 0; i < 3; i++) {
            key = rotation(key);
            scaleUpKey = scaleUp(key, lock.length - 1);
            if (match(scaleUpKey, lock)) {
                return true;
            }
        }
        return false;
    }

    private int[][] rotation(int[][] key) {
        int N = key.length;
        int[][] newKey = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                newKey[i][j] = key[j][Math.abs(i - (N - 1))];
            }
        }
        return newKey;
    }

    private boolean match(int[][] key, int[][] lock) {
        for (int i = 0; i <= key.length - lock.length; i++) {
            for (int j = 0; j <= key.length - lock.length; j++) {
                if (keyLockMatch(key, lock, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean keyLockMatch(int[][] key, int[][] lock, int i, int j) {
        for (int y = 0; y < lock.length; y++) {
            for (int x = 0; x < lock.length; x++) {
                if (key[i + y][j + x] == lock[y][x]) {
                    return false;
                }
            }
        }
        return true;
    }

    private int[][] scaleUp(int[][] key, int n) {
        int m = key.length;
        int[][] newKey = new int[m + n * 2][m + n * 2];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                newKey[n + i][n + j] = key[i][j];
            }
        }
        return newKey;
    }
}
