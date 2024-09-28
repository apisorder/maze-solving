
// Programmer:     Cheng, Jeff
// Last Modified:  09-21-2024 08:07PM
// Problem:        Java Tutorial 7 (Monster Class)

//  video game
//  public classes can be used by other classes
//  a file can't contain more than one public classes

import java.util.Arrays;

public class MonsterTwo
{
    static char[][] battleBoard = new char[10][10];

    public static void buildBattleBoard()
    {
        for (char[] row : battleBoard)
        {

        }
    }

    public final String TOMBSTONE = "Here lies a Dead Monster.";
    
    //  use as many private fields as possible
    private int health = 500;
    private int attack = 20;
    //  some sort of grid-based system
    private int movement = 2;
    private int xPosition = 0;
    private int yPosition = 0;
    private boolean alive = true;

    //  use as few public fields as possible
    public String name = "Big Monster";

    //  accessor methods
    public int getAttack() { return attack; }
    public int getHealth() { return health; }
    public int getMovement() { return movement; }
    
    public void setHealth(int decreaseHealth)
    {
        health -= decreaseHealth;
        if (health < 0)
        {
            alive = false;
        }
    }

    //  overloaded method
    //  same name but different attributes, the only way to overload
    public void setHealth(double decreaseHealth)
    {
        int intDecreaseHealth = (int) decreaseHealth;
        health -= intDecreaseHealth;
        if (health < 0)
        {
            alive = false;
        }
    }
    public MonsterTwo(int newHealth)
    {
        health = newHealth;
    }

    //  a construtor cannot have a return value of any type
    public MonsterTwo(int newHealth, int attack, int newMovement)
    {
        this(newHealth);
        this.attack = attack;
        movement = newMovement;
    }   

    //  Default Constructor
    //  also provided by the Java interpreter if no constructors 
    //  have been defined
    //  overloading the constructor
    //  existing but does nothing
    public MonsterTwo()
    {

    }

    //  this is the wrong way!
    //  it allows access to the private field!!!! 
    //  (since we are inside the class)
    // public static void main(String[] args)
    // {
    //     Monster Frank = new Monster();
    //     System.out.println(Frank.attack);
    // }
}

