using System;

namespace FirstProject
{
    class Program
    {
        static void Main(string[] args)
        {
            int First_Number = 3;
            int Second_Number = 5;

            // Comparison Operators
            Console.WriteLine(First_Number == Second_Number);   // Equals to
            Console.WriteLine(First_Number === Second_Number);  // Equals to and same type
            Console.WriteLine(First_Number != Second_Number);   // Not equals to
            Console.WriteLine(First_Number > Second_Number);    // Greater than
            Console.WriteLine(First_Number >= Second_Number);   // Greater than or equal to
            Console.WriteLine(First_Number < Second_Number);    // Less than
            Console.WriteLine(First_Number <= Second_Number);   // Less than or equal to

            /*
                Logical operators - Used to join two or more statements

                &&	logical and
                ||	logical or
                !	logical not - Asks if a statement is not true.
            */

            Console.WriteLine(First_Number != Second_Number && Second_Number == 5);     // Condition 1 AND condition 2
            Console.WriteLine(First_Number = Second_Number || Second_Number <= 5);      // Condition 1 OR condition 2
            Console.WriteLine(!(Second_Number == 5);                                    // NOT condition 1
        }
    }
}



