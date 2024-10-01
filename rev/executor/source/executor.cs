using System;
using System.Linq;

public static class Program
{
	public static void Main(string[] args)
	{
		if (args.Length != 1)
		{
			Console.WriteLine("Usage: ./execuror.exe <flag>");
			return;
		}
		string text = args[0];
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