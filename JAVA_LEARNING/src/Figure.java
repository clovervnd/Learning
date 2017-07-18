/**
 * Created by joonki on 16. 12. 27.
 */
abstract public class Figure {
    abstract void area(int a, int b);

    void print_status(){
        System.out.println("This is abstract class Figure");
    }
}


class Tetragon extends Figure{
    void area(int a, int b){
        System.out.println("사각형의 넓이: "+(a*b));
    }

    void print_status(){
        System.out.println("This is class Tetragon");
    }
}

class Triangle extends Figure{
    void area(int a, int b){
        System.out.println("삼각형의 넓이: "+(a*b/2));
    }

    void print_status(){
        System.out.println("This is class Triangle");
    }
}

class Simple{
    public static void main(String args[]){
        Tetragon tetragon = new Tetragon();
        Triangle triangle = new Triangle(); // 추상 클래스를 상속받은 triangle로 객체를 생성
        // Figure figure = new Figure(); 추상 클래스로는 객체를 생성할 수 없음

        tetragon.print_status();
        triangle.print_status();

        tetragon.area(4,5);
        triangle.area(4,5);
    }
}