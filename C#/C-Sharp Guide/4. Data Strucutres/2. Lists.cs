using System;
using System.Collections.Generic;
using System.Linq;

namespace C_Sharp_Sandbox
{
    class Lists
    {
        static void Main(string[] args)
        {

            List<Car> myCars = new List<Car>(){
                new Car(){VIN = "A1", Make= "BMW", Model= "550i", Year = 2009, Price = 55000},
                new Car(){VIN = "B2", Make= "Toyota", Model= "4Runner", Year = 2010, Price = 35000},
                new Car(){VIN = "C3", Make= "BMW", Model= "745li", Year = 2008, Price = 75000},
                new Car(){VIN = "D4", Make= "Ford", Model= "Escape", Year = 2008, Price = 25000},
                new Car(){VIN = "E5", Make= "BMW", Model= "55i", Year = 2015, Price = 57000},
            };

            // LINQ query


            // First query 
            var BMWs = from car in myCars
                       where car.Make == "BMW"
                       select car;

            // Displaying results from query result variable BMWs
            foreach (var car in BMWs){
                Console.WriteLine($"{car.Model} {car.VIN}");
            }

            // Second query 
            var orderedCars = from car in myCars
                              orderby car.Year descending
                              select car;

            // Displaying results from query result variable BMWs
            foreach (var car in orderedCars){
                Console.WriteLine($"{car.Year} {car.Model}");
            }

            // Third query 
            var carPrices = from car in myCars
                            orderby car.Price descending
                            select car;

            // Displaying results from query result variable BMWs
            foreach (var car in carPrices){
                Console.WriteLine($"The {car.Make} {car.Model} will cost {car.Price:C}");
            }

            List<Todo> taskList = new List<Todo>() {
                new Todo{Description = "Task 1", EstimatedHours = 6, Status = Status.Completed},
                new Todo{Description = "Task 2", EstimatedHours = 2, Status = Status.Inprogress},
                new Todo{Description = "Task 3", EstimatedHours = 8, Status = Status.NotStarted},
                new Todo{Description = "Task 4", EstimatedHours = 12, Status = Status.Deleted},
                new Todo{Description = "Task 5", EstimatedHours = 6, Status = Status.Inprogress},
                new Todo{Description = "Task 6", EstimatedHours = 2, Status = Status.NotStarted},
                new Todo{Description = "Task 7", EstimatedHours = 14, Status = Status.NotStarted},
                new Todo{Description = "Task 8", EstimatedHours = 8, Status = Status.Completed},
                new Todo{Description = "Task 9", EstimatedHours = 8, Status = Status.Inprogress},
                new Todo{Description = "Task 10", EstimatedHours = 8, Status = Status.Completed},
                new Todo{Description = "Task 11", EstimatedHours = 4, Status = Status.NotStarted},
                new Todo{Description = "Task 12", EstimatedHours = 10, Status = Status.Completed},
                new Todo{Description = "Task 13", EstimatedHours = 12, Status = Status.Deleted},
                new Todo{Description = "Task 14", EstimatedHours = 6, Status = Status.Completed},
            };

            foreach (var todo in taskList) {
                switch (todo.Status) {
                    case Status.NotStarted:
                        Console.ForegroundColor = ConsoleColor.Red;
                        break;

                    case Status.Inprogress:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        break;

                    case Status.OnHold:
                        Console.ForegroundColor = ConsoleColor.Gray;
                        break;

                    case Status.Completed:
                        Console.ForegroundColor = ConsoleColor.Green;
                        break;

                    case Status.Deleted:
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        break;
                }
                Console.WriteLine(todo.Description);
            }
    }

    class Car{
        public string VIN { get; set; }
        public string Make { get; set; }
        public string Model { get; set; }
        public int Year { get; set; }
        public double Price { get; set; }
    }; 
}