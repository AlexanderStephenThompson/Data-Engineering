using System;

namespace C_Sharp_Sandbox
{
    class Program
    {
        static void Main(string[] args)
        {
            // if else
            int number = 5;
            bool condition = number > 10;
            bool condition2 = number < 10 && number > 3;

            if (condition)
            {
                Console.WriteLine("Number is greater than 10");
            }
            else if (condition2)
            {
                Console.WriteLine("Number is between 4 and 10"); // In this case this line will be printed
            }
            else
            {
                Console.WriteLine("Number is not smaller than 3");
            }


            // Switch case
            int number = 1;

            switch (number)
            {
                case 1:
                    Console.WriteLine("Case 1"); // In this case this line will be printed
                    break;
                case 2:
                    Console.WriteLine("Case 2");
                    break;
                default:
                    Console.WriteLine("Default case");
                    break;
            }
        }
    }
}