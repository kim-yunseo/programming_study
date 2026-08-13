package ex;

public class ContractEmployee extends Employee{
    int bonus;
    ContractEmployee(String name, int basePay, int bonus){
        super(name, basePay);
        this.bonus=bonus;
    }
    @Override
    int getPay(){
        return basePay + bonus;
    }
    @Override
    void printInfo(){
        System.out.println(name+"의 계약직 급여: "+getPay());
    }

    public static void main(String[] args) {
        Employee[] employees = {new Employee("이순신", 3100000),
                new ContractEmployee("홍길동", 2000000, 300000)};

        int totalPay=0;

        for (Employee emp: employees){
            emp.printInfo();
            totalPay+=emp.getPay();
        }
        System.out.println("전체 급여 합계: " + totalPay);
    }

}
