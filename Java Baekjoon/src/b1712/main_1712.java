package b1712;

import java.util.Scanner;

public class main_1712 {
    public static void main(String[] args) {
        int cost_A; // 1000
        int cost_B; // 70
        int cost_C; // 1070


        // User Input.
        Scanner sc = new Scanner(System.in);

        cost_A = sc.nextInt();
        cost_B = sc.nextInt();
        cost_C = sc.nextInt();


        // Break-Even Point Cal.
        if (cost_C <= cost_B) {
            System.out.println(-1);
        }
        else {
            int num = cost_A / (cost_C - cost_B);
            System.out.println(num+1);
        }


        sc.close();
    }
}
