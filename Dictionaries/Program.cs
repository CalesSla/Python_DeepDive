

using System.Text;
using System.Text.RegularExpressions;

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, Bitches, enter your string!");

var test1 = GetFirstInput();
var test2 = GetSecondInput();
var test3 = GetThirdInput();

Console.WriteLine($"result for {test1} is : \n  {GetStringWithoutBrekets(test1)} \n");
Console.WriteLine($"result for {test2} is : \n  {GetStringWithoutBrekets(test2)} \n");
Console.WriteLine($"result for {test3} is : \n  {GetStringWithoutBrekets(test3)} \n");


var request = Console.ReadLine();

if(!IsValid(request))
{
    Console.WriteLine("Неа, херня это, проверь условие");
    Console.ReadKey();
    return;
}

request = ReplaceWhitespace(request);

// 0 layer = (x*y)
// max layer = ((()...)

var response = GetStringWithoutBrekets(request);

Console.WriteLine($"Response is : {response}");

Console.ReadKey();

// Возвращает результат с расчитанными скобками
static string GetStringWithoutBrekets(string input)
{
    if (!IsValid(input))
        return input;

    var chars = input.ToCharArray();
    var iO = 0;
    var iC = 0;

    for(int i =0; i < chars.Length; i++)
    {
        var c = chars[i];

        if (c == '(')
        {
            iO = i;
        }

        if (c == ')')
        {
            iC = i;

            var cInp = input.Substring(iO, (iC + 1 - iO));
            var calcResult = Calc(cInp).ToString();
            var newString = input.Replace(cInp, calcResult);

            return GetStringWithoutBrekets(newString);
        }
    }

    //if(input.Any(c => c == '('))
    //    return GetStringWithoutBrekets(input);

    return input;
    
}

static double Calc(string input)
{
    return CalcPlus(input);
   // return input.Sum(x => x);
}


static double CalcPlus(string input)
{
    double r = 0;

    var digits = input.Replace("(", "").Replace(")", "").Split('+');
    for (int i = 0; i < digits.Length; i++)
    {
        var d = digits[i];
        if (d == "+")
            continue;

        r += double.Parse(d);
    }

    return r;
}



static string ReplaceWhitespace(string input)
{
    Regex sWhitespace = new Regex(@"\s+");
    return sWhitespace.Replace(input, "");
}


static bool IsValid(string input)
{
    if(string.IsNullOrEmpty(input))
        return false;

    var countOpen = input.Count(s => s == '(');
    var countClose = input.Count(s => s == ')');

    if (countOpen != countClose)
        return false;

    return true;
}

static string GetFirstInput()
{
    return "((2+2) + 2)";
}

static string GetSecondInput()
{
    return "(2+2) + (3+3)";
}

static string GetThirdInput()
{
    return "(((2+2) + (2+1) + 3) + 2) + 1";
}
