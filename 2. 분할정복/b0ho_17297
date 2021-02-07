import java.util.*;
import java.io.*;

public class Main {
    static int M;
    static int[] dp;
    static String answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        dp = new int[Integer.MAX_VALUE/4];
        dp[0] = 5;
        dp[1] = 13;
        answer = " ";

        if (M > 13) {
            int n = 1;
            while (dp[n++] < M) {
                if (dp[n - 2] + 1 + dp[n - 1] <= (int) Math.pow(2, 30) - 1) {
                    dp[n] = dp[n - 2] + 1 + dp[n - 1];
                }
            }
            answer = find(n - 1, M);
        } else {
            String str = "Messi Gimossi";
            answer = str.substring(M - 1, M);
        }

        if (answer == " ") {
            System.out.println("Messi Messi Gimossi");
        } else {
            System.out.println(answer);
        }
    }

    public static String find(int idx, int m) {
        if (idx <= 1) {
            String str = "Messi Gimossi";
            answer = str.substring(m - 1, m);
        } else if (m > dp[idx - 1] + 1) {
            find(idx - 2, m - dp[idx - 1] - 1);
        } else if (m < dp[idx - 1]) {
            find(idx - 1, m);
        }

        return answer;
    }

}
