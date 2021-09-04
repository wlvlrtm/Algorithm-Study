package b1316;

import java.util.Scanner;

public class main_1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // group words count
        int result = 0;

        // User Input; number of words
        int count = sc.nextInt();


        // User Input; words
        for (int i = 0; i < count; i++) {
            String word = sc.next();

            if (check(word)) {
                result += 1;
            }
        }


        // Result print
        System.out.println(result);


        sc.close();
    }



    public static boolean check(String word) {
        boolean[] alphabets = new boolean[26];  // array of alphabets (26: A to Z)
        char preTemp = ' '; // front char

        for (int i = 0; i < word.length(); i++) {
            char temp = word.charAt(i); // current char

            // if the same char doesn't repeat,
            if (temp != preTemp) {
                // if current char is new one,
                if (!alphabets[(int)temp - 'a']) {
                    alphabets[(int)temp - 'a'] = true;  // change the array's state.
                    preTemp = temp; // change the front char
                }
                else {  // if current char is same of front char even though they didn't repeat; if that word is not group word,
                    return false;   // false; It's not a group word
                }
            }
            // else: if the same character is repeatedly, -> continue
        }

        return true;    // It's a group word
    }
}