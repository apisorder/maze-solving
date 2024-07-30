
// Programmer:     Cheng, Jeff
// Last Modified:  06-13-2024 09:25PM
// Problem:        Java Tutorial 3

//  demonstrates array class with low-level interface
//  this is a tool
class LowArray
{
    //  reference to array a
    private long[] a;

    //  constructor
    public LowArray(int size)
    {   
        //  create array
        a = new long[size];
    }

    //  set value
    public void setElem(int index, long value)
    {
        a[index] = value;
    }
    
    //  get value
    public long getElem(int index)
    {
        return a[index];
    }
}   //  end class lowArray

//  demonstrates array class wsith high-level interface
class HighArray
{
    //  reference to array a
    private long[] a;
    //  number of data items 
    private int nElems;
    
    //  constructor
    public HighArray(int max)
    {
        //  create the array
        a = new long[max];
        nElems = 0;
    }

    //  looks through the array for the item whose key value was passed to it as an argument
    //  returns true or false, depending on whether it finds the item
    public boolean find(long searchKey)
    {
        int j;

        //  for each element
        for (j = 0; j < nElems; j++)
        {
            //  found item?
            if (a[j] == searchKey)
            {
                //  exit loop before end
                break;
            }
        }
        //  gone to end?
        if (j == nElems)
        {
            //  yes, can't find it
            return false;
        }
        else
        {
            //  no, found it
            return true;
        }
    }   //  end find()

    //  places a new data item in the next available space in the array
    //  a field named nElems keeps track of the number of array cells that are actually filled
    //  with data items
    public void insert(long value)
    {
        //  insert it
        a[nElems] = value;
        //  increment size
        nElems += 1;
    }

    //  searches for the element whose key value was passed to it as an argument and, when it finds the element,
    //  shifts all the elements in the higher index cells down one cell, thus writing over the deleted value
    //  it then decrements nElems
    public boolean delete(long value)
    {
        int j;
        //  look for it
        for (j = 0; j < nElems; j++)
        {
            if (value == a[j])
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
            //  move higher ones down
            for (int k = j; k < nElems-1; k++)
            {
                a[k] = a[k+1];
            }
            //  decrement size
            nElems -= 1;

            return true;
        }
    }   //  end delete()

    //  displays all the values stored in the array
    public void display()
    {
        //  for each element
        for (int j = 0; j <nElems; j++)
        {
            //  display it
            System.out.print(a[j] + " ");
        }
        System.out.println("");
    }
}   //  end class HighArray

//  this is the user of the tool
//  demonstrates how communication between classes and the divison of responsibility between clases are important OOP aspects 
public class JavaLessonThree 
{
    public static void main(String[] args)
    {
        int defaultValue = (int) (Math.random() * 50);
        System.out.println("Default value = : " + defaultValue);

        int randomNumber = (int) (Math.random() * 50);

        if (randomNumber < 25)
        {
            System.out.println("The random number is less than 25 : " + randomNumber);
        }
        else if (randomNumber == 25)
        {
            System.out.println("The random number is equal to 25 : " + randomNumber);
        }
        else
        {
            System.out.println("The random number is greater than 25 : " + randomNumber);
        }

        int biggestValue = (defaultValue > randomNumber) ? defaultValue: randomNumber;
        System.out.println("biggestValue : " + biggestValue);

        char theGrade = 'B';
        
        switch( theGrade )
        {
            case 'A':
                System.out.println("Marvelous!");
                break;
            case 'B':
                System.out.println("Outstanding");
                break;
            case 'C':
                System.out.println("Good");
                break;
            case 'D':
                System.out.println("....");
                break;
            default:
                System.out.println("See you next semester again.");
                break;
        }

        //  reference
        LowArray arr;
        //  create LowArray object
        arr = new LowArray(100);
        //  number of items in array
        int nElems = 0;
        //  loop variable
        int j;

        //  insert 10 items
        arr.setElem(0, 77);
        arr.setElem(1, 99);
        arr.setElem(2, 44);
        arr.setElem(3, 55);
        arr.setElem(4, 22);
        arr.setElem(5, 88);
        arr.setElem(6, 11);
        arr.setElem(7, 00);
        arr.setElem(8, 66);
        arr.setElem(9, 33);

        //  now 10 items in array
        nElems = 10;

        //  display items
        for (j = 0; j < nElems; j++)
        {
            System.out.print(arr.getElem(j) + " ");
        }
        System.out.println("");

        //  search for data item
        int searchKey = 26;
        //  for each element,
        for (j = 0; j < nElems; j++)
        {
            //  found item?
            if (arr.getElem(j) == searchKey)
            {
                break;
            }
        }
        //  no
        if (j == nElems)
        {
            System.out.println("Can't find " + searchKey);
        }
        //  yes
        else
        {
            System.out.println("Found " + searchKey);
        }

        //  delete value 55
        //  look for it
        for (j = 0; j < nElems; j++)
        {
            if (arr.getElem(j) == 55)
            {
                break;
            }
        }

        //  higher ones down
        for (int k = j; k < nElems-1; k++)
        {
            arr.setElem(k, arr.getElem(k+1));
        }
        //  decrement size
        nElems -= 1;

        //  display items
        for (j = 0; j < nElems; j++)
        {
            System.out.print( arr.getElem(j) + " ");
        }
        System.out.println("");

        //  array size for HiArray
        int maxSize = 100;
        //  reference to array
        HighArray arr1;
        //  create the array
        arr1 = new HighArray(maxSize);

        //  insert 10 items
        arr1.insert(77);
        arr1.insert(99);
        arr1.insert(44);
        arr1.insert(55);
        arr1.insert(22);
        arr1.insert(88);
        arr1.insert(11);
        arr1.insert(00);
        arr1.insert(66);
        arr1.insert(33);

        //  display items
        arr1.display();

        //  search for item
        searchKey = 35;
        if (arr1.find(searchKey))
        {
            System.out.println("Found " + searchKey);
        }
        else
        {
            System.out.println("Can't find " + searchKey);
        }

        //  delete 3 items
        arr1.delete(00);
        arr1.delete(55);
        arr1.delete(99);

        //  display items again
        arr1.display();
    }    // end main
}   //  end class
