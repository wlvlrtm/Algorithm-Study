package b5622;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int result = 0;


        // num || Char
        String[][] numToChar = {
                {"A", "B", "C", "-"},
                {"D", "E", "F", "-"},
                {"G", "H", "I", "-"},
                {"J", "K", "L", "-"},
                {"M", "N", "O", "-"},
                {"P", "Q", "R", "S"},
                {"T", "U", "V", "-"},
                {"W", "X", "Y", "Z"}
        };


        // User Input
        String callNum;
        callNum = sc.next();

        // String Splint
        String[] cnSplint;
        cnSplint = callNum.split("");


        // One by one from cnSplint's element
        for (String num : cnSplint) {
            Loop1 : // Checking about is it equals num with callNum; Loop in numToChar's row.
            for (int i = 0; i < numToChar.length; i++) {
                //  Checking about is it equals num with callNum; Loop in numToChar's column.
                for (int j = 0; j < numToChar[0].length; j++) {
                    if (numToChar[i][j].equals(num)) {  // if num and callNum is equal,
                        result += (i + 3);      // cal. time

                        break Loop1;            // break
                    }
                }
            }
        }

        System.out.println(result);   // Print Result

        sc.close();
    }
}