package b10818;

import java.util.Scanner;

public class main_10818 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = 0;
        int a = 0;
        int m = 0;
        int M = 0;
        n = scanner.nextInt();

        a = scanner.nextInt();
        m = a;
        M = a;

        for(int i = 1; i < n; i++) {
            a = scanner.nextInt();
            if (M < a) {
                M = a;
            }
            if (m > a) {
                m = a;
            }
        }
        System.out.print(m + " " + M);
    }
}
