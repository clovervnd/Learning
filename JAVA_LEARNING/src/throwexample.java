/**
 * Created by joonki on 16. 12. 28.
 */
import java.util.Scanner;

class NegativeException extends Exception{
    public NegativeException(){
        super("음수는 입력될 수 없습니다.");
    }
}

public class throwexample {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("숫자를 입력하세요: ");

        try{
            int num = sc.nextInt();
            System.out.println(inputnum(num));
        }   catch (NegativeException ne){
            System.out.println(ne);
        }
    }
    public static int inputnum(int num) throws NegativeException {
        if(num < 0){
            NegativeException ext = new NegativeException();
            throw ext;
        }

        return num;
    }
}
