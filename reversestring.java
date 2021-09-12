class Test1{
    Test1(int x){
        System.out.print("constructor called"+x);
    }
}
public class Main{
    Test1 t1=new Test1(10);
    Main(int i){
        t1=new Test1(i);
    }
    public static void main(String args[]){
        Main t2=new Main(5);
    }
}