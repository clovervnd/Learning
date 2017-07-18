/**
 * Created by joonki on 16. 12. 28.
 */
public class clsNumber {
    int num = 0;
    public synchronized void addNum(){
        num++;
    }

    /*
    public void addNum(){
        synchronized(this){
            num++;
        }
    }
     */


    public int getNum(){
        return num;
    }
}

class MultiThread4 extends Thread{
    clsNumber number;

    public MultiThread4(clsNumber cn){
        number = cn;
    }

    public void run(){
        for(int i=0;i<5000;i++){
            number.addNum();
        }
    }
}

class TutorialThread4{
    public static void main(String[] args){
        clsNumber number = new clsNumber();
        MultiThread4 mt1 = new MultiThread4(number);
        MultiThread4 mt2 = new MultiThread4(number);
        MultiThread4 mt3 = new MultiThread4(number);

        mt1.start();
        mt2.start();
        mt3.start();

        try{
            mt1.join();
            mt2.join();
            mt3.join();
        }   catch (Exception e){
            e.printStackTrace();
        }
        System.out.println(number.getNum());
    }
}