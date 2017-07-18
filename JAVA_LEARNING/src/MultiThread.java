/**
 * Created by joonki on 16. 12. 28.
 */


public class MultiThread extends Thread {
    String name;

    public MultiThread(String name){
        System.out.println(getName()+"스러드가 생성되었습니다");
        this.name = name;
    }

    public void run(){
        for(int i=0;i<50;i++){
            System.out.println(getName()+"("+name+")");
            try {
                sleep(100);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

class TutorialThread
{
    public static void main(String[] args)
    {
        MultiThread mt1 = new MultiThread("Thread1");
        MultiThread mt2 = new MultiThread("Thread2");
        MultiThread mt3 = new MultiThread("Thread3");

        mt1.start();
        mt2.start();
        mt3.start();

    }

}