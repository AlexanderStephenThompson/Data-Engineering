using System;

namespace C_Sharp_Sandbox
{
    class Program {
        static void Main(string[] args)
        {

            Chef chef = new Chef();
            chef.MakeChicken();
            chef.MakeSpecial();

            Italian_Chef italianChef = new Italian_Chef();
            italianChef.MakeChicken();
            italianChef.MakePasta();
            italianChef.MakeSpecial();

        }

    }
    // Super/Parent class
    class Chef{
        public void MakeChicken() {
            Console.WriteLine("The chef made a chicken");
        }

        public void MakeSalad() {
            Console.WriteLine("The chef made a salad");
        }
        
        // Virtual enables the function to be overwritten in subclasses.
        public virtual void MakeSpecial() {
            Console.WriteLine("The chef made super toast");
        }
    }

    class Italian_Chef : Chef {
        public void MakePasta(){
            Console.WriteLine("The italian chef made PASTA");
        }

        // Override overrides the inherited functionality
        public override void MakeSpecial() {
            Console.WriteLine("The chef made super pasta");
        }
    }
}