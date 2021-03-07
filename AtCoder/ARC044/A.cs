using System;

class Program
{
    static bool Solve(long N) {
        if(N==1) return false;
            
        var isPrime = true;
        for(int p=2; p*p<=N && isPrime; ++p) {
            if(N%p==0) isPrime = false;
        }
        if(isPrime) return true;
        return N%2!=0 && N%3!=0 && N%5!=0;
    }
    
    static public void Main() {
        var N = long.Parse(Console.ReadLine());
        Console.WriteLine(Solve(N) ? "Prime" : "Not Prime");
    }
}
