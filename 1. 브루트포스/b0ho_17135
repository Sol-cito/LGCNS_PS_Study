import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int D;
    static int[][] arr;
    static int[][] map;
    static ArrayList<Integer> archer;
    static boolean[][] visit;
    static int dist;
    static int mx;
    static int my;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        map = new int[N][M];
        archer = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        comb(0, 3);

        System.out.println(answer);

    }

    // 3 궁수의 조합을 구한다.
    public static void comb(int start, int r) {
        if (r == 0) {
            attack();
            return;
        }

        for (int i = start; i < M; i++) {
            archer.add(i);
            comb(i + 1, r - 1);
            archer.remove(archer.size() - 1);
        }
    }

    // 궁수가 공격하고 적을 제거한다.
    public static void attack() {
        init();
        int sum = 0;

        for (int i = 0; i < N; i++) {
            visit = new boolean[N][M];
            for (Integer arc : archer) {
                mx = Integer.MAX_VALUE;
                my = Integer.MAX_VALUE;
                dist = Integer.MAX_VALUE;

                choice(arc);

                if (dist <= D) {
                    visit[mx][my] = true;
                }
            }

            sum = check(sum);
            move();

        }

        answer = Math.max(answer, sum);
    }

    // 맵 초기화
    public static void init() {
        for (int i = 0; i < N; i++) {
            if (M >= 0) System.arraycopy(arr[i], 0, map[i], 0, M);
        }
    }

    // 공격할 적을 선택한다. 바로 죽이지는 않고,
    public static void choice(int pos) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1) {
                    if (dist > getDist(i, j, N, pos)) {
                        dist = getDist(i, j, N, pos);
                        mx = i;
                        my = j;
                    } else if (dist == getDist(i, j, N, pos) && my > j) {
                        mx = i;
                        my = j;
                    }
                }
            }
        }
    }

    // 거리 구하는 공식을 적용한다.
    public static int getDist(int r1, int c1, int r2, int c2) {
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    }

    // 적을 죽이고, 점수를 계산한다.
    public static int check(int sum) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visit[i][j]) {
                    sum++;
                    map[i][j] = 0;
                }
            }
        }
        return sum;
    }

    // 남은 적들이 한칸씩 내려온다
    public static void move() {
        for (int i = N - 1; i > 0; i--) {
            if (M >= 0) System.arraycopy(map[i - 1], 0, map[i], 0, M);
        }
        for (int i = 0; i < M; i++) {
            map[0][i] = 0;
        }
    }

}
