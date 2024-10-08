
// Programmer:     Cheng, Jeff
// Last Modified:  09-21-2024 08:07PM
// Problem:        Java Tutorial 8

import org.apache.commons.lang3.ArrayUtils;
import java.util.Arrays;

public class MonsterTwo
{
    //  create our gameboard
    static char[][] battleBoard = new char[10][10];

    public static void buildBattleBoard()
    {
        //  temp holding cell for all the stars
        //  individual cells individual stars which go into the cells
        for (char[] row : battleBoard)
		{
            Arrays.fill(row, '*');
		}	
	}
	
    public static void redrawBoard()
	{
        //  print the top line
        int k = 1;
        while (k <= 30)
        {
            System.out.print('-');
            k++;
        }
		System.out.println();
		
        for (int i = 0; i < battleBoard.length; i ++)
		{
            for (int j = 0; j < battleBoard[i].length; j++)
			{
				System.out.print("|" + battleBoard[i][j] + "|");
			}
			System.out.println();
		}

        //  print the bottom line
		k = 1;
		while(k <= 30)
        { 
            System.out.print('-'); 
            k++; 
        }
		System.out.println();
	}
	
	public final String TOMBSTONE = "Here Lies a Dead monster";
	
	// private fields are not visible outside of the class
	private int health = 500;
	private int attack = 20;
	private int movement = 2;
	
	private boolean alive = true;
	
	// public variables are visible outside of the class
	// You should have as few as possible public fields
	public String name = "Big Monster";
    //  default to be big monster
    //  because all of the monsters are represented by a single letter
	public char nameChar1 = 'B';

    //  these private fields have to be changed to public
	public int xPosition = 0;
	public int yPosition = 0;
	public static int numOfMonsters = 0;
	
	// Class Methods
	// Accessor Methods are used to get and set the values of private fields
	
	public int getAttack()
	{
		return attack;
	}
	
	public int getMovement()
	{
		return movement;
	}
	
	public int getHealth()
	{
		return health;
	}
	
	public boolean getAlive()
	{
		return alive;
	}
	
	// You can create multiple versions using the same method name
	// Now setHealth can except an attack that contains decimals
	// When overloading a method you can't just change the return type
	// Focus on creating methods that except different parameters
	
	public void setHealth(int decreaseHealth)
	{
		health = health - decreaseHealth;
		if (health < 0)
		{
			alive = false;
		}
	}
	
	public void setHealth(double decreaseHealth)
	{
		int intDecreaseHealth = (int) decreaseHealth;
		health = health - intDecreaseHealth;
		if (health < 0)
		{
			alive = false;
		}
	}
	
	/* The Constructor
	 * Code that is executed when an object is created from this class definition
	 * The method name is the same as the class
	 * The constructor is only executed once per object
	 * The constructor can't return a value
	 */
	public MonsterTwo(int health, int attack, int movement, String name)
	{
		this.health = health;
		this.attack = attack;
		this.movement = movement;
		this.name = name;
		
        //  x and y for the model board for the monster
        //  maximum horizontally (rows)
		int maxXBoardSpace = battleBoard.length - 1;
        //  maximum vertically (columns)
		int maxYBoardSpace = battleBoard[0].length - 1;
		
        //  random number of generated thing that is gonna like where 
        //  everything begins
		int randNumX, randNumY;
		
		do 
        {			
			randNumX = (int) (Math.random() * maxXBoardSpace);
			randNumY = (int) (Math.random() * maxYBoardSpace);
		} 
        //  only allow the monster to go on a space which currently has a *
        while( battleBoard[randNumX][randNumY] != '*' );
		
		this.xPosition = randNumX;
		this.yPosition = randNumY;
		
		this.nameChar1 = name.charAt(0);
		
		battleBoard[this.yPosition][this.xPosition] = this.nameChar1;
		
		numOfMonsters++;
		
	}
	
	// You can overload constructors like any other method
	// The following constructor is the one provided by default if you don't create any other constructors
	// Default Constructor
	
	public MonsterTwo()
	{
		numOfMonsters++;
	}
	
public static void main(String[] args)
{
	
	
}
	
}