/**
 * Created by joonki on 16. 12. 27.
 */
class ParentClass_2 {
    private int x;
    private int y;

    public ParentClass_2(int x, int y){
        this.x = x;
        this.y = y;
    }

    public void xyDisplay(){
        System.out.println("Parent Class, x= "+ x +", y= "+ y);
    }
}

class ChildClass_2 extends ParentClass_2 {
    private int x;
    private int y;

    public ChildClass_2(int x, int y){
        super(x*3, y*2);
        this.x = x;
        this.y = y;
    }

    public void childMethod(){
        super.xyDisplay();
        xyDisplay();
    }

    public void xyDisplay(){
        System.out.println("ChildClass, x= "+x+", y= "+y);

    }

}

class InheritanceExample2{
    public static void main(String[] args)
    {
        ChildClass_2 child = new ChildClass_2(44, 7);
        child.childMethod();
    }

}