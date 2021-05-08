package b3052;

import java.util.Scanner;


public class test {
    public static void main(String[] args) {
        int[] nums = {39, 40, 41, 42, 43, 44, 82, 83, 84, 85};
        int[] lNums = new int[10];
        int count = 0;

        // nums[10] = [39, 40, 41, 42, 43, 44, 82, 83, 84, 85]
        // lNums[10] = [39, 40, 41, 0, 1, 2]

        for(int i = 0; i < 10; i++) {
            lNums[i] = (nums[i] % 42);
        }

        for(int i = 0; i < 10; i++) {
            int n = 0;
            for(int a = i + 1; a < 10; a++) {
                if (lNums[i] == lNums[a]) {
                    count += 1;
                    break;
                }
            }
        }
        System.out.println(count);
    }
}
