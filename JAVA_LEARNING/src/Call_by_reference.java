/**
 * Created by joonki on 17. 1. 4.
 */
public class Call_by_reference {
    private static void swap(int a, int b){
        int temp = a;
        a = b;
        b = temp;
    }

    public static void main(String args[]){
        int a = 1;  // Primitive type은 call by value이다.
        int b = 2;

        System.out.println("a=>"+a);
        System.out.println("b=>"+b);

        swap(a,b);

        System.out.println("-------- swap 후 --------");

        System.out.println("a=>"+a);
        System.out.println("b=>"+b);
    }
}
