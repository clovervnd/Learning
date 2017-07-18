/**
 * Created by joonki on 16. 12. 27.
 */
interface aExample {
    public void sayHello();
}

interface bExample {
    public void sayBye();
}

class JavaInterfaceExample implements aExample, bExample{
    public void sayHello(){
        System.out.println("안녕!");
    }

    public void sayBye(){
        System.out.println("잘가!");
    }

    public static void main(String args[]){
        JavaInterfaceExample javaInterfaceExample = new JavaInterfaceExample();
        javaInterfaceExample.sayBye();
        javaInterfaceExample.sayHello();

    }
}

