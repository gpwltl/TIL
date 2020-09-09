# MyBatis

## 1. MyBatis란?

> 객체지향 언어인 자바의 관계형 데이터베이스 프로그래밍을 좀더 쉽게 할 수 있게 도와주는 개발 프레임워크

- SQL을 자바 코드에서 분리하여 xml 파일에 따로 관리
  (**객체-SQL 사이의 파라미터 매핑작업**을 자동화)

- **개발자가 익숙한 SQL을 그래도 이용하면서** JDBC 코드 작성의 불편함도 제거해줌 
- 도메인 객체나 VO 객체 중심으로 개발 가능함



#### 특징

- 쉬운 접근성과 코드의 간결함
- SQL문과 프로그래밍 코드의 분리
  - sql에 변경있어도 자바 코드를 수정하거나 컴파일 하지 않아도 됨
- 다양한 프로그래밍 언어로 구현 가능



## 2. MyBatis 구조

> 구성 요소

| 구성요소/파일                                      | 설명                                                         |
| -------------------------------------------------- | ------------------------------------------------------------ |
| MyBatis configuration file                         | Mybatis의 작업 설정을 설명하는 xml파일<br />(데이터베이스의 연결 대상, 매핑 파일의 경로, 작업 설정 등) |
| org.apache.ibatis.session.SqlSessionFactoryBuilder | Mybatis 구성 파일을 읽고 생성하는 `SqlSessionFactory` 구성 요소 |
| org.apache.ibatis.session.SqlSessionFactory        | `SqlSession`을 생성하는 구성 요소                            |
| org.apache.ibatis.session.SqlSession               | Sql 실행 및 트랜잭션 제어를 위한 qpi를 제공하는 구성 요소<br />(Mybatis와 데이터베이스가 액세스할 때 중요한 역할) |
| Mapper interface                                   | 매핑 파일에 정의된 sql을 호출하는 인터페이스<br />(mapper 인터페이스의 구현 클래스는 자동생성되어 개발자는 인터페이스만 생성) |
| Mapping file                                       | sql 및 o/r 매핑 설정을 설명하는 xml 파일                     |



> 주요 컴포넌트 역할

- `설정파일` SqlMapConfig.xml  데이터베이스의 접속 주소 정보나 Mapping 파일의 경로 등의 고정된 환경정보 설정
- `SqlSessionFactoryBuilder`  설정 파일을 바탕으로 SqlSessionFactory를 생성
- `SqlSessionFactory`  SqlSession을 생성
- `SqlSession`  핵심적인 역할을 하는 클래스.  스레드마다 필요에 따라 생성함
   Thread-safe (x)
- `mapping 파일`user.xml  Sql문과 OR Mapping을 설정



> 구조& 데이터베이스에 액세스하는 흐름

![image-20200909153815773](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200909153815773.png)

> Processing to run once (응용 프로그램 시작시)
>
> > 어플리케이션이 컴파일 시 스프링에서 MyBatis의 빈 생성

(1) 응용 프로그램은 SqlSessionFactoryBuilder에 대한 `SqlSessionFactory 빌드를 요청함`

(2) SqlSessionFactoryBuilder는 SqlSessionFactory 생성을 위한 `MyBatis 구성 파일을 읽음`

(3) SqlSessionFactoryBuilder는 MyBatis 구성 파일 설정 기반으로 `SqlSessionFactory를 생성`



> Processing to run per requests (클라이언트의 요청에 대해)
>
> > 어플리케이션 내에서 개발자가 구현한 사용자의 데이터 요청 

(4) 클라이언트가 응용 프로그램에 대한 `프로세스를 요청`

(5) 응용 프로그램은 SqlSessionFactoryBuilder를 사용해 `빌드된 SqlSessionFactory에서 SqlSession을 가져옴`

(6) SqlSessionFactory는 `SqlSession을 생성`하고 `애플리케이션에 반환`

(7) 응용 프로그램이 `SqlSession에서 매퍼 인터페이스 구현 개체 가져옴`

(8) 응용 프로그램이 `매퍼 인터페이스 메서드 호출`

(9) 매퍼 인터페이스의 구현 개체가 `SqlSession 메서드를 호출`하고 `sql을 실행 요청함`

(10) SqlSession은 `매핑 파일에서 실행할 sql을 가져와 sql을 실행함`



## 3. MyBatis-Spring

> 주요 컴포넌트 역할

- `설정파일`SqlMapConfig.xml  VO 객체의 정보를 설정함
- `SqlSessionFactoryBean`  
  - 설정파일을 바탕으로 SqlSessionFactory를 생성함
  - Spring Bean으로 등록해야 함
- `SqlSessionTemplate  `
  - 핵심역할 하는 클래스. 트랜잭션 관리 실행
  - SqlSession 인터페이스 구현. Thread-safe
  - Spring Bean으로 등록해야 함
- `Mapping파일` UserMapper.xml  Sql문과 OR Mapping을 설정
- `Spring Bean 설정파일` beans.xml  
  - 빈 등록시 DataSource나 config파일 정보, mapping 파일의 정보를 함께 함
  - SqlSessionTemplate을 Bean으로 등록



> 구조

![image-20200909221239819](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200909221239819.png)



### #resultMap

> MyBatis xml 파일에 쿼리 작성하면, 쿼리 결과가 pojo클래스에 자동으로 바인딩됨
>
> -> VO 클래스의 코드량이 줄어들고 깔끔하게 관리 가능
> -> 객체 혹은 List 속성으로 가지기에 의미 전달도 훨씬 잘 됨

- 테이블 간 관계가 1:1 `Association`
- 테이블 간 관계가 1:N 인 경우 `collection`





## 4. Mapper 인터페이스

> Mapping 파일에 기재된 sql을 호출하기 위한 인터페이스

- Mapper 인터페이스는 sql을 호출하는 프로그램을 Type Safe하게 기술하기 위해 등장
- Mapping 파일에 있는 sql을 자바 인터페이스를 통해 호출 가능케 함



> Mapper 사용 이유

![image-20200909221812323](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200909221812323.png)

- Mapper 사용하지 않을 경우, SqlSession 메서드의 아규먼트에 문자열을 `namespace.sql_id` 형식으로 지정해야 함
- 오타가 있을 때 무조건 에러를 발생시켜 문제



![image-20200909221756358](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200909221756358.png)

- UserMapper 인터페이스는 개발자가 작성
- `패키지명.인터페이스명.메서드명`을 네임스페이스.sql_id가 되도록 네임스페이스와 Sql의 ID를 설정해야 함
  - 네임스페이스엔 패키지 포함한 Mapper 인터페이스 이름이어야 
  - Sql ID에는 매핑하는 메서드 이름 지정

