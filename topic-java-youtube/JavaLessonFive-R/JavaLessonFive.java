
// Programmer:     Cheng, Jeff
// Last Modified:  06-15-2024 08:08PM
// Problem:        Java Tutorial 5

import java.util.Scanner;

class Person
{
    private String lastName;
    private String firstName;
    private int age;

    //  constructor
    public Person(String last, String first, int a)
    {
        lastName = last;
        firstName = first;
        age = a;
    }

    public void displayPerson()
    {
        System.out.print("  Last name : " + lastName);
        System.out.print(", First name : " + firstName);
        System.out.println(", Age : " + age);
    }

    //  get last name
    public String getLast()
    {
        return lastName;
    }
}   //  end class Person

class ClassDataArray
{
    //  reference to array
    private Person[] a;
    //  number of data items
    private int nElems;

    //  constructor
    public ClassDataArray(int max)
    {
        //  create the array
        a = new Person[max];
        //  no items yet
        nElems = 0;
    }

    public Person find(String searchName)
    {
        //  find specified value
        int j;
        //  for each element
        for (j = 0; j < nElems; j++)
        {
            //  found item?
            if (a[j].getLast().equals(searchName))
            {
                //  exit loop before end
                break;
            }
        }
        //  gone to end
        if (j == nElems)
        {
            //  yes, can't find it
            return null;
        }
        else
        {
            //  no, found it
            return a[j];
        }        
    }   //  end find()

    //  put person into array
    public void insert(String last, String first, int age)
    {
        //  append at the end
        a[nElems] = new Person(last, first, age);
        //  increment size
        nElems += 1;
    }

    //  delete person from array
    public boolean delete(String searchName)
    {
        int j;
        //  look for it
        for (j = 0; j < nElems; j++)
        {
            if (a[j].getLast().equals(searchName))
            {
                break;
            }
        }
        //  can't find it
        if (j == nElems)
        {
            return false;
        }
        else
        //  found it
        {
            //  shift down
            for (int k = j; k < nElems-1; k++)
            {
                a[k] = a[k+1];
            }
            //  decrement size
            nElems -= 1;
            return true;
        }
    }   //  end delete()

    //  display array contents
    public void displayA()
    {
        //  for each element,
        for (int j = 0; j < nElems; j++)
        {
            //  display it
            a[j].displayPerson();
        }
    }
}   //  end class ClassDataArray

public class JavaLessonFive
{
    //  class variable 
    static double myPI = 3.14159;
    static int randomNumber;
    static Scanner userInput = new Scanner(System.in);
 
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
            
            //  decide whether to continue loop
            guessResult = checkGuess(randomGuess);
            //  only informs
            compareGuess(randomGuess);
        }
        System.out.println("Yes, the random number is " + randomGuess);

        //  array size
        int maxSize = 100;

        //  reference to array
        ClassDataArray arr;

        //  create the array
        arr = new ClassDataArray(maxSize);

        //  insert 10 items
        arr.insert("Evans", "Patty", 24);
        arr.insert("Smith", "Lorraine", 37);
        arr.insert("Yee", "Tom", 43);
        arr.insert("Adams", "Henry", 63);
        arr.insert("Hashimoto", "Sato", 21);
        arr.insert("Stimson", "Henry", 29);
        arr.insert("Velasquez", "Jose", 72);
        arr.insert("Lamarque", "Henry", 54);
        arr.insert("Vang", "Minh", 22);
        arr.insert("Creswell", "Lucinda", 18);

        //  display items
        arr.displayA();

        //  search for item
        String searchKey = "Stimson";
        Person found;

        found = arr.find(searchKey);

        if (found != null)
        {
            System.out.print("Found : ");
            found.displayPerson();
        }
        else
        {
            System.out.println("Can't find : " + searchKey);
        }

        System.out.println("Deleting Smith, Yee, and Creswell");
        //  delete 3 items
        arr.delete("Smith");
        arr.delete("Yee");
        arr.delete("Creswell");

        //  display items again
        arr.displayA();
    }   //  end main()
}   //  end class