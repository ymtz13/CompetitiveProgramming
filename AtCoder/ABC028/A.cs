using System;

class Program
{
	static void Main()
    {
    	int N = int.Parse(Console.ReadLine());
      	string ans = N<60 ? "Bad" : N<90 ? "Good" : N<100 ? "Great" : "Perfect";
        Console.WriteLine(ans);
    }

}
