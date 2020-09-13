import java.util.Arrays;

public class Fibonacci {
    public static int fibo(int n) {
        if(n == 1 || n == 2) {
            return 1;
        } else {
            return fibo(n - 1) + fibo(n - 2);
        }
    }

    public static String fibo_list(int n) {
        int[] out = new int[n];

        for(int i = 1; i <= n; i++) {
            out[i - 1] = fibo(i); 
        }

        return Arrays.toString(out);
    }

    public static void main(String[] args) {
        System.out.println("The 10th Fibonacci number: ");
        System.out.println(Fibonacci.fibo(10));
        System.out.println("\n");
        System.out.println("The first 10 Fibonacci numbers: ");
        System.out.println(Fibonacci.fibo_list(10));
    }
}
