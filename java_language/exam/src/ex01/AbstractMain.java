package ex01;

abstract class Company{
    String name;

    Company(String name){
        this.name=name;
    }
    void start(){
        System.out.println(name+"이 출근했습니다.");
    }
    void end(){
        System.out.println(name+"이 퇴근했습니다.");
    }
    abstract void  work();
}

class Devel extends Company{
    Devel(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 프로그램을 개발합니다.");
    }
}

class Designer extends Company{
    Designer(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 프로그램을 디자인합니다.");
    }
}

class Planner extends Company{
    Planner(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 프로그램을 기획합니다.");
    }
}

public class AbstractMain {
    public static void main(String[] args) {
        Company c1 = new Devel("홍길동");
        Company c2 = new Designer("장길동");
        Company c3 = new Planner("오길동");

        c1.start();
        c1.work();
        c1.end();
        System.out.println();
        c2.start();
        c2.work();
        c2.end();
        System.out.println();
        c3.start();
        c3.work();
        c3.end();
    }
}
