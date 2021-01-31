import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] op;
    static long Min;
    static long Max;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        op = new int[4];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            op[i] = Integer.parseInt(st.nextToken());
        }

        Max = Integer.MIN_VALUE;
        Min = Integer.MAX_VALUE;

        rec(arr[0], 1);

        System.out.println(Max);
        System.out.println(Min);

    }

    public static void rec(long tmp, int idx) {

        if (idx == N) {
            if (tmp < Min) {
                Min = tmp;
            }
            if (tmp > Max) {
                Max = tmp;
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (op[i] > 0) {
                op[i]--;
                if (i == 0) {
                    rec(tmp + arr[idx], idx + 1);
                }
                if (i == 1) {
                    rec(tmp - arr[idx], idx + 1);
                }
                if (i == 2) {
                    rec(tmp * arr[idx], idx + 1);
                }
                if (i == 3) {
                    rec(tmp / arr[idx], idx + 1);
                }

                op[i]++;
            }
        }

    }

}
