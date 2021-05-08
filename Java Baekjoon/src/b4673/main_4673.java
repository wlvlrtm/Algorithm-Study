package b4673;

public class main_4673 {
    public static void main(String[] args) {
        // 셀프 넘버 점검 리스트
        boolean[] Num = new boolean[10000];

        // 1 to 10000
        for(int n = 1; n <= Num.length; n++) {
            int x = d(n);   // x = n의 각 자리수를 더한 값; 생성자
            if (x < Num.length) {   // 생성자가 범위 내에 있는가; (범위: 10000)
                Num[x] = true;  // 생성자 인덱스에 셀프 넘버 여부 체크
            }
        }

        // 1 to 10000
        for(int i = 1; i < Num.length; i++) {
            if (!Num[i]) {  // 셀프 넘버라면,
                System.out.println(i);  // 해당 인덱스 값 출력
            }
        }
    }

    // n의 각 자리수 더하기; 생성자 계산
    private static int d(int n) {
        int T = 0;
        T += n;

        while(n != 0) {
            T += (n % 10);
            n = (n / 10);
        }
        return T;
    }
}