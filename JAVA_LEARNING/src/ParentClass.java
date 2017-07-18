/**
 * Created by joonki on 16. 12. 27.
 */
class ParentClass {
    public void parentMethod(){
        System.out.println("부모의 클래스의 parentMethod가 호출되었습니다. \n");
    }
}

class ChildClass extends ParentClass{
    public void childMethod(){
        System.out.println("자식 클래스의 childMethod가 호출되었습니다.\n");
        System.out.println("부모 메소드의 parentMethod를 호출했습니다 \n");
        parentMethod(); // ParentClass를 상속했기 때문에 class안에 parentMethod가 정의되어있는것처럼 쓸 수 있다.
    }
}

class InheritanceExample{
    public static void main(String[] args){
        ChildClass child = new ChildClass();

        System.out.println("간단한 자바 상속의 예\n");
        System.out.println("자식 클래스의 childMethod를 호출했습니다\n");
        child.childMethod();
    }
}
