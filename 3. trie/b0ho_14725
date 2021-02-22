import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static String[][] S;
    static Trie root;
    static StringBuilder answer;

    public static void main(String[] args) throws IOException {
        answer = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        root = new Trie();
        S = new String[N][];

        //입력값을 저장
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());
            S[i] = new String[K];

            for (int j = 0; j < K; j++) {
                S[i][j] = st.nextToken();
            }
        }

        // 케이스마다 trie 에 입력한다
        for (int i = 0; i < N; i++) {
            insert(S[i]);
        }

        print(root, 0);
        System.out.print(answer);
    }

    // 삽입시 기본적으로는 기존 trie 와 동일하지만
    // 알파벳 단위가 아니라 단어 단위로 넣는다
    // 층별로 단어가 오므로 어쩔수없다
    // 즉 인덱스가 아닌 단어(key)로 다음 위치를 찾는다
    public static void insert(String[] words) {
        //시작이 root 임은 동일
        Trie Node = root;

        //알파벳 길이만큼이 아니라 단어 개수 만큼 반복
        for (String word : words) {
            //단어(key)가 해당 노드의 트리맵에 없으면 trie 를 생성한다
            if (!Node.node.containsKey(word)) {
                //생성은 곧 트리맵에 추가하는 것
                Node.node.put(word, new Trie());
            }

            //다음으로 이동한다
            Node = Node.node.get(word);
        }

        //모든 입력을 출력하는 문제이므로 끝 확인이 필요없다
    }

    //출력을 위한 함수
    //재귀하여 모두 sb에 담는다
    public static void print(Trie now, int idx) {
        for (String key : now.node.keySet()) {
            //idx 만큼 '--' 출력
            answer.append("--".repeat(idx));
            //단어:문자열 출력
            answer.append(key).append("\n");
            //다음 위치를 찾고
            Trie next = now.node.get(key);
            //재귀한다:1층의 첫번째부터 깊이우선 탐색해야하기 때문에
            print(next, idx + 1);
        }
    }

    public static class Trie {
        //트리맵은 key 값(word:string) 에 따라 정렬된다
        //추가적인 정렬 없이 알파벳 순서로 정렬됨
        TreeMap<String, Trie> node;

        public Trie() {
            //각 노드마다 트리맵을 생성한다
            //즉 이번문제에서 Trie 는 26개짜리 배열이 아닌
            // 단어와 다음 Trie 를 갖는 트리맵이다
            node = new TreeMap<>();
        }
    }
}
