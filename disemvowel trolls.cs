using System;

public static class Kata
{
    public static string Disemvowel(string str)
    {
        string vowels = "aeiouAEIOU";
        string result = "";
        foreach (char c in str)
        {
            if (!vowels.Contains(c))
            {
                result += c;
            }
        }
        return result;
    }
}