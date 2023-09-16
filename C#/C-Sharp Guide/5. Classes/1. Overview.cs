using Microsoft.VisualBasic.CompilerServices;
using System;
using System.Globalization;

namespace C_Sharp_Guide
{
    /* 
     
    -- Access Modifers --
        public: Whatever you're modifying with the access modifier can be accessed by any other code in the same assembly or another assembly that references it.
        private: Can only be seen within the class. The type or member can be accessed only by code in the same class or struct.
        protected: The type or member can be accessed only by code in the same class, or in a class that is derived from that class.

    -- Calling --
        Object Creation:    ClassName ObjectName = new ClassName(First_Attribute, Second_Attribute, Third_Attribute )
        Class Method:       ClassName.ClassMethodName()
        Static Method:      ClassName.StaticMethodName()
        Object Method:      ObjectName.ObjectMethodName() 
        Object Attribute:   ObjectName.Attribute
    
    public class Class_Name
    {
        public static int Object_Count = 0;

        // ~~~~~ Blueprint Attribute Parameters ~~~~~
        private string First_Attribute { get; set; }
        private string Second_Attribute { get; set; }
        private string Third_Attribute { get; set; }

        // ~~~~~ Constructor ~~~~~ - Special method defining the attributes of each object
        public Class_Name(string First_Attribute, string Second_Attribute, string Third_Attribute) {
            this.First_Attribute = First_Attribute; // Usually some identifier
            this.Second_Attribute = Second_Attribute;
            this.Third_Attribute = Third_Attribute;

            Object_Count += 1;
        }
        // Object Creation: Class_Name Instance_Name = new Class_Name("First value", "Second value", "Third value");

        // ~~~~~ Class Methods ~~~~~ - Working with class variables of the class
        public static void Total_Object_Count() {
            Console.WriteLine($"There are {Class_Name.Object_Count} members in this class_name class.");
        }

        // ~~~~~ Object Methods ~~~~~ - Working with objects of the class, often interacting with its attributes in some way
        public void Self_Reflection() {
            Console.WriteLine($"{First_Attribute} has {Second_Attribute} and {Third_Attribute}.");
        }

        // ~~~~~ Static Methods ~~~~~ - Close to a normal method, but not targeting self or class. 
        // This gives us a way to gain access to a method without creating an object first.
        public static void Class_Description() {
            Console.WriteLine("This is the character class. You can make characters!");
        }
    }

    */


    public class Character{
        public static int Number_Of_Characters = 0;

        // ~~~~~ Blueprint Attribute Parameters ~~~~~
        public string First_Name { get; set; } // Get and set methods to manipulate object attributes as needed. 
        public string Last_Name { get; set; }
        public string Species { get; set; }
        public float Height { get; set; }
        public string Gender { get; set; }

        // ~~~~~ Constructor ~~~~~ - Special method defining the attributes of each object
        public Character(string First_Name, string Last_Name, string Species, float Height, string Gender) {
            this.First_Name = First_Name;
            this.Last_Name = Last_Name;
            this.Species = Species;
            this.Height = Height;
            this.Gender = Gender;

            Number_Of_Characters += 1;
        }

        // ~~~~~ Class Methods ~~~~~ - Working with class variables of the class
        public static void Character_Count() {
            Console.WriteLine($"There are {Character.Number_Of_Characters} in this character class.");
        }

        // ~~~~~ Object Methods ~~~~~ - Working with objects of the class
        public void Greeting() {
            Console.WriteLine($"Hey, I'm {First_Name} and I'm a {Species}!");
        }

        // ~~~~~ Static Methods ~~~~~ - Close to a normal method, but not targeting self or class. 
        // This gives us a way to gain access to a method without creating an object first.
        public static void Class_Description() {
            Console.WriteLine("This is the character class. You can make characters!");
        }

    }
    

    public class Program
    {
        public static void Main(string[] args)
        {
            // *----------------------------*
            //    ------ Characters ------
            // *----------------------------*

            //Object Creation
            Character Fiona = new Character("Fiona", "Valentine", "Otter", 8.8f, "Female");
            Character Felix = new Character("Felix", "Roswell", "Zebra", 6.0f, "Male");

            // Object Method
            Fiona.Greeting();

            // Static Method
            Character.Class_Description();

            // Class Method
            Character.Character_Count();

            // Object Attribute
            Console.WriteLine(Fiona.First_Name)

        }
    }
}