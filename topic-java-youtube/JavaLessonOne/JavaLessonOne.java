
// Programmer:     Cheng, Jeff
// Last Modified:  05-31-2024 08:50AM
// Problem:        Java Tutorial 1

//  demonstrates basic OOP syntax

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class BankAccount
{
    //  account balance
    private double balance;

    //  constructor
    public BankAccount(double openingBalance)
    {
        balance = openingBalance;
    }

    //  makes deposit
    public void deposit(double amount)
    {
        balance += amount;
    }

    //  makes withdrawal
    public void withdraw(double amount)
    {
        balance -= amount;
    }

    //  displays balance
    public void display()
    {
        System.out.println("balance = " + balance);

    }
};  //  end class BankAccount

//  class BankApp
public class JavaLessonOne
{
    static String randomString = "String to print";
    //  final == const
    static final double PINUM = 3.141529;

    //  static => only a class can call this method
    //  public => accessible by all classes

    //  prompts user to enter a string and returns the string
    public static String getString() throws IOException
    {
    InputStreamReader isr = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(isr);
    String s = br.readLine();
    return s;
    }

    //  prompts user to enter a string and returns the first character 
    public static char getChar() throws IOException
    {
        String s = getString();
        //  prevents extraneous characters being left in the input buffer, because
        //  such characters can cause problems with subsequent input
        return s.charAt(0);
    }

    //  prompts user to enter a string containing a number
    public static int getInt() throws IOException
    {
        //  to read numbers, we make a String object and then convert it to the type we want using a conversion method
        String s = getString();
        return Integer.parseInt(s);
    }

    //  prompts the user to enter a string containing a double
    public static double getDouble() throws IOException
    {
        String s = getString();
        //  converting String object to a Double object using the wrappper class Double
        Double aDub = Double.valueOf(s);
        return aDub.doubleValue();
    }

    public static void main(String[] args)
    {
        System.out.println("String literal = Hello World");
        System.out.println("static String randomString = " + randomString);
        System.out.println("static final double PINUM = " + PINUM);

        int integerOne = 21, integerTwo 
        = 
        integerOne 
        + 1; 
        System.out.println("int integerTwo = " + integerTwo);
        byte bigByte = 127;
        short bigShort = 32767;
        int bigInt = 2100000000;
        long bigLong = 9220000000000000000L;
        float bigFloat = 3.14F;
        double bigDouble = 3.1234567890D;

        System.out.println("byte bigByte = " + bigByte);
        System.out.println("short bigShort = " + bigShort);
        System.out.println("int bigInt = " + bigInt);
        System.out.println("long bigLong (terminating L required) = " + bigLong);
        System.out.println("float bigFloat = " + bigFloat);
        System.out.println("double bigDouble (terminating D optinal)= " + bigDouble);

        System.out.println("Float.MAX_VALUE = " + Float.MAX_VALUE);
        System.out.println("Double.MAX_VALUE = " + Double.MAX_VALUE);

        boolean trueOrFalse = true;
        char randomChar = 65;
        char anotherChar = 'A';

        System.out.println("boolean trueOrFalse = " + trueOrFalse);
        System.out.println("char = " + randomChar);
        System.out.println("anotherChar = " + anotherChar);

        String randomString2 = "I'm a random string";
        String anotherString = "Stuff";
        String andAnotherString = randomString2 + ' ' + anotherString;
        System.out.println("String andAnotherString = " + andAnotherString);
        
        String byteString = Byte.toString(bigByte);
        String shortString = Short.toString(bigShort);
        String intString = Integer.toString(bigInt);
        String longString = Long.toString(bigLong); 
        String floatString = Float.toString(bigFloat);
        String doubleString = Double.toString(bigDouble);
        String booleanString = Boolean.toString(trueOrFalse);

        System.out.println("String byteString = Byte.toString(bigByte) = " + byteString);
        System.out.println("String shortString = Short.toString(bigShort) = " + shortString);
        System.out.println("String longString = Long.toString(bigLong) = " + longString);
        System.out.println("String floatString = Float.toString(bigFloat) = " + floatString);
        System.out.println("String doubleString = Double.toString(bigDouble) = " + doubleString);
        System.out.println("String booleanString = Boolean.toString(trueOrFalse) = " + booleanString);

        double aDoubleValue = 3000000000000.14546466464;
        int doubleToInt = (int) aDoubleValue;

        System.out.println("int doubleToInt = (int) aDoubleValue = " + doubleToInt);
        
        int stringToInt = Integer.parseInt(intString);
        System.out.println("int stringToInt = Integer.parseInt(String intString = Integer.toString(bigInt)) = " + stringToInt);

        //  create acct
        BankAccount ba1 = new BankAccount(100.00);

        System.out.print("Before transactions, ");
        //  display balance
        ba1.display();

        //  make deposit
        ba1.deposit(74.35);

        //  make withdrawl
        ba1.withdraw(20.00);

        System.out.print("After transactions, ");
        //  display balance
        ba1.display();

        BankAccount ba2 = ba1;
        if (ba1 == ba2)
        {
            System.out.println("Java references: they are identical!");
        }
        if (ba2.equals(ba1))
        {
            System.out.println("They are equal: meaning they contain the same data!");
        }

        String userInputString = "";
        char userInputChar = 'a';
        int userInputInt = -1;
        double userInputDouble = 0.0;
        try
        {
            System.out.println("Please enter any string : ");
            userInputString = getString();
            System.out.println("The string you entered : " + userInputString);

            System.out.println("Now please another string from which the first character will be retrieved: ");
            userInputChar = getChar();
            System.out.println("The character you entered : " + userInputChar);

            System.out.println("Now, please enter another string containing an integer (numbers only) : ");
            userInputInt = getInt();
            System.out.println("The integer you entered : " + userInputInt);

            System.out.println("Finally, please enter a string containing a floating number (numbers only, except the decimal point) : ");
            userInputDouble = getDouble();
            System.out.println("The floating number you entered : " + userInputDouble);
        }
        catch (IOException e)
        {
            System.out.println("An IO exception has taken place.  Program will now exit.");
        }        
        catch (Exception e)
        {
            System.out.println("An unexpected exception has taken place.  Program will now exit.");
        }
    }   //  end main()
}   //  end class BankApp