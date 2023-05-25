package b1110;

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N;
        int N1;
        int T;
        int count = 0;

        N = sc.nextInt();
        T = 0;

        N1 = N;

        while(true) {
            T = ((N%10) * 10) +(((N / 10) + (N % 10)) % 10);
            N = T;
            count++;

            if (N1 == N) {
                System.out.println(count);
                break;
            }
        }

        sc.close();
    }
}
