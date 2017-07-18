/**
 * Created by joonki on 16. 12. 28.
 */
import java.io.*;

public class FileTutorial {
    public static void main(String[] args) throws IOException{
        FileReader reader = new FileReader("test.txt");
        int ch;

        while ((ch = reader.read())!= -1){
            System.out.println((char)ch);
        }
        reader.close();
    }
}


