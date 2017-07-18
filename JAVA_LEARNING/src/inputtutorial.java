/**
 * Created by joonki on 16. 12. 28.
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class inputtutorial {

    public static void main(String args[]){

        InputStreamReader isr = new InputStreamReader(System.in);   // 한 문자씩 읽어오고
        BufferedReader br = new BufferedReader(isr);    // 한 문자씩 읽은것을 입력받아서 한 줄씩 읽는다
        String str;

        try{
            System.out.println("당신의 이름은?");
            String name = br.readLine();
            System.out.println("당신의 나이는?");
            str = br.readLine();
            int age = Integer.parseInt(str);
            System.out.println("당신의 몸무게는?");
            str = br.readLine();
            double weight = Double.parseDouble(str);

            System.out.println("당신의 이름은 "+name+"이고, 당신의 나이는 "+age+"살이며, 당신의 몸무게는 "+weight+"kg 입니다.");
        }   catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
