/**
 * Created by joonki on 16. 12. 28.
 */
public class MultiThread2 implements Runnable{  // Thread class를 상속받아 구현하는 것이 더 간편하나 Thread class를 상속받으면 다른 클래스를 상속받을 수 없음
    String name;

    public MultiThread2(String name){
        System.out.println(name + "스레드가 생성되었습니다");
        this.name = name;
    }

    public void run() {
        for (int i=0;i<50;i++){
            System.out.println(Thread.currentThread().getName() + "("+name+")");
        }
        try{
            Thread.sleep(100);
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }
}

class TutorialTherad2 {
    public static void main(String[] args){
        MultiThread2 mt1 = new MultiThread2("Thread1");
        MultiThread2 mt2 = new MultiThread2("Therad2");
        MultiThread2 mt3 = new MultiThread2("Thread3");

        Thread tr1 = new Thread(mt1);
        Thread tr2 = new Thread(mt2);
        Thread tr3 = new Thread(mt3);

        tr1.start();
        tr2.start();
        tr3.start();
    }
}
