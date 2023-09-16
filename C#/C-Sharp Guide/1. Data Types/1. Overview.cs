using System;

namespace Sandbox
{
    class Experiment
    {
        static void Main(string[] args)
        {
            //Variables

            // Variable Syntax - C# variables are strongly typed
            //Data_Type Variable_Name = Value;

            cosnt string Name = "Alexander"; // Constants don't change

            string Name = "Alexander";
            int Number = 357;
            double Decimal = 5.99D;
            decimal Pi = 3.14m;
            char Letter = 'D';
            bool Condition = true;
            var General = "Something general."


            /*
            *----------------------------------*
               ---- Assignment Operators ----
            *----------------------------------*
            Addition:       x + 2   same as x+=2
            Subtraction:    x - 2   same as x-=2
            Multiplication: x * 2   same as x*=2
            Division:       x / 2   same as x/=2
            Floor Division: x // 2  same as x//=2
            Exponent:       x ** 2  same as **=2
            Modulus:        x % 2   same as x%=2
            */

            // * -------------------*
            //     ---- Enums----
            // * -------------------*
            // Basically a variable that can only be one of a set of values - Great for data validation


            // *---------------------------*
            //     ------ Strings ------
            // *----------------------------*

            //Must use single quotes
            Char SingleChar = 'K'; // Represents a single 16-bit Unicode code point
            Char UnicodeChar = '\u00A7';

            // Must use double quotes
            String Name = "Felix Roswell"; // Name[] internalChars = {'F','e','l','i','x',' ','R','o','s','w','e','l','l',} (This is how strings are literally strung together.)

            // *---------------------------*
            //     ------ Numbers ------
            // *----------------------------*
            sbyte Small_Byte = 42;                      // -128 to 127
            byte Byte_Number = 123;                     // 0 to 255

            short Short_Number = 9001;                  // -32,767 to 32,767
            ushort Unsigned_Short_Number = 1234;        // 0 to 65,535

            int Int_Number = 123456789;                 // -2,147,483,648 to 2,147,483,647
            uint Unsigned_Int_Number = 145755;          // 0 to 4,294,967,295

            long Long_Number = 14685392833524L;         // -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
            ulong Unsigned_Long_Number = 71254763289    // 0 to 18,446,744,073,709,551,615


            float Floating_Number = 3.14f;
            double Double_Number = 6.28d;
            decimal Decimal_Number = 0.999m;


            // *--------------------------*
            //     ------ Boolean ------
            // *---------------------------*
            bool True_Statement = true;
            bool False_Statement = false;

            // *------------------------*
            //     ------ Dates ------
            // *------------------------*
            DateTime My_Birthday = new DateTime(1994, 7, 5);


            // *-----------------------*
            //     ------ Enum ------
            // *-----------------------*

            enum Level {
                Low,
                Medium,
                High
            }

            // Enum in a class
            Level myVar = Level.Medium;
            Console.WriteLine(myVar);

            class Program {
                enum Level {
                    Low,
                    Medium,
                    High
                }

                static void Main(string[] args)
                {
                    Level myVar = Level.Medium;
                    Console.WriteLine(myVar);
                }
            }

            /* 
              Converting (Type Casting)

              int myInt = 10;
              double myDouble = 5.25;
              bool myBool = true;

              Console.WriteLine(Convert.ToString(myInt));    // Convert int to string
              Console.WriteLine(Convert.ToDouble(myInt));    // Convert int to double
              Console.WriteLine(Convert.ToInt32(myDouble));  // Convert double to int
              Console.WriteLine(Convert.ToString(myBool));   // Convert bool to string
           */
         }
    }
}