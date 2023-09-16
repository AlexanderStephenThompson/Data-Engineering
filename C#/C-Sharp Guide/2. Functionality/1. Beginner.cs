using System;

namespace Exam_1
{
   
    class Program
    {
        /*
            Function Syntax

            <Access Specifier> static <return type> <name of the function>(<data type> <function parameter>) {
                <function code>
                [return];
            }
       
           Access modifier determines where the function can be accessed and how. This will be revisited in classes. 

           Static just means this function doesn't depend on an object to complete its instructions either through appending functionality onto objects (Object.methodName()) when called or referencing objects while the function is being created (If the parameters are empty).

           Return type - A return statement allows us to take a value of a variable within a function and enable it to be accessed at a different scope of the program. Having a data type listed instead tells C# we do intend to have something returned as a result of the executed function. Void means we don't intend to return anything, probably just printing out a value instead. 
       */


        // *------------------------*
        //    ---- Common Use ----
        // *------------------------*
        public static void Greeting() {
            Console.WriteLine("Hello!");
        }
        // Calling: Greeting();

        /// <summary> You get a special greeting, you should feel special
        /// 
        /// <list type="bullet">
        /// <item>
        /// <description>Item 1.</description>
        /// </item>
        /// <item>
        /// <description>Item 2.</description>
        /// </item>
        /// </list>
        /// 
        /// </summary>
        /// 
        /// <example><code>Custom_Greeting("Timmy")</code></example>
        /// 
        /// <returns>A very nice message</returns>
        /// <param name='name'>This is where you put your beautiful name.</param>
        public static void Custom_Greeting(string name) {
            Console.WriteLine($"Hello {name}");
        }
        // Calling: Custom_Greeting("Timmy");


        public static void Input_Greeting() {
            Console.WriteLine("What is your name?");
            string Name = Console.ReadLine();

            Console.WriteLine($"Hey, {Name}!");
        } //Calling: Input_Greeting();


        // *-----------------------------*
        //    ---- Error Handling ----
        // *-----------------------------*
        public static void ErrorDemo() {

            int SomeNumber = 100;
            int Zero = 0;
            int Result;

            try {
                if (SomeNumber > 1000) {
                    throw new ArgumentOutOfRangeException("SomeNumber","The number can't be larger than 1000");
                }

                Result = SomeNumber / Zero;
                Console.WriteLine($"The result is {Result}");
            }
            catch (DivideByZeroException ZeroError) {
                Console.WriteLine("Can't divide by zero!");
                Console.WriteLine(ZeroError.Message);
            }
            catch (ArgumentOutOfRangeException OutOfRange) {
                Console.WriteLine("The number can't be larger than 1000.");
                Console.WriteLine(OutOfRange.Message);
            }
            finally {
                Console.WriteLine("This will always execute.");
            }
        }

        // *--------------------------*
        //    ---- Unit Testing ----
        // *--------------------------*


        // *--------------------*
        //    ---- Events ----
        // *--------------------*


        // *------------------------*
        //    ---- Decorators ----
        // *------------------------*


        // *-----------------------*
        //    ---- Callbacks ----
        // *-----------------------*


        // *------------------------*
        //    ---- Delegation ----
        // *------------------------*


        // *---------------------*
        //    ---- Lambdas ----
        // *---------------------*


        // *----------------------------*
        //    ---- Multithreading ----
        // *----------------------------*
    }
    static void Main(string[] args) {

            // Common Use
            Greeting();
            Custom_Greeting("Timmy");
            Input_Greeting();
        


        }      
    }
}
