
// Programmer:     Cheng, Jeff
// Last Modified:  06-16-2024 09:04PM
// Problem:        Java Tutorial 6

//  there are mainly two kinds of exceptions

//  these are your responsibility
//  java.lang.MainTimeException

//  these are checked by the compiler
//  java.lang.Exception

//  Arithmetic Exception
//  division by zer0

//  Class Not Found Exception
//  class is called that doesn't exist

//  Illegal Argument Exception

//  Index Out Of Bounds Exception

//  Input Mismatch Exception
//  Scaner method when you try to input the wrong data type

//  IO Exception

import java.util.*;
import java.io.*;

public class JavaLessonSix
{
    static Scanner userInput = new Scanner(System.in);

    public static void divideByZero(int a)
    {
        try
        {
            System.out.println(a/0);
        }
        catch(ArithmeticException e)
        {
            System.out.println("You can't do that!");
            System.out.println(e.getMessage());
            System.out.println(e.toString());
            e.printStackTrace();         
        } 
    }

    public static int checkValidAge()
    {
        try
        {
            return userInput.nextInt();
        }
        catch (InputMismatchException e)
        {
            //  flush the user input
            userInput.next();
            System.out.println("That isn't a whole number!");
            return 0;
        }
    }

    public static void getAFile(String fileName)
    {
        //  check expression -> complier checks for this
        try
        {
            FileInputStream file = new FileInputStream(fileName);           
        }
        catch (FileNotFoundException e)
        {
            System.out.println("Sorry can't find that file");
        }
        catch (Exception e)
        {
            //  ignore an error
        }
        finally
        {
            System.out.println("This is always called in the finally.");
        }
            }
    public static void main(String[] args)
    {
        divideByZero(2);
        System.out.println("How old are you?");
        int age = checkValidAge();

        if (age != 0)
        {
            System.out.println("You are " + age + " years old");
        }
        getAFile("./somestuff.txt");
    }
}