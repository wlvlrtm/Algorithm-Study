package b1152;

import java.util.Scanner;

public class main_b1152 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String word = scanner.nextLine().trim();   // User Input

        if (word.isEmpty()) {
            System.out.println(0);
        }
        else {
            String[] words = word.split(" ");
            System.out.println(words.length);
        }
    }
}