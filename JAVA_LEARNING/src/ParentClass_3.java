/**
 * Created by joonki on 16. 12. 27.
 */
public class ParentClass_3 {
    public void DisplayMethod(String str)
    {
        System.out.println("ParentClass의 DisplayMethod(String str) 호출: "+str);
    }
}

class ChildClass_3 extends ParentClass_3{
    public void DisplayMethod() {
        System.out.println("ChildClass의 DisplayMethod() 호출");
    }
}

class InehritanceExample_3{
    public static void main(String[] args){
        ChildClass_3 child = new ChildClass_3();

        child.DisplayMethod();
        child.DisplayMethod("JAVA!");
    }
}