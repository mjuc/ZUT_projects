import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;

public class Main {


    public static void main()
    {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("nextlab");
        EntityManager em = emf.createEntityManager();

        // zadanie 5

        Person person = new Person();
        person.setFirstName("Jan");
        person.setFamilyName("Kowalski");
        person.setAge(20);

        em.getTransaction().begin();
        em.persist(person);
        em.getTransaction().commit();

        // zadanie 6

        String query = "UPDATE Person SET age = 18 WHERE age < 18";

        Query q = em.createQuery(query);
        int result = q.executeUpdate();

        // zadanie 7

        String cntQuery = "SELECT COUNT(p) FROM Person";
        Query cntQ = em.createQuery(cntQuery);
        result = cntQ.getMaxResults();

        // zadanie 8

        String aQuery = "SELECT p FROM Person WHERE p.name LIKE 'a%'";
        Query aQ = em.createNamedQuery(aQuery);
        result = cntQ.getMaxResults();
    }
}
