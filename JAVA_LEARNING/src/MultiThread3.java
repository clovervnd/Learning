/**
 * Created by joonki on 16. 12. 28.
 */
public class MultiThread3 extends Thread{
    String name;

    public MultiThread3(String name) {
        this.name = name;
    }
    public void run(){
        for (int i=0;i<50;i++){
            System.out.println(name+"(우선 순위"+getPriority()+")");
        }
    }

}

class TutorialThread3
{
    public static void main(String[] args){
        MultiThread3 mt1 = new MultiThread3("Thread1");
        MultiThread3 mt2 = new MultiThread3("Thread2");
        MultiThread3 mt3 = new MultiThread3("Thread3");

        mt1.setPriority(Thread.MIN_PRIORITY);
        mt2.setPriority(Thread.NORM_PRIORITY);
        mt3.setPriority(Thread.MAX_PRIORITY);


        mt1.start();
        mt2.start();
        mt3.start();
    }
}