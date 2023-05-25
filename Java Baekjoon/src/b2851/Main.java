package b2851;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] num = new int[10];
        int result = 0;

        for(int i = 0; i < 10; i++) {
            num[i] = sc.nextInt();    // 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

        }

        for(int i : num) {
            result += i;
            if (result == 100) {
                break;
            }
            else if (result > 100) {
                result = (Math.abs((result - 100)) > Math.abs((result - i - 100))) ? (result - i) : (result);
                break;
            }
        }

        System.out.println(result);


        sc.close();
    }
}
