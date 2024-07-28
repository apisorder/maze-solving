
// Programmer:     Cheng, Jeff
// Last Modified:  06-13-2024 09:25PM
// Problem:        Java Tutorial 3

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
    }    
}
