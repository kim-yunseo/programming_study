package ex;

public class Employee {
    String name;
    int basePay;
    Employee(String name, int basePay){
        this.name=name;
        this.basePay=basePay;
    };
    int getPay(){
        return basePay;
    }
    void printInfo(){
        System.out.println(name+"의 급여: "+getPay());
    }
}
