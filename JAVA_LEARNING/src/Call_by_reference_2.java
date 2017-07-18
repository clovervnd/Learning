/**
 * Created by joonki on 17. 1. 4.
 */
public class Call_by_reference_2 {
    private static void swap(Integer a, Integer b){
        Integer temp = a; //하지만 이런식으로 swap한다고 해서 main함수 내의 reference가 swap되지는 않는다.
        a = b;
        b = temp;
    }

    public static void main(String args[]){
        Integer a = new Integer(1); //Object는 call by reference이다.
        Integer b = new Integer(2);

        System.out.println("a=>"+a);
        System.out.println("b=>"+b);

        swap(a,b);

        System.out.println("-------- swap 후 --------");

        System.out.println("a=>"+a);
        System.out.println("b=>"+b);
    }
}