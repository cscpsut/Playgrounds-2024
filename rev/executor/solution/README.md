First run the command file to check what type of files is this:
```bash
$ file executor.exe 
executor.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows, 3 sections
```
then we can use ILSPY to get the source code. To reverse the operations we are going to put an additional line to the source code and use online C# compiler to run it. Here is the code after modification:

```C#
using System;
using System.Linq;

public static class Program
{
    public static void Main(string[] args)
    {


    string text = "u4_3r1_433h23C3syl5p_x_1";
    if (text.Length != 24)
    {
        Console.WriteLine("Nope.");
        return;
    }
    string first = "u4_3r1_433h23C3syl5p_x_l";
    char[] array = new char[24];
    int num = 7312;
    for (int i = 0; i < 24; i++)
    {
        num = (51 * num + 42) % 24;
        while (array[num] != 0)
        {
            num = (num + 1) % 24;
        }
        array[num] = text[i];
        Console.Write(first[num]);
    }
    if (first.SequenceEqual(array))
    {
        Console.WriteLine("Correct!");
        Console.WriteLine("Take Your Flag Now: ");
        Console.WriteLine("PlaygroundsCTF{" + text + "}");
    }
    else
    {
        Console.WriteLine("Nope.");
    }
    }
}
```

Running this will give u the flag!.
