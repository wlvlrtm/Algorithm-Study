package b10809;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        String S;                   // word S val.
        int[] arr = new int[26];    // alphabet array


        // arr reset; ALL -1
        Arrays.fill(arr, -1);


        // User Input; ex) baekjoon
        S = sc.next();

        // word S slice
        for(int i = 0; i < S.length(); i++) {
            char S_alpha = S.charAt(i);

            // Avoid duplication
            if(arr[S_alpha - 'a'] == -1) {
                arr[S_alpha - 'a'] = i;
            }
        }

        // Print Result
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }


        sc.close();
    }
}
