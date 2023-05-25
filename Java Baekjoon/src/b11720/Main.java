package b11720;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int c;
        String num;


        // 숫자의 개수 입력
        c = sc.nextInt();

        // 숫자 입력
        num = sc.next();


        // 자리 수 더하기
        int t = 0;

        for(int i = 0; i < c; i++) {
            t += num.charAt(i) - '0';
        }

        // 결과 출력
        System.out.println(t);


        sc.close();
    }
}
