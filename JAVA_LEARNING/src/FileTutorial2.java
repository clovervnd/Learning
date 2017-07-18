/**
 * Created by joonki on 16. 12. 28.
 */
import java.io.*;

class FileTutorial2 {
    public static void main(String[] args) throws IOException {
        FileWriter reader = new FileWriter("test.txt"); // 텍스트 파일이 없으면 새로 생성함!

        reader.write("입출력!"); // 파일에 "입출력!"을 저장함.
        reader.append('!'); // 파일의 끝에 ! 문자를 추가시킴.
        reader.close(); // 파일을 닫음.
    }
}
