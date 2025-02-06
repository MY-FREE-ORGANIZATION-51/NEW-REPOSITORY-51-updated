using System;

class Program {
    static void Main() {
        Console.WriteLine(Greet("World"));
    }

    static string Greet(string name) {
        return $"Hello, {name}!";
    }
}
