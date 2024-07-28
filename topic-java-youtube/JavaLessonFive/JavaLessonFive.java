
// Programmer:     Cheng, Jeff
// Last Modified:  06-15-2024 08:08PM
// Problem:        Java Tutorial 5

import java.util.Scanner;

public class JavaLessonFive
{
    //  class variable 
    static double myPI = 3.14159;
    static int randomNumber;
    static Scanner userInput = new Scanner(System.in);

    //  this can come before or after the main function
    public static int addThem(int a, int b)
    {
        //  local variable, only accessible here
        double smallPI = 3.140;

        System.out.println("Global PI: " + myPI);

        //  local variable overwriting the global within the function scope
        //  therefore, you can use class variables anywhere, but you can also "change" their values
        //  in different scopes
        double myPI = 3.0; 

        System.out.println("Global [actually local] PI: " + myPI);
        return a + b;
    }
 
    public static void tryToChange(int d)
    {
        d = d + 1;
        System.out.println("tryToChange d = " + d);
    }

    public static int getRandomNum()
    {
        randomNumber = (int) (Math.random() * 51);
        return randomNumber;
    }

    public static int checkGuess(int guess)
    {
        if (guess == randomNumber)
        {
            return -1;
        }
        else
        {
            return guess;
        }
    }

    public static void compareGuess(int guess)
    {
        if (guess > randomNumber)
        {
            System.out.println("Guess is too high");
        }
        else if (guess < randomNumber)
        {
            System.out.println("Guess is too low");
        }
        else
        {
            System.out.println("Guess is spot on!");
        }
    }

    public static void main(String[] args)
    {
        //  accessModifier [static 
        //  = used whenever you want to access a method that is NOT part of a class definition]
        //  returnType methodName([parameters/arguments])
        System.out.println(addThem(7, 11));        

        int d = 5;
        tryToChange(d);

        System.out.println("Main d = " + d);

        System.out.println(getRandomNum());
        
        //  flag
        int guessResult = 1;

        int randomGuess = 0;
        while (guessResult != -1)
        {
            System.out.println("Guess a number between 0 and 50 : ");
            randomGuess = userInput.nextInt();
            guessResult = checkGuess(randomGuess);
            compareGuess(randomGuess);
        }
        System.out.println("Yes, the random number is " + randomGuess);
    }
}