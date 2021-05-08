package b2562;

import java.util.Scanner;

public class main_2562 {
    public static void main(String[] args) {
        int[] list = new int[9];

        int max = 0;
        int indx = 1;

        Scanner scanner = new Scanner(System.in);

        for(int i = 0; i <= 8; i++) {    // int num input
            list[i] = scanner.nextInt();
        }

        max = list[0];

        for(int i = 0; i <= 8; i++) {   // finding MAX
            if (max < list[i]) {
                max = list[i];
                indx = i+1;
            }
        }

        System.out.println(max);
        System.out.println(indx);
    }
}
