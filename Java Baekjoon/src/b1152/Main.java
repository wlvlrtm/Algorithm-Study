package b1152;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // User Input
        String word = sc.nextLine().trim();   

        if (word.isEmpty()) {
            System.out.println(0);
        }
        else {
            String[] words = word.split(" ");
            System.out.println(words.length);
        }

        sc.close();
    }
}