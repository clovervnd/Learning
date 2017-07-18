/**
 * Created by joonki on 16. 12. 29.
 */
import java.io.*;

public class FileTutorial3 {
    public static void main(String[] args) throws IOException{
        FileInputStream in = new FileInputStream("test.txt");
        int ch;

        while((ch=in.read())!=-1){
            System.out.println((char)ch);
        }
        in.close();
    }
}
