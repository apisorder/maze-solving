
// Programmer:     Cheng, Jeff
// Last Modified:  06-14-2024 08:46PM
// Problem:        Java Tutorial 4 

import java.util.Scanner;

public class JavaLessonFour
{
    static Scanner userInput = new Scanner(System.in); 
    public static void main(String[] args)
    {
        int i = 1;

        System.out.println("Printing all 20 numbers");
        while ( i <= 20 )
        {
            System.out.println(i);
            i++;
        }

        //  reset i to 1
        i = 1;

        System.out.println("Printing all 20 numbers, except if i == 3, increment by 2, then continue");
        while ( i <= 20 )
        {
            if (i == 3)
            {
                i += 2;
                continue;
            }
            
            System.out.println(i);
            i++;            
        }

        //  reset i to 1
        i = 1;

        System.out.println("Add skipping even numbers to the above: if i % 2 == 0, then simply i++");
        while ( i <= 20 )
        {
            if (i == 3)
            {
                i += 2;
                continue;
            }
            
            System.out.println(i);
            i++;
            
            if((i%2) == 0)
            {
                i++;
            }
        }
        
        //  reset i to 1
        i = 1;

        System.out.println("Enable early termination where i > 10");
        while ( i <= 20 )
        {
            if (i == 3)
            {
                i += 2;
                continue;
            }
            
            System.out.println(i);
            i++;
            
            if((i%2) == 0)
            {
                i++;
            }

            if (i > 10)
            {
                break;
            }
        }

        double myPi = 4.0;
        double j = 3.0;
        //  4 - 4/3 + 4/5 - 4/7 + 4/9
        while (j < 11)
        {
            myPi = myPi - (4/j) + 4/(j+2);
            //  note it's incremented by 4
            j += 4;
        }
        System.out.println("My PI where j < 11= " + myPi);

        //  resetting myPi and j
        myPi = 4.0;
        j = 3.0;
        while (j < 8001)
        {
            myPi = myPi - (4/j) + 4/(j+2);
            //  note it's incremented by 4
            j += 4;
        }
        System.out.println("My PI where j < 8001 = " + myPi);

        //  resetting myPi and j
        myPi = 4.0;
        j = 3.0;
        while (j < 1000001)
        {
            myPi = myPi - (4/j) + 4/(j+2);
            //  note it's incremented by 4
            j += 4;
        }
        System.out.println("My PI where j < 1000001= " + myPi);

        String contYorN = "Y";
        int h = 1;

        while (contYorN.equalsIgnoreCase("y"))
        {
            System.out.println(h);
            System.out.print("Continue: y or n ? ");
            contYorN = userInput.nextLine(); 
            h += 1;
        }

        int k = 10;

        //  do-while loop
        do
        {
            System.out.println("k = " + k);
            k += 1;
        }
        while (k < 10);

        //  for (declare iterator; conditional statement; change iterator)
        for (int l = 10; l >= 1; l--)
        {
            System.out.println(l);
        }
    }
}
