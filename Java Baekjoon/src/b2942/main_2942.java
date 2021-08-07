package b2942;

import java.util.Scanner;

public class main_2942 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int count = 0;

        // User Input
        String str = input.nextLine();


        // find Croatia's alphabets
        for (int i = 0; i < str.length(); i++) {
            char temp = str.charAt(i);

            switch(temp) {
                case 'c':
                    if (i+1 < str.length()) {
                        if (str.charAt(i+1) == '=' || str.charAt(i+1) == '-') {
                            i += 1;
                        }
                    }
                    break;

                case 'd':
                    if (i+1 < str.length()) {
                        if (str.charAt(i+1) == 'z') {
                            if (i+2 < str.length()) {
                                if (str.charAt(i+2) == '=') {
                                    i += 2;
                                }
                            }
                        }
                        else if (str.charAt(i+1) == '-') {
                            i += 1;
                        }
                    }
                    break;

                case 'n':
                case 'l':
                    if (i+1 < str.length()) {
                        if (str.charAt(i+1) == 'j') {
                            i += 1;
                        }
                    }
                    break;
                case 'z':
                case 's':
                    if (i+1 < str.length()) {
                        if (str.charAt(i+1) == '=') {
                            i += 1;
                        }
                    }
                    break;
            }
            count++;
        }

        // Result
        System.out.println(count);
    }
}
