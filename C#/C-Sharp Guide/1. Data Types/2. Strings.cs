using System;

namespace C_Sharp_Guide
{
    class Program
    {
        static void String()
        {
            // *----------------------------*
            //    ------ Common Use ------
            // *----------------------------*
            // A string is a collection of chracters, literally strung together.

            //This is a single line comment
            
            /* 
               This is a multi-line comment.
               If you need to express larger
               comments, you can do it this way 
            */

            /// XML comments start with three slashes and have a special syntax.
            /// <summary>Blep</summary>

            // Single-line string
            Console.WriteLine("This is a single line");

            //Single same line string
            Console.Write("Hey! ");
            Console.Write("Hello!"); // Write puts the output on the same line as the last output.

            // Multiple-line string (Verbatim string literal)
            Console.WriteLine(
                @"Line one
                line 2
                line 3");
            
            // String interpolation
            Console.WriteLine.(@"This will write // anything \\ at all. 
                                It ignores any special character rules for ~!#@$^* and takes
                                line breaks into consideration.")

            // User input
            Console.WriteLine("What is your name? ");
            string Name = Console.ReadLine(); // Prompts input. What you type will be assigned to the variable. 

            // Conversion (Type casting)
            Console.WriteLine("What is your age? ");
            int Age = Convert.ToInt32(Console.ReadLine()); 

            // Interpolation
            Console.WriteLine($"So, you're {Name} and {Age} years old?");

            // Concatination
            string First_Half = "Hello,";
            string Second_Half = "world!";

            string Result1 = $"{First_Half} {Second_Half}";

            // String Builder
            // Use the StringBuilder class to mitigate the problem.It stores the composed string in 
            // mutable memory during the process. When the string is ready, transfer it one time to the immutable string.

            using System.Text; // Must be at the proper using location, which is at the top of the document. 

            StringBuilder String_Builder_Example = new StringBuilder();

            String_Builder_Example.AppendLine("Line one");
            String_Builder_Example.AppendLine("Line two");
            String_Builder_Example.AppendLine("Line three");

            Console.WriteLine(String_Builder_Example.ToString());

            // Line Breaks
            Console.WriteLine("Line one" +
                              "\r\n" +
                              "Line two");

            Console.WriteLine("First line" +
                               Environment.NewLine +
                               "Second line");

            // Escape characters - Used to represent non-printable and special characters in string literals.
            /*             
                \ - escape character                
                \'	Single quotation mark
                \"	Double quotation mark
                \\	Backslash
                \?	Literal question mark 
                
                \a	Bell (alert)
                \b	Backspace
                \f	Form feed
            
                \t	Horizontal tab
                \v	Vertical tab
            
                \n	New line
                \r	Carriage return
            */

            
            // *-----------------------------------*
            //    ------ String Formatting ------
            // *-----------------------------------*
            // General format is {index[,alignment]:[format]}
            // Common types: G (General), F (FixedPoint), N (Number), D (Decimal), P (Percent), E (Exponential), C (Currency), 

            string Money = string.Format($"{123.45:C}"); // Outputs $123.45
            Console.WriteLine(Money);

            string Long_Number = string.Format($"{123456789:N}"); // Provides comma seperation and decimals. 
            Console.WriteLine(Long_Number);

            string Percent = string.Format($"{.123:P}"); // 12.30%
            Console.WriteLine(Percent);

            // Custom Format - https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings
            string Custom_String_Format = string.Format("{0:(###) ###-####}", 3861234567);
            Console.WriteLine(Custom_String_Format);

            // *------------------------*
            //    ------ Regex ------
            // *------------------------*


            // *----------------------------------*
            //    ------ Built-in Methods ------
            // *----------------------------------*

            // Email
            string email = "user@example.com";
            int indexOfAt = email.IndexOf('@');
            string domain = email.Substring(indexOfAt + 1);
            Console.ReadLine(domain);
             
            // String Alteration
            string Normal_Sentence = "Hello, I'm Paul!";
            string Loud_String = Normal_Sentence.ToUpper();
            Console.WriteLine(Loud_String);

            string Not_Paul = Normal_Sentence.Replace("Paul", "Timmy");
            Console.WriteLine(Not_Paul);

            // Data Cleaning
            string Extra = "    This has some extra spacing   ";
            string Cleaned = Extra.Trim();

            Console.WriteLine(Cleaned);

            // Table creation
            int[] Year = { 2013, 2014, 2015 };
            int[] Population = { 1025632, 1105967, 1148203 };
            var Population_Table = new System.Text.StringBuilder();

            Population_Table.Append(String.Format($"{"Year",5} {"Population",15}\n\n"));

            for (int index = 0; index < Year.Length; index++)
                Population_Table.Append(String.Format($"{Year[index],5} {Population[index],15:N0}\n"));

            Console.WriteLine(Population_Table);
        }
    }
}