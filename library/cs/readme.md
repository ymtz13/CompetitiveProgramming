# C#チートシート

```
int X = int.Parse(Console.ReadLine()); // 1個

// using. System.Linq; が必要
List<int> X = Console.ReadLine().Split(' ').Select(int.Parse).ToList(); // 複数（空白区切り）
```

```
List<int> X = new List<int>{1, 2, 3, 4, 5};
Console.WriteLine(string.Join(", ", X)); // "1, 2, 3, 4, 5"

int X = 'Hello, World!'
Console.WriteLine($"{X,  20}"); # 20桁、右寄せ
Console.WriteLine($"{X, -20}"); # 20桁、左寄せ
```
