using System;

namespace C_Sharp_Sandbox
{
    class Program
    {
        static void Main(string[] args){
            // for
            int[] numbers = new int[] { 3, 14, 15, 92, 6 };

            for (int i = 0; i < numbers.Length; i++){
                Console.WriteLine(numbers[i]); // Will print each numbers in new lines
            }

            //foreach
            int[] numbers = new int[] { 3, 14, 15, 92, 6 };

            foreach (int number in numbers){
                Console.Write($"{number} "); // Will print each numbers
            }

            //while
            int[] numbers = new int[] { 3, 14, 15, 92, 6 };
            int n = 0;
            while (n < numbers.Length){
                Console.WriteLine(numbers[n]);
                n++;
            }

            //do - executed at least once, then the expression is evaluated after each execution of the loop.
            int[] numbers = new int[] { 3, 14, 15, 92, 6 };
            int n = 0;
            do{
                Console.WriteLine(numbers[n]);
                n++;
            } while (n < numbers.Length);           
        }
    }
}