/**
 * Created by joonki on 16. 12. 27.
 */
public class Vehicle {

    private int speed =0;
    private int maxSpeed = 100;

    public Vehicle(int mspeed)
    {
        System.out.println("JAVA constructer is called\n");
        maxSpeed = mspeed;
    }

    public int showSpeed(){
        return speed;
    }

    public void speedUP(int increment){
        if (speed + increment > maxSpeed) {
            speed = maxSpeed;
        } else{
            speed += increment;
        }
    }

}

class VehicleMain{
    public static void main(String[] args){
        int[] apple = new int[20];

        Vehicle bike = new Vehicle(100);
        Vehicle bike2 = new Vehicle(200);

        bike.speedUP(1000);
        System.out.println("Bike is running at "+bike.showSpeed()+"km/h");

        bike2.speedUP(1000);
        System.out.println("Bike2 is running at "+bike2.showSpeed() +"km/h");
    }
}