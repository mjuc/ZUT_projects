import java.sql.*;

public class lab3 {

    public static void main(String args[]){
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con= DriverManager.getConnection( "jdbc:mysql://localhost:3306/lab","user","");
            Statement stmt=con.createStatement();
            ResultSet resultSet = stmt.executeQuery("select * form l2");
            while(resultSet.next())
            {
                System.out.println(resultSet.getString(2));
            }
        }
        catch(Exception e)
        {
            System.out.print(e);
        }
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con= DriverManager.getConnection( "jdbc:mysql://localhost:3306/lab","user","");
            Statement stmt=con.createStatement();
            ResultSet resultSet = stmt.executeQuery("insert into l2 values('1','test')");
            while(resultSet.next())
            {
                System.out.println(resultSet.getString(2));
            }
        }
        catch(Exception e)
        {
            System.out.print(e);
        }
        try {
            String input[]={"1","2","3","4","5","6","7","8","9","10"};
            Class.forName("com.mysql.jdbc.Driver");
            Connection con= DriverManager.getConnection( "jdbc:mysql://localhost:3306/lab","user","");
            PreparedStatement stmt=con.prepareStatement("INSERT INTO l2 VALUES(str = ?,num = ?)");
            for(int i=0;i<input.length;i++)
            {
                stmt.setInt(1,(int)(Math.random() * (10000 - 0)) + 0);
                stmt.setString(2,input[i]);
                stmt.execute();
            }
            con.commit();
        }
        catch (Exception e)
        {
            System.out.print(e);
        }
    }
}
