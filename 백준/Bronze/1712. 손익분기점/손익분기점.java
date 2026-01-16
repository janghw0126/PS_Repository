import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long A = sc.nextLong(); 
        long B = sc.nextLong(); 
        long C = sc.nextLong(); 

        if (C <= B) {
            System.out.println(-1);
            return;
        }

        long breakEven = A / (C - B) + 1;
        System.out.println(breakEven);
    }
}
