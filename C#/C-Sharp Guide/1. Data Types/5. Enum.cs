using System;

namespace C_Sharp_Sandbox
{
    // https://www.dotnetperls.com/enum
    //Enums in C# are used to represent a set of constants as integral values. Think of them a semantic way of expressing constants for a group of closely related items. 
    // Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc. Or even ordinal data types.

    // WeekDay – Mon, Tue, Wed, Thu, Fri, Sat, Sun
    // Months – Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
    // Rectangle – Left, Top, Bottom, Right
    // Point – X, Y

    enum WeekDays {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
    }    

    class Program
    {
        static void Main(string[] args)
        {
            WeekDays First_Day = WeekDays.Monday; // Setting a variable 


            Console.WriteLine(WeekDays.Monday);     // Monday
            Console.WriteLine(WeekDays.Tuesday);    // Tuesday
            Console.WriteLine(WeekDays.Wednesday);  // Wednesday
            Console.WriteLine(WeekDays.Thursday);   // Thursday
            Console.WriteLine(WeekDays.Friday);     // Friday
            Console.WriteLine(WeekDays.Saturday);   // Saturday
            Console.WriteLine(WeekDays.Sunday);     // Sunday
        }
    }
}