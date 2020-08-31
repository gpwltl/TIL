# Java

## 0. java 시작 전

#### 1) jdk vs jre

- jdk: java developmentkit -for developer (jdk가 jre를 포함)
- jre: java run time enviroment -for user

java는 platfor이 독립적 
.java-> .class(byte code) -> assembly code

#### 2) j2se vs j2ee

j2se- stand alone application , java core, i/o,

j2ee- server based web application



## 1. java 기초

> src 아래 많은 파일이 존재할 것
>
> > 이때 패키지별로 .java파일들을 묶어주는 것이 좋다. 
> > 파일명이 같아도 패키지명이 다르면 사용 가능하기에 보기 쉽게 정리가 된다. 

##### 1) 이름 설정

- 클래스명은 대문자로 시작
- 패키지명은 소문자로 구성
- 메서드명과 변수명은 소문자로 시작
- 메서드명이나 변수명에서 단어가 바뀌면 바뀌는 첫글자는 대문자로 한다. (camel case)
  - getMethod() (o) / getmethod() (x)



##### 2) 주석

- // 한 줄 주석

- /*

   \* 여러줄 주석

   */



## 2. 데이터 타입

### 1. Primitive Data Type

- 정수형 : `byte`, `short`, `int`, `long`
  - 값 범위 : 1   2   4   8 byte
  - default : 0   0   0   0L
  - 정수형 literal의 데이터 타입은` int형`
- 실수형 : `float` , `double` 
  - 값 범위 : 4   8 byte
  - default : 0.0F    0.0D
  - 실수형 literal의 데이터 타입은 `double형`
- 문자형 : `char` 
  - 값 범위 : 16bit uni-code문자  '\u0000' (default)
- 논리형 : `boolean` 
  - 값 범위 : true / false(default)



### 2. Reference Data Type

> Primitive Data Type 제외한 모든 것

- 객체에 대한 주소 값(reference)

  - 객체의 생성은 new로 이루어지며, 객체의 데이터 타입은 그 객체의 클래스로 표현

    `Students s = new Students();`

- 객체 생성시, 메모리 할당 순서

  1) 메모리 할당(reference 변수, 객체)

  2) 객체의 멤버 변수 초기화

  ​		(1) default value로 초기화

  ​		(2) 명시적 초기화

  ​    	(3) Constructor에 의한 초기화

  3) 객체의 주소 값이 reference 변수에 할당



## 3. this

> this는 자기자신의 객체를 가리킨다.
>
> > - this.멤버변수 : 자기자신의 멤버변수 참조
> > - this.멤버메소드 : 자기자신의 멤버메소드 참조
> > - this(파라미터_리스트) : 자기자신의 생성자 호출

``` java
public class MyDate{
    private int year=2000;
    private int month=1;
    private int day=1;
    
	public MyDate(int year, int month, int day){
        this.year=year;
        this.month=month;
        this.day=day;
    }
}
```



## 4. Pass by value

> 메소드 호출 시, parameter로 넘겨지는 값은 
>
> > - Primitive data type : 실제 값 (변수 자체가 아니다.)
> > - Reference data type : 객체의 주소 값 (객체 자체가 아니다.)



### 1. Primitive type

```java
public class PassPrimitive{
    public void passValue(){
        int num=10;
        change(num);
        System.out.println(num);
    }
    public void change(int num){
        num=num+10;
    }
    public static void main(String[] args){
        PassPrimitive pp = new PassPrimitive();
        pp.passValue();
    }
}
```



### 2. Reference type

```java
//1. MyDate 클래스
public class MyDate{
    private int year;
    private int month;
    private int day;
    
    public MyDate(int year, int month, int day){
        this.year=year;
        this.month=month;
        this.day=day;
    }
    
    public int getYear(){
        return year
    }
    public void setYear(int year){
        this.year=year;
    }
    
    public int getMonth(){
        return year
    }
    public void setMonth(int month){
        this.month=month;
    }
    
    public int getDay(){
        return year
    }
    public void setDay(int day){
        this.day=day;
    }
}
```

```java
//2. TestMyDate 클래스(메인)
public class TestMyDate{
    public static void main(String [] args){
        MyDate today = new MyDate(1974,7,22);
        TestMyDate test = new TestMyDate();
        
        today.setDay(30);
        test.print(today);
    }
    public void print(MyDate day){
        System.out.println("The Day is "+day.getDay()+"-"+day.getMonth()+"-"+day.getYear());
    }
}
```

