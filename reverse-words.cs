using System;

public static class Kata
{
    public static string ReverseWords(string str)
    {
        string[] words = str.Split(' ');

        // Reverse each word in the array
        for (int i = 0; i < words.Length; i++)
        {
            char[] charArray = words[i].ToCharArray();
            Array.Reverse(charArray);
            words[i] = new string(charArray);
        }

        // Join the reversed words back into a string
        string result = string.Join(" ", words);
        return result;
    }
}