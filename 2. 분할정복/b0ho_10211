import java.util.*;
import java.io.*;

public class Main {
    static int T;
    static int N;
    static int[] arr;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        while (T-- > 0) {
            answer = 0;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            arr = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            answer = find(0, N - 1);

            System.out.println(answer);
        }

    }

    public static int find(int left, int right) {
        if (left == right) {
            return arr[right];
        }

        int mid = (left + right) / 2;
        int left_sum = find(left, mid);
        int right_sum = find(mid + 1, right);
        int merge = merge(left, mid, right);

        return Math.max(Math.max(left_sum, right_sum), merge);
    }

    public static int merge(int left, int mid, int right) {
        int left_sum = Integer.MIN_VALUE;
        int right_sum = Integer.MIN_VALUE;

        for (int i = mid, tmp = 0; i >= left; i--) {
            tmp += arr[i];
            left_sum = Math.max(left_sum, tmp);
        }

        for (int i = mid + 1, tmp = 0; i <= right; i++) {
            tmp += arr[i];
            right_sum = Math.max(right_sum, tmp);
        }

        return left_sum + right_sum;
    }

}
