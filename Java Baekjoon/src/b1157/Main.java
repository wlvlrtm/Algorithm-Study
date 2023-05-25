package b1157;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int max = -1;               // 가장 많은 알파벳
        char ch = '?';             // 가장 많은 알파벳이 중복일 경우


        int[] arr = new int[26];    // 영문자 26자리 배열

        String word = sc.next();   // 단어 입력 Ex) zZa


        // 단어 검사
        for(int i = 0; i < word.length(); i++) {

            if(65 <= word.charAt(i) && word.charAt(i) <= 90) {
                arr[word.charAt(i) - 65] += 1;  // 대문자
            }
            else {
                arr[word.charAt(i) - 97] += 1;  // 소문자
            }
        }


        // 가장 많은 알파벳 검사
        for(int j = 0; j < 26; j++) {
            if(max < arr[j]) {
                max = arr[j];       // max == 알파벳 중복 개수
                ch = (char) (j + 65);   // j + 65 == 알파벳 ASCII 코드; j == 알파벳 번호 ex) j == 25 == 'Z'
            }
            else if (max == arr[j]) {
                ch = '?';
            }
        }

        System.out.println(ch); // 결과 출력


        sc.close();
    }
}
