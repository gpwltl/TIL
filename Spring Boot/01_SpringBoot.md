# Spring Boot

단독실행 가능하고, 제품 수준의 스프링 기반 어플리케이션을 제작하는데 목표로 진행된 프로젝트

> 주요 기능

- 단독 실행이 가능한 수준
- **내장된 Tomcat**, Jetty, UnderTow 등의 서버를 포함하여 별도의 서버를 설치하지 않고 실행 가능함
- 최대한 내부적으로 **자동화된 설정을 제공**
- xml 설정 없이 단순한 설정 방식 제공
- war 안해도되고 **jar**로도 가능



## 1. 스프링부트 시작하기

### 1) 프로젝트 구조

![image](https://user-images.githubusercontent.com/44856614/93169579-5ac4f600-f760-11ea-9da9-b9a007eaf5f0.png)

- src/main/java  : 자바 Source 파일들
  - 만들자마자 생성된 com.gpwltl.myspringboot 패키지 속 MyspringbootApplication.java 파일에 `@SpringBootApplication` 어노테이션을 내부에 선언함
    -> 디폴트 패키지에 위치해야 함
- src/main/resources/application.properties : 스프링부트 프로퍼티 값들 모아 놓은 파일
- src/main/resources/static  : html, css 같은 정적 파일들
- src/main/resources/templates  : jsp, thymeleaf 같은 동적 파일들
- src/test/java  : 자바 테스트 파일들



### 2) 실행

- 프로젝트 실행 :  우클릭 -> Run As -> Spring Boot App
- 포트번호 변경 : src/main/resources/application.properties에서 `server.port=8086` 으로 포트번호 변경



## 2. 스프링부트 원리

### 1. 자동 설정

`@SpringBootApplication` 
= @SpringBootConfiguration + @ComponentScan + @EnableAutoConfiguration

1. **@ComponentScan** : 프로젝트 생성시 정해준 default 패키지부터 아래 패키지까지 찾아서, 
    @Repository, @Configuration, @Service 들을 스프링 bean으로 등록하는 기능
2. **@EnableAutoConfiguration**  : 스프링 bean들을 자동적으로 컨테이너에 등록하는 기능 (기본적으로 웹 프로젝트로 만들 수 있는 기본값 설정되어 있음)

![image](https://user-images.githubusercontent.com/44856614/93181544-8ac9c480-f773-11ea-86cf-7288e89661dc.png)

- SERVLET : Default / MVC가 존재하면 Servlet으로 동작 (웹 어플리케이션 타입 지정)
- REACTIVE : Webflux가 존재하면 reactive로 동작
- NONE : 둘다 없으면 none으로 동작 -> 일반 프로젝트 용도로 사용할 때 사용 (웹 어플리케이션 프로젝트(x) )

