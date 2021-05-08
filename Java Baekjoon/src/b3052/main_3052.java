package b3052;

import java.nio.file.FileSystemNotFoundException;
import java.util.Scanner;
import java.util.HashSet;

public class main_3052 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashSet<Integer> hashSet = new HashSet<Integer>();

        for(int i = 0; i < 10; i++) {
            hashSet.add(scanner.nextInt() % 42);
        }

        System.out.println(hashSet.size());
    }
}
