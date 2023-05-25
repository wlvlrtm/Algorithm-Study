package b2908;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        // 사용자 입력; 상수 2개
        String num_A = sc.next();
        String num_B = sc.next();

        // 상수 슬라이싱
        String[] list_A = num_A.split("");
        String[] list_B = num_B.split("");

        // 뒤집은 상수 2개 저장; string 타입
        String reverse_A = "";
        String reverse_B = "";


        // 상수 A reverse
        for (int i = list_A.length-1; i >= 0; i--) {
            reverse_A += list_A[i];
        }


        // 상수 B reverse
        for (int j = list_B.length-1; j >= 0; j--) {
            reverse_B += list_B[j];
        }


        // 크기 비교 후 결과 출력
        int result_A = Integer.parseInt(reverse_A);
        int result_B = Integer.parseInt(reverse_B);

        if (result_A > result_B) {
            System.out.print(result_A);
        }
        else {
            System.out.print(result_B);
        }


        sc.close();
    }
}