package b2577;

import java.util.Scanner;

public class main_2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();  // 150
        int B = sc.nextInt();  // 266
        int C = sc.nextInt();  // 427

        int ABC = A * B * C;    // 17037300

        int[] zTn = new int[10];    // zTn[] = 0 ~ 9 (index)

        while(ABC > 0) {
            zTn[ABC % 10]++;    // (자리수 == zTn 인덱스) -> +1
            ABC /= 10;
        }

        for(int i = 0; i < 10; i++) {
            System.out.println(zTn[i]);
        }


        sc.close();
    }
}
