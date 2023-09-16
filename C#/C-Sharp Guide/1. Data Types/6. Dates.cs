using Microsoft.VisualBasic.CompilerServices;
using System;

namespace C_Sharp_Guide {
    class Program {
        static void Main(string[] args)
        {
            // Date-times
            DateTime Some_DateTime = new DateTime(2017, 10, 18, 9, 51, 32);
            Some_DateTime.AddMinutes(134);
            Console.WriteLine(Some_DateTime);

            // Dates
            DateTime Current_DateTime = DateTime.Now;
            Console.WriteLine(Current_DateTime.ToString());

            Console.WriteLine(Current_DateTime.ToShortDateString());
            Console.WriteLine(Current_DateTime.ToLongDateString());

            Console.WriteLine(Current_DateTime.ToShortTimeString());
            Console.WriteLine(Current_DateTime.ToLongTimeString());

            Console.WriteLine(Current_DateTime.AddDays(3).ToLongDateString()); // Three days from now. 
            Console.WriteLine(Current_DateTime.AddDays(-3).ToLongDateString()); // Three days before now. 

            DateTime My_Birthday = new DateTime(1994, 7, 5);
            Console.WriteLine(My_Birthday.ToShortDateString());
        }
    }
}

