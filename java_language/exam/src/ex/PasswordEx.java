package ex;

public class PasswordEx {

    public static void main(String[] args) {
        String [] pw = {"pass2026","java","Admin123"};
        int ovchar=0;
        for (String i:pw){
            int len = i.length();
            System.out.println("\n비밀번호: "+i);
            System.out.println("비밀번호 길이: "+len);
            if(len>=6){
                System.out.println("길이 조건 통과");
                ovchar++;}
            else System.out.println("길이 조건 미통과");

            System.out.println("대문자 변환: "+i.toUpperCase());
            System.out.println("소문자 변환: "+i.toLowerCase());

            System.out.println("첫번째 문자: "+i.charAt(0));
        }
        System.out.println("\n길이 조건을 통과한 비밀번호 수: "+ovchar);
    }
}