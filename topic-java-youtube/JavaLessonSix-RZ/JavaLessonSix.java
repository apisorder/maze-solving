
// Programmer:     Cheng, Jeff
// Last Modified:  09-19-2024 09:32PM
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

//  demonstrates bubble sort

class ArrayBub
{
    //  reference to array a
    private long[] a;
    //  number of data items
    private int nElemes;

    //  constructor
    ArrayBub(int max)
    {
        //  create the array
        a = new long[max];
        //  no items yet
        nElemes = 0;
    }
    //  put element into array
    public void insert(long value)
    {
        //  insert it
        a[nElemes] = value;
        //  increment size
        nElemes += 1;
    }

    //  displays array contents
    public void display()
    {
        //  for each element
        for (int j = 0; j < nElemes; j++)
        {
            //  display it
            System.out.print(a[j] + " ");
        }
        System.out.println("");
    }

    public int find(long searchKey)
    {
        int lowerBound = 0;
        int upperBound = nElemes-1;
        int curIn;

        while (true)
        {
            curIn = (lowerBound + upperBound)/2;

            if (a[curIn] == searchKey)
            {
                return curIn;
            }
            else if (lowerBound > upperBound)
            //  can't find it
            {
                return -1;
            }
            else
            {
                if (a[curIn] < searchKey)
                {
                    lowerBound = curIn + 1;
                }
                else
                {
                    upperBound = curIn - 1;
                }
            }
        }
    }

    public boolean delete(long value)
    {
        int j = find(value);

        if (j == -1)
        {
            return false;
        }
        else
        {
            for(int k = j; k < nElemes-1; k++)
            {
                a[k] = a[k+1];
            }
            //  remember to decrement the size
            nElemes -= 1;
            return true;
        }
    }

    //  maximum sort
    public void bubbleSort()
    {
        int out, in;

        //  outer loop (backward)
        for (out = nElemes-1; out > 1; out--)
        {
            //  inner loop (forward)
            for (in = 0; in < out; in++)
            {
                //  out of order?
                if (a[in] > a[in+1])
                {
                    //  swap them
                    swap(in, in+1);
                }
            }
        }   //  end bubbleSort()
    }
    public void swap(int one, int two)
    {
        long temp = a[one];
        a[one] = a[two];
        a[two] = temp;
    }
}   //  end class ArrayBub

//  demonstrates selection sort
class ArraySel
{
    //  ref to array a
    private long[] a;
    //  number of data items
    private int nElemes;

    //  constructor
    public ArraySel(int max)
    {
        //  create the array
        a = new long[max];
        //  no items yet
        nElemes = 0;
    }
    //  put element into array
    public void insert(long value)
    {
        //  insert it
        a[nElemes] = value;
        //  increment size
        nElemes += 1;
    }
    //  display array conetns
    public void display()
    {
        //  for each element
        for (int j = 0; j < nElemes; j++)
        {
            //  display it
            System.out.print(a[j] + " ");
        }
        System.out.println("");
    }

    //  minimum sort
    public void selectionSort()
    {
        int in, out, min;

        //  outer loop
        for (out = 0; out < nElemes-1; out++)
        {
            //  minimum
            min = out;
            //  inner loop
            for (in = out+1; in < nElemes; in++)
            {
                //  if min greater
                if (a[in] < a[min])
                {
                    //  we have a new min
                    min = in;
                }
            }
            //  swap them
            swap(out, min);
        }   //  end for(out)
    }   //  end selectionSort()

    public void swap(int one, int two)
    {
        long temp = a[one];
        a[one] = a[two];
        a[two] = temp;
    }
}   //  end class ArraySel

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

        //  array size
        int maxSize = 100;
        //  reference to array
        ArrayBub arr;
        //  create the array
        arr = new ArrayBub(maxSize);

        //  insert 10 items
        arr.insert(77);
        arr.insert(99);
        arr.insert(44);
        arr.insert(55);
        arr.insert(22);
        arr.insert(88);
        arr.insert(11);
        arr.insert(00);
        arr.insert(66);
        arr.insert(33);

        // display items
        arr.display();

        System.out.println("Bubble sort....");
        //  bubble sort them
        arr.bubbleSort();

        //  display them agin
        arr.display();

        System.out.println("searching for key 33 : " + arr.find(33));
        arr.delete(33);
        System.out.println("searching for key 33 : " + arr.find(33));        

        //  reference to array
        ArraySel arr2;
        //  reference to array
        arr2 = new ArraySel(maxSize);

        //  insert 10 items
        arr2.insert(77);
        arr2.insert(99);
        arr2.insert(44);
        arr2.insert(55);
        arr2.insert(22);
        arr2.insert(88);
        arr2.insert(11);
        arr2.insert(00);
        arr2.insert(66);
        arr2.insert(33);

        //  display items
        arr2.display();

        //  selection-sort them
        System.out.println("Selection sort....");
        arr2.selectionSort();

        //  display them again
        arr2.display();
    }   //  end main()
}