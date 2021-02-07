import java.util.*;
import java.io.*;

public class Main {
    static int L;
    static int W;
    static int H;
    static int N;
    static int[][] arr;
    static boolean flag;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        arr = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = (int) Math.pow(2, Integer.parseInt(st.nextToken()));
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o2[0] - o1[0];
            }
        });

        divide(L, W, H, 0);

        if (flag) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }

    public static void divide(int l, int w, int h, int idx) {
        if (l == 0 || w == 0 || h == 0) {
            return;
        }
        for (int i = idx; i < arr.length; i++) {
            if (arr[i][1] != 0 && l >= arr[i][0] && w >= arr[i][0] && h >= arr[i][0]) {
                arr[i][1]--;
                answer++;
                divide(l - arr[i][0], w, h, i);
                divide(arr[i][0], w - arr[i][0], h, i);
                divide(arr[i][0], arr[i][0], h - arr[i][0], i);
                return;
            }
        }

        flag = true;

    }

}
