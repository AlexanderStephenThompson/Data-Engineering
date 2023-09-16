using System;
using System.Collection.Generics; //Step 1

namespace C_Sharp_Sandbox
{
    class Dictionaries
    {

        // Step 2 - Create the dictionary
        // Syntax: Dictionary<data type, data type> Dictionary_Name = new Dictionary<data type, data type>();

        Dictionary<string, string> Classes = new Dictionary<string, string>();

        // Step 3 - Add records to your dictionary
        // Syntax: Dictionary_Name.Add(key, value);

        // Creating a dictionary 
        // using Dictionary<TKey,TValue> class 
        Dictionary<string, string> Courses = new Dictionary<string, string>();

        // Adding key/value pairs  
        // in the Dictionary 
        // Using Add() method 
        Courses.Add("CTS1851", "Internet Web Foundation");
        Courses.Add("CGS2820", "Web Programming");
        Courses.Add("CGS2821", "Advanced Web Programming");
        Courses.Add("COP2361", "C# Programming");

        foreach (KeyValuePair<string, string> course in Courses){
            Console.WriteLine($"{course.Key} is {course.Value}");
        }


    static void Main(string[] args)
        {
            //Step 4 - Access using loops or the index. 

            // Loops

            // For loop
            for (int x = 0; i < Classes.Count; x++) {
                Console.WriteLine("{0} and {1}", Classes.Keys.ElementAt(x), My_dict1[My_dict1.Keys.ElementAt(x)]);
            }

        }
    }
}