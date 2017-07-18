/**
 * Created by joonki on 17. 1. 4.
 */
public class Call_by_reference_3 {

    int value;

    public Call_by_reference_3(int value){
        this.value = value;
    }

    private static void swap (Call_by_reference_3 a, Call_by_reference_3 b){
        int temp = a.value;
        a.value = b.value;
        b.value = temp;
    }

    public static void main(String[] args){
        Call_by_reference_3 a = new Call_by_reference_3(1);
        Call_by_reference_3 b = new Call_by_reference_3(2);

        System.out.println("a=>"+a.value);
        System.out.println("b=>"+b.value);

        swap(a,b);

        System.out.println("------- swap 후 --------");

        System.out.println("a=>"+a.value);
        System.out.println("b=>"+b.value);
    }

}
