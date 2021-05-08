package b1065;

import java.util.Scanner;

public class main_1065 {
    public static void main(String[] args) {
        int num;    // 사용자 입력 수
        int[] nums = new int[3]; // 자리 수 배열
        int k;  // 자리 수 배열 인덱스 카운트

        int han = 0;    // 한수 카운트

        Scanner sc = new Scanner(System.in);

        // 사용자 수 입력
        num = sc.nextInt();

        for(int i = 1; i <= num; i++) {
            // 두자리 수 한수
            if (i < 100) {
                han = i;
            }
            else if (i == 1000) {
                break;
            }
            else {
                k = 0;
                int t = i;  // 현재 i 값 복사 (Line 33)
                // 세자리 수 한수
                while(t != 0) {
                    nums[k] = (t % 10);
                    t = (t / 10);   // !! i = (i/10); -> for() i 값이 바뀜
                    k += 1;
                }

                // 한수 검사; 세자리 수
                if(nums[0] - nums[1] == nums[1] - nums[2]) {
                    han += 1;
                }
            }
        }
        System.out.println(han);
    }
}
