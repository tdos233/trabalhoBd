import org.voltdb.*;
import org.voltdb.client.*;

public class Client {

    public static void main(String[] args) throws Exception {

        /*
         * Instantiate a client and connect to the database.
         */
        org.voltdb.client.Client myApp;
        myApp = ClientFactory.createClient();
        myApp.createConnection("localhost");

        /*
         * Load the database.
         */
        

        //myApp.callProcedure("InsertIntoAcidente", "2017/11/06","00:00", 3687941);
        //myApp.callProcedure("Insert", "French", "Bonjour", "Monde");
        //myApp.callProcedure("Insert", "Spanish", "Hola", "Mundo");
        //myApp.callProcedure("Insert", "Danish", "Hej", "Verden");
        //myApp.callProcedure("Insert", "Italian", "Ciao", "Mondo");

        /*
         * Retrieve the message.
         */
        final ClientResponse response = myApp.callProcedure("Select",
        3687941);
        if (response.getStatus() != ClientResponse.SUCCESS){
            System.err.println(response.getStatusString());
            System.exit(-1);
        }

        final VoltTable results[] = response.getResults();
        if (results.length == 0 || results[0].getRowCount() != 1) {
            System.out.printf("I can't say Hello in that language.\n");
            System.exit(-1);
        }

        VoltTable resultTable = results[0];
        VoltTableRow row = resultTable.fetchRow(0);
        System.out.printf("%s, %s\n!\n", row.getString("Dat"),
                                       row.getString("uniquekey"));
    }
}
