package b2675;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String P;   // 새로 제작할 문자열 P
        String S;   // 문자열 S
        int T;      // 테스트 케이스의 개수
        int R;      // 테스트 케이스 반복 횟수

        T = sc.nextInt();  // Ex) 2

        for(int k = 0; k < T; k++) {
            P = "";                 // 문자열 P 초기화
            R = sc.nextInt();  // Ex) 3
            S = sc.next();     // Ex) ABC

            // 각 문자를 R번 반복해 문자열 P 생성
            for(int i = 0; i < S.length(); i++) {
                for(int j = 0; j < R; j++) {
                    P += S.substring(i, i+1);
                }
            }
            System.out.println(P);  // 결과 출력
        }



        sc.close();
    }
}
