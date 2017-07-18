/**
 * Created by joonki on 16. 12. 29.
 */
import java.io.*;

public class FileTutorial4 {
    public static void main(String[] args)throws IOException{
        FileOutputStream out = new FileOutputStream("test.txt",false);
        int ch;

        for(int i='a';i<='z';i++){
            out.write(i);
        }
        out.close();
    }
}
