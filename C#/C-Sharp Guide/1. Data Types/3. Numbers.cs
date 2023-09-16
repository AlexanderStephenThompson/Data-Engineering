using Microsoft.VisualBasic.CompilerServices;
using System;

namespace C_Sharp_Guide
{
    class Program
    {
        static void Main(string[] args)
        {

            /* 
                *--------------------------*
                |                          |
                |    ~~~~ Numeric ~~~~     |
                |                          |
                *--------------------------*

                
                *--------------------------------------*
                   ------ Arithmetic Operators ------
                *--------------------------------------*
                https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/arithmetic-operators
                Rules of operation apply.

                Addition:       3 + 2
                Subtraction:    3 - 2
                Multiplication: 3 * 2
                Division:       3 / 2
                Floor Division: 3 // 2
                Exponent:       3 ** 2
                Modulus:        3 % 2

                *------------------------------------------------*
                   ------  Increment/Decrement Operators ------
                *------------------------------------------------*
                Good for loops

                
                Pre-increment: ++$Number: Increments Number by one, then returns the updated Number value.
                Post-increment: $Number++: Returns the orginal Number value, then increments the Number by one.

                Pre-decrement: --$Number: Decreases Number by one, then returns the updated Number value.
                Post-decrement: $Number--: Returns the orginal Number value, then decrements the Number by one.

            */


            // *------------------------------------*
            //   ------ Numeric Data Types ------
            // *------------------------------------*


            // *---------------*
            //    - Integer -
            // *---------------*
            byte Byte_Number = 123; // 0 to 255
            Console.WriteLine(Byte_Number);

            short Short_Number = 9001; // -32,767 to 32,767
            Console.WriteLine(Short_Number);

            int Int_Number = 123456789; // -2,147,483,648 to 2,147,483,647
            Console.WriteLine(Int_Number);

            long Long_Number = 14685392833524; // -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
            Console.WriteLine(Long_Number);


            // *----------------*
            //    - Decimals -
            // *----------------*
            float Floating_Number = 3.14f;
            Console.WriteLine(Floating_Number);

            double Double_Number = 6.28d;
            Console.WriteLine(Double_Number);

            decimal Decimal_Number = 0.999m;
            Console.WriteLine(Decimal_Number);

            // *--------------------------*
            //    ------ Operations ------
            // *--------------------------*
            int First_Number = 3;
            int Second_Number = 2;

            //Operator Examples
            Console.WriteLine(First_Number + Second_Number);
            Console.WriteLine(First_Number - Second_Number);
            Console.WriteLine(First_Number * Second_Number);
            Console.WriteLine(First_Number / Second_Number);
            Console.WriteLine(First_Number % Second_Number);


            // *-------------------------------------*
            //    ------ Increment/Decrement ------
            // *-------------------------------------*
            Console.WriteLine(--First_Number);
            Console.WriteLine(++First_Number);
            Console.WriteLine(Second_Number--);
            Console.WriteLine(Second_Number++);


            // *------------------------------------*
            //    ------Built -in Functions------
            // *------------------------------------*

        }
    }
}
