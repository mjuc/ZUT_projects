import java.sql.*;

class lab1{
    public static void main(String args[]){
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con=DriverManager.getConnection( "jdbc:mysql://localhost:3306/lab","user","");
            Statement stmt=con.createStatement();
            ResultSet resultSet = stmt.executeQuery("select * form test");
            while(resultSet.next())
            {
                System.out.println(resultSet.getString(2));
            }
        }
        catch(Exception e)
        {
            System.out.print(e);
        }
    }  
}