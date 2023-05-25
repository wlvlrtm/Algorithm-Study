package b15596;

public class Main {

    long sum(int[] a) {
        int y = 0;
        long result = 0;

        for (y = 0; y < a.length; y++) {
            result += a[y];
        }
        return result;
    }
}
