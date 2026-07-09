package ex01;

class Employee{ //슈퍼 클래스
	public int pay() {
		return 0;
	}
}

class FullTime extends Employee{ //서브 클래스

	@Override
	public int pay() { //재정의
		return 5000000;
	} 
	public void work() {
		System.out.println("정규직 직원이 일을 합니다.");
	}
}
public class Main2 {

	public static void main(String[] args) {
		FullTime e1= new FullTime();
		Employee p1= new Employee();
		//다형성: 부모타입-자식 객체 생성, 동적바인딩(자식 생성)
		Employee f1= new FullTime();
		System.out.println("부모 메서드: "+p1.pay());
		System.out.println("자식 메서드: "+e1.pay());
		System.out.println("다형성: "+f1.pay());
		e1.work();
		// f1.work();  //오류 자식한테만 있는 메서드이기 때문에
	}

}
