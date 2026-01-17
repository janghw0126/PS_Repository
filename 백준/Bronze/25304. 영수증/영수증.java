import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long X = sc.nextLong(); // 총 금액
        int N = sc.nextInt();   // 물건 종류 개수

        long sum = 0;

        for (int i = 0; i < N; i++) {
            long price = sc.nextLong();
            long count = sc.nextLong();
            sum += price * count;
        }

        if (sum == X) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        sc.close();
    }
}
