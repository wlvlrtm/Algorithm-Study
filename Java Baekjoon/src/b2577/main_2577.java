package b2577;

import java.util.Scanner;

public class main_2577 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int A = scanner.nextInt();  // 150
        int B = scanner.nextInt();  // 266
        int C = scanner.nextInt();  // 427

        int ABC = A * B * C;    // 17037300

        int[] zTn = new int[10];    // zTn[] = 0 ~ 9 (index)

        while(ABC > 0) {
            zTn[ABC % 10]++;    // (자리수 == zTn 인덱스) -> +1
            ABC /= 10;
        }

        for(int i = 0; i < 10; i++) {
            System.out.println(zTn[i]);
        }
    }
}
