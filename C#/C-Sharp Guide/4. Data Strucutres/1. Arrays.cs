using System;

namespace C_Sharp_Sandbox
{
    class Program
    {
        static void Main(string[] args)
        {
            // One dimensional 

                // Declare and define later
                string[] Names = new string[3];
                Names[0] = "Jack";
                Names[1] = "Manuka";
                Names[2] = "Lennox";

                Console.WriteLine(Names[1]); // Writes Mankua

                // Immediate declaration and definition
                string[] More_Names = new string[4] { "Rufus", "Fiona", "Ezra", "Laura" };

                // Alternative syntax.
                string[] Even_More_Names = { "Kira", "Zell", "Brutus", "Kaiser" };

                // Reading data with loops
                string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };

                Console.WriteLine(cars[0]); // Outputs Volvo

                // Outputs all of the cars in the array
                foreach (string car in cars) {
                    Console.WriteLine(car);
                }

                Console.WriteLine(cars.Length); // Counts how many items are in the array. Outputs 4


                // Checking if a value is in an array
                /*Make sure to add 
                using System.Linq;
                */

                string[] printer = { "jupiter", "neptune", "pangea", "mercury", "sonic" };
                if (printer.Contains("jupiter")) // Or some variable
                {
                    // Code to be executed
                }


                // Multidimensional (Rectangular arrays)

                // ~~ Two Dimensions ~~

                // Two-dimensional array.
                var Character_Details = new string[4, 2] {
                        // Name,  Age
                        {"Rufus", "25"},
                        {"Laura", "28"},
                        {"Ezra", "30"},
                        {"Fiona", "26"}
                };

                Console.WriteLine(Character_Details[1, 0]); //Laura

                int[,] array2D = new int[,] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };

                // The same array with dimensions specified.

                int[,] array2Da = new int[4, 2] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };

                // A similar array with string elements.
                string[,] array2Db = new string[3, 2] { { "one", "two" }, { "three", "four" }, { "five", "six" } };

                int[,] a = new int[3, 4]
                {
                    {0, 1, 2, 3},   /*  initializers for row indexed by 0 */
                    {4, 5, 6, 7},   /*  initializers for row indexed by 1 */
                    {8, 9, 10, 11}   /*  initializers for row indexed by 2 */
                 };

                //Accessing
                int val = a[2, 3];

            // ~~ Three Dimensions ~~

                // Three-dimensional array.
                int[,,] array3D = new int[,,]
                {
                    { { 1, 2, 3 }, { 4, 5, 6 } },
                    { { 7, 8, 9 }, { 10, 11, 12 } }
                };

                // The same array with dimensions specified.
                int[,,] array3Da = new int[2, 2, 3]
                {
                    { { 1, 2, 3 }, { 4, 5, 6 } },
                    { { 7, 8, 9 }, { 10, 11, 12 } }
                };


            // Jagged Arrays - similar to multidimensional ones, but all elements of this array can have different dimensions and sizes.

                // Declare a jagged array
                int[][] jaggedArray = new int[6][];

                // Set the values of the first array in the jagged array structure
                jaggedArray[0] = new int[4] { 1, 2, 3, 4 };

        }
    }
}