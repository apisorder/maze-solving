
// Programmer:     Cheng, Jeff
// Last Modified:  06-21-2024 08:29PM
// Problem:        Java Tutorial 7

//  creating a new class to do this instead

public class JavaLessonSeven
{
    public static void main(String[] args)
    {
        Monster Frank = new Monster();
        Frank.name = "Frank";
        
        //  this would not work!
        // System.out.println(Frank.attack);
        System.out.println(Frank.name + " has an attack of " + Frank.getAttack());
    }
}