/**
 * Created by joonki on 16. 12. 28.
 */
import java.util.Scanner;

class calculators {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("피제수를 입력하세요: ");
            int num1 = sc.nextInt();
            System.out.print("제수를 입력하세요: ");
            int num2 = sc.nextInt();
            System.out.println(num1 + "을 " + num2 + "로 나눈 값은 " + num1 / num2 + "입니다.");
        } catch (ArithmeticException ae) {
            System.out.println("피제수를 0으로 나눌 수는 없습니다. (" + ae + ")");
        } finally {
            System.out.println("Finally 영역이 실행되었습니다");
        }
    }
}
