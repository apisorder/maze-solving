
// Programmer:     Cheng, Jeff
// Last Modified:  05-31-2024 08:47AM
// Problem:        Java Tutorial 2

import java.util.Scanner;

//  demonstrates Java arrays
//  name of the class == name of the file
public class JavaLessonTwo
{
    //  any time you want to create a scanner object, you must use the keyword new and scanner, always
    //  and then the input stream you want the scanner object to look at
    //  System.in == user's keyboard
    static Scanner userInput = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.print("Your favorite number : ");

        if (userInput.hasNextInt())
        {
            //  string == nextLine()
            int numberEntered = userInput.nextInt();
            System.out.println("int numberEntered = " + numberEntered);
            
            //  alternatively, int numberEntered2 *= numberEntered;
            int numberEntered2 = numberEntered *2;
            System.out.println(numberEntered + " + " + numberEntered + " = " + Math.abs(numberEntered2));
            System.out.println("number entered vs number entered*2 (which is bigger) : " + Math.max(numberEntered2, numberEntered));
        }
        else
        {
            System.out.println("Enter an integer next time");
            //  Math.ceil returns a float automatically

            double numberEntered = 12.13;

            if (userInput.hasNextDouble())
            {
                numberEntered = userInput.nextDouble();
            }
        
            int numCeil = (int) Math.ceil(numberEntered);
            System.out.println("numbered entered (forced) = " + numCeil);
        }

        System.out.println("Enter a number for the upperbound to generate a random number : ");
        if (userInput.hasNextInt())
        {
            System.out.println("Some random number based on the number you entered as upperbound : " + Math.random()*(userInput.nextInt()+1));
        }
        else
        {
            System.out.println("Some random number between (0 and 10) : " + Math.random()*11);
        }
        /*
         *  multi-line comment
         */

         // reference to array
         // alternative syntax: long arr[], but placing the [] after the long makes it clear that the [] is part of the type. 
         long[] arr = new long[100];
         // number of items
         int nElems = 0;
         // loop counter
         int j;
         // key of tiem to search for
         long searchKey;

         // insert 10 items
         arr[0] = 77;
         arr[1] = 99;
         arr[2] = 44;
         arr[3] = 55;
         arr[4] = 22;
         arr[5] = 88;
         arr[6] = 11;
         arr[7] = 00;
         arr[8] = 66;
         arr[9] = 33;

         // now 10 items in array
         nElems = 10;

         // display items
         for (j = 0; j < nElems; j++)
         {
            System.out.print(arr[j] + " ");
         }
         System.out.println("");

         // find itme with key 66
         searchKey = 66;

         // for each element
         for (j = 0; j < nElems; j++)
         {
            //  found item?
            if (arr[j] == searchKey)
            {
                //  yes, exit before end
                break;              
            }
         }

        //  at the end?
        if (j == nElems)
        {
            //  yes
            System.out.println("Can't find " + searchKey);
        }
        else
        {
            //  no
            System.out.println("Found " + searchKey);
        }
         
         // delete item with key 55
         searchKey = 55;
         for (j = 0; j < nElems; j++)
         {
            //  look for it
            if (arr[j] == searchKey)
            {
                break;
            }
         }

         //  move higher ones down
        for (int k = j; k < nElems-1; k++)
        {
            System.out.println("k = " + k);
            System.out.println("arr[k] = " + arr[k]);
            System.out.println("arr[k+1] = " + arr[k+1]);

            arr[k] = arr[k+1];
        }
        //  decrement size
        nElems -= 1;

        //  display items
        for (j = 0; j < nElems; j++)
        {
            System.out.print( arr[j] + " ");
        }
        System.out.println("");
    //  end main()
    }
//  end class
}