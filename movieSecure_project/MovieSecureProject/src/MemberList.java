import java.sql.*;

public class MemberList {
    public static void main(String[] args) {
        // MySQL 접속 주소
        String url = "jdbc:mysql://localhost:3306/movie_db";
        //MySQL 사용자 계정
        String user ="root";
        //MySQL 비밀번호
        String password = "sql12345";

        try{
            // Java와 MySQL 연결
            Connection conn =
                    DriverManager.getConnection(url, user, password);
            String sql = "SELECT * FROM member";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            System.out.println("[영화관 회원 목록]");
            while (rs.next()){
                int memberId = rs.getInt("m_id");
                String userId = rs.getNString("user_id");
                String memberName = rs.getNString("m_name");
                String memberRole = rs. getNString("m_role");
                System.out.println(memberId+"/"+userId+"/"+memberName+"/"+memberRole);
            }
            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            System.out.println("데이터베이스 오류입니다");

            System.out.println("오류 내용: " + e.getMessage());
        }
    }
}
