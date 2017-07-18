/**
 * Created by joonki on 16. 12. 28.
 */

import java.util.Scanner;

public class scantutorial {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        System.out.println("당신의 이름은?");
        String name = sc.nextLine();

        System.out.println("당신의 나이는?");
        int age = sc.nextInt();

        System.out.println("당신의 몸무게는?");
        Double weight = sc.nextDouble();

        System.out.println("당신의 이름은 "+name+"이고, 당신의 나이는 "+age+"살이며, 당신의 몸무게는 "+weight+"kg 입니다.");
    }
}
