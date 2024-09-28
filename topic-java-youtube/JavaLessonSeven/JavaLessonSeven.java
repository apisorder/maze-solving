
// Programmer:     Cheng, Jeff
// Last Modified:  09-21-2024 08:07PM
// Problem:        Java Tutorial 7

//  creating a new class to do this instead

public class JavaLessonSeven
{
    public static void main(String[] args)
    {
        Monster Frank = new Monster();
        Frank.name = "Frank";
        
        //  this would not work!
        //  ok to access private fields within the class itself
        //  trying to access private fields out of the class 
        // System.out.println(Frank.attack);
        System.out.println(Frank.name + " has an attack of " + Frank.getAttack());
    }
}