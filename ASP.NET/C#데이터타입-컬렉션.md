# C#

## 자료형(Data Type)과 리스트

- 기본 자료형 : int, string, double, long, float

- 사용자 정의 : class(객체)

- 리스트 : `List\<T>();` 제네릭 리스트

```c#
var list = List<T>();
list.Add(new User{Name="", Birth="..."})
```

> **리스트**
>
> 1. Non-Generic-collection
>    - ArrayList
>    - SortedList
>    - HashTable
>    - BitArray
>    - Queue
>    - Stack
>
> 2. Generic-collection
>    - **List\<User>**

<br/>

## :seedling: 기본 형식(정리)

- List를 선언하기  `List<데이터형식> List이름 = new List<데이터형식>();`

- List에 element(요소) 추가하기  `List이름.Add(element);`

- List에 element 삽입하기  `List이름.Insert(삽입할 위치, element);`

- List에 element 제거하기 `List이름.RemoveAt(제거할 위치);`

- List에 들어있는 요소의 수 `List이름.Count`

- List 비우기 `List이름.Clear`



## :seedling: Loops

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
    List<int> list = new List<int>();
    list.Add(2);
		list.Add(3);
		list.Add(7);
    
    //Loop throught List with foreach
    foreach(int number in list)
    {
      Console.WriteLine(number);
    }
    
    //Loop with for
    for (int i=0; i<list.Count; i++)
    {
      Console.WriteLine(list[i]);
    }
  }
}
```



## :seedling: Copy array to List

생성자를 이용해서 만든 배열의 요소를 List에 매개변수로 전달하여 복사할 수 있다. 

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
    int[] arr = new int[3];
    arr[0]=2;
    arr[1]=3;
    arr[2]=5;
    
    //Copy to List
    List<int> list = new List<int>(arr);
  }
}
```



## :seedling: Find Element

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
    List<int> primes = new List<int>(new int[] {2,3,4});
    
    //See if List contains 3
    foreach(int nubmer in primes)
    {
      if(number==3)
      {
        Console.WriteLine("Contains 3");
      }
    }
  }
}
```



## :seedling: Join String List 

String.Join을 이용하여 단어 사이에 ',' 가 찍히는 문자열을 만들 수 있다. 

- List에서 문자열을 추출할 땐, `ToArray`를 이용할 것

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
    List<string> cities = new List<string>();
    cities.Add('New York');
    cities.Add('Mumbai');
    cities.Add('Berlin');
    cities.Add('Istanbul');
    
    //Join strings into one CSV line
    string line = string.Join(",", cities.ToArray());
    Console.WriteLine(line);
  }
}
```



## :seedling: Get List from keys in dictionary

key들의 값을 얻어낼 List를 생성하여 `.Keys`를 통해 Enumerable을 반환받을 수 있다. 

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
   	var dict = new Dictionary<int, bool>();
    //Dictionary<int, bool> dict = new Dictionary<int, bool>(); 와 동일한 표현
    dict.Add(3, true);
    dict.Add(6, false);
    
    //Get a List of all the Keys
    List<int> keys = new List<int>(dict.Keys);
    
    foreach(int key in keys)
    {
      Console.WriteLine(key);
    }
  }
}
```



## :seedling: Get range of Element

`GetRange` 메소드 이용하여 범위안의 요소를 추출할 수 있다. 

```c#
using System;
using System.Collections.Generic;

class Program
{
  static void Main()
  {
   	List<string> rivers = new List<string>(new string[]{
      'nile',
      'amazon',
      'yangtze',
      'mississippi',
      'yellow'
    });
    
    List<string> range = rivers.GetRange(1, 2);
    foreach(string river in range)
    {
      Console.WriteLine(river);	//amazon 	//yangtze
    }
  }
}
```

