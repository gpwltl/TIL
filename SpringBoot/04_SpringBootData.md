# SpringBoot Data

## 0. In-Memory DB

NoSQL방식에 속하는 데이터베이스로 key-value 방식을 사용 

- Memory 가격이 용량 대비 빠른 데이터베이스 성능을 가짐
- 디스크 대신 메모리를 사용하여 I/O의 성능을 높여줌
- H2, HSQL, Derby 지원



## 1. H2 데이터베이스

*콘솔기능을 제공하기 때문에 추천* :star:

1. h2 의존성 추가 

```xml
<dependency>
 	<groupId>com.h2database</groupId>
 	<artifactId>h2</artifactId>
	<scope>runtime</scope>
</dependency>
```

2. H2 데이터베이스 기본 연결 정보 확인

DBRunner.java 파일을 통해 해당 DBURL과 DB Username을 파악한다. 

```java
logger.debug("DB URL=> " + dbMeta.getURL());
logger.debug("DB Username=> " + dbMeta.getUserName());
```

3. h2 console 사용 

브라우저에서  http://localhost:8086/h2-console 에 접속하여 위에서 나온 url과 username을 입력하고 connect하면 성공
(단, 포트번호는 현재 부트를 돌리고 있는 포트번호이어야 함)

4. 테이블 생성하고 데이터 추가해보기 

![image-20200916180500972](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200916180500972.png)





## 2. Maria 데이터베이스 :star2:

*현재 실습하고 있는 데이터베이스*

1. Mysql 의존성 추가

```xml
<dependency>  
    <groupId>mysql</groupId>  
    <artifactId>mysql-connector-java</artifactId>  
    <version>8.0.13</version> 
</dependency>
```

2. Maria DB 접속

```mysql
mysql -u root –p 
show databases; 
use mysql; 
create user spring@localhost identified by 'spring'; #spring 계정 생성(id,pw 암기)
grant all on *.* to spring@localhost; 
flush privileges; 
exit; 
 
mysql -u spring -p 
create database spring_db; 
show databases; 
use spring_db; 
```

3. MySQL 데이터소스 설정 (DB 연결)

*src/main/resources/application.properties 에 입력해줌*

```properties
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/spring_db?useUnicode=true&charaterEncoding=utf-8&useSSL=false&serverTimezone=UTC 
spring.datasource.username=spring 
spring.datasource.password=spring
spring.datasource.driverClassName=com.mysql.cj.jdbc.Driver
```



## 3. Spring-Data-JPA

JPA를 쉽게 사용하기 위해 스프링에서 제공하는 프레임워크

- Repository Bean을 자동 생성
- 쿼리 메소드 자동 구현
- @EnableJpaRepositories을 부트가 자동으로 설정해줌



1. 의존성 추가

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>     		
	<artifactId>spring-boot-starter-data-jpa</artifactId> 
</dependency> 
```

2. **Entity 클래스 작성**

- `@Entity` : DB 테이블과 매핑하는 **객체**를 나타냄 

- `@Id` : 엔티티의 **기본키**를 나타냄

- `@GenerateValue`  : 주 **키의 값을 자동생성**하기 위해 명시하는데 사용

  - AUTO
  - IDENTITY -maria에서 확인시 추천
  - SEQUENCE -oracle에서 확인시 추천
  - TABLE

  

3. Repository 인터페이스 작성

AccountRepository.java를 확인해보면 따로 구현체를 작성하지 않아도 된다. spring-data-jpa가 자동적으로 해당 문자열을 username에 대한 인수를 받아 자동적으로 db table과 매핑하기 때문이다.  

```java
import java.util.Optional; 

public interface AccountRepository extends JpaRepository<Account, Long>{     
    Account findByUsername(String username); 	//(1)
    Optional<Account> findByEmail(String email);	//(2)
} 
```

*id 값이 Long으로 주어졌기 때문에 <Account, **Long**> 확인할 것*

- (1)은 기본적으로 username으로 조회하기 위해 사용
- (2)은 Optional을 이용해 반복적인 null 체크를 줄이기 위해 사용



4. jpa 사용한 데이터베이스 초기화

*src/main/resources/application.properties 에 입력해줌*

```properties
spring.jpa.show-sql=true	//(1)
spring.jpa.hibernate.ddl-auto=update	//(2)
```

(1) show-sql의 경우 jpa가 생성한 sql문을 보여줄 지 대한 여부 알려주는 프로퍼티

(2) ddl-auto의 경우 4가지로 나뉠 수 있음

- create : 기존에 있는 테이블 삭제하고 새로 만들겠다. 
- create-drop : jpa 종료 시점에 기존에 있었던 테이블 삭제
- update : 기존 스키마 유지, 새로운 것만 추가하고, 기존 데이터도 유지 (변경부분만 반영)  :+1:개발mode 
- validate : 엔티티와 테이블이 정상 매핑되어 있는지 검증  :+1:운영mode



5. AccountRepositoryTest 파일 생성해서 테스트하기

(Test 파일은 @RunWith(SpringRunner.class)  @SpringBootTest 로 시작!!)

- 객체 생성& 등록

![image-20200916195121287](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200916195121287.png)

- 객체 업데이트

![image-20200916195812348](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200916195812348.png)

- 객체 찾기 find

![image-20200916201423847](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200916201423847.png)

1) userName으로 find

2) id로 find -> optional.get() 이용

3) email로 find -> optional.orElseThrow() 이용

4) 전체 조회



6. 컬럼을 추가하고 싶다면 validate 속성 테스트를 이용한다. 

   -> validate는 테이블과 엔티티가 정상 매핑하지 않으면 에러를 발생하니 주의할 것!



---

### :ballot_box_with_check: Optional 관련

반복적인 null 체크를 줄이기 위해 사용함

#### 1. get() 관련

- `.get()`의 경우 결과값이 null일 때, 알아서 NoSuchElementException 발생

  ```java
  repository.findById(100L).get();
  ```

- `orElseThrow()`는 값이 없을 경우 예외를 던져주거나 orElse, orElseGet을 이용해 값을 지정

  ```java
  repository.findByEmail("dooly@aa.com").orElseThrow(() -> new RuntimeException("요청한 이메일 주소를 가진 Account가 없음!!"));
  ```



#### 2. Optional에서 값 바로 받기

Repository에서 Optional을 반환하는 경우, 원하는 값이 있으면 원하는 객체로 받고 `없으면 Exception처리`하는 패턴

```java
Optional<Account> optional = repository.findById(100L);
if(optional.isPresent()) {
	Account account2 = optional.get();
}
```



#### 3. ifPresent()

```java
Optional<Account> optional = repository.findById(100L);		System.out.println("optional.isPresent()>>>"+optional.isPresent()); //값이 존재하면 true, 아니면 false
```

