
// Programmer:     Cheng, Jeff
// Last Modified:  06-14-2024 08:46PM
// Problem:        Java Tutorial 4 

import java.util.Scanner;

//  demonstrates ordered array class
class  OrdArray
{
    //  reference to arrfay a
    private long[] a;
    //  number of data items
    private int nElems;

    //  constructor
    public OrdArray(int max)
    {
        //  create array
        a = new long[max];
        nElems = 0;
    }

    public int size()
    {
        return nElems;
    }

    //  the major advantage is that search times are much faster than in an unordered array
    public int find(long searchKey)
    {
        int lowerBound = 0;
        int upperBound = nElems-1;
        int curIn;

        while (true)
        {
            curIn = (lowerBound + upperBound)/2;
            if (a[curIn] == searchKey)
            {
                //  found it
                return curIn;
            }
            else if (lowerBound > upperBound)
            {
                //  can't find it
                return nElems;
            }
            else
            //  divide range
            {
                if (a[curIn] < searchKey)
                //   it's in upper half
                {
                    lowerBound = curIn + 1;
                }
                else
                //  it's in lower half
                {
                    upperBound = curIn - 1;
                }
            }   //  end else divide range
        }   //  end while
    }   //  end find()

    //  put element into array
    //  disadvantage:   insertion takes longer because all the data items with a higher key value must be moved up to make room.
    public void insert(long value)
    {
        int j;
        //  find where it goes
        for (j = 0; j < nElems; j++)
        {
            //  linear search
            if (a[j] > value)
            {
                break;
            }
        }
        //  move bigger ones up
        for (int k = nElems; k > j; k--)
        {
            a[k] = a[k-1];
        }
        //  insert it
        a[j] = value;
        //  increment size
        nElems += 1;
    }   //  end insert()

    public boolean delete(long value)
    {
        int j = find(value);
        //  can't find it
        if (j == nElems)
        {
            return false;
        }
        else
        {
            //  move bigger ones down
            for (int k = j; k < nElems; k++)
            {
                a[k] = a[k+1];
            }
            //  decrement size
            nElems -= 1;
            return true;
        }
    }   //  end delete()

    //  display array contents
    public void display()
    {
        //  for each element
        for (int j = 0; j < nElems; j++)
        {
            //  display it
            System.out.print(a[j] + " ");
        }
        System.out.println("");
    }
}

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

        //  array size
        int maxSize = 100;
        //  reference to array
        OrdArray arr;
        //  create the array
        arr = new OrdArray(maxSize);

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

        //  search for item
        int searchKey = 55;
        if (arr.find(searchKey) != arr.size())
        {
            System.out.println("Found " + searchKey);
        }
        else
        {
            System.out.println("Can't find " + searchKey);
        }

        //  display items
        arr.display();


        //  delete 3 items
        arr.delete(00);
        arr.delete(55);
        arr.delete(99);

        //  display items again
        arr.display();
    }   //  end main()
}
