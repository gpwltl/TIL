# Rest

## 0. Open API 이란?

**프로그래밍에서 사용할 수 있는 개방되어 있는 상태의 인터페이스** 

<small> *API란? 응용 프로그램을 개발할 때 사용하는 인터페이스 </small>

- 포털사이트, 통계청, 기상청 등 관공서에서 가지고 있는 데이터를 외부 응용 프로그램에서 사용할 수 있도록 open api 제공함
- 대부분의 open api는 rest 방식을 지원



## 1. REST 란?

HTTP URL + HTTP Method

**HTTP URL를 통해 제어할 자원을 명시하고, HTTP Method를 통해 해당 자원을 제어하는 명령을 내리는 방식의 아키텍쳐**

> 특징

- URI로 지정한 리소스에 대한 조작을 통일하고 한정적인 인터페이스로 수행하는 아키텍처 스타일
- 세션이나 쿠키 등을 별도로 관리하지 않아 API 서버는 요청만 들어오는 메시지로만 처리하기에 구현이 단순함
- 캐싱 기능 적용 가능
- REST API 메시지로만 쉽게 이해 가능한 구조
- 클라이언트-서버 구조 (의존성이 줄어듬)
- 계층형 구조 (다중 계층으로 구조상 유연성 줄 수 있음)



> HTTP Method 종류

| Http Method | CRUD             |
| ----------- | ---------------- |
| POST        | Create (Insert)  |
| GET         | Read (Select)    |
| PUT         | Update or Create |
| DELETE      | Delete           |



## 2. Restful API

HTTP와 URI 기반으로 자원을 접근할 수 있도록 제공하는 애플리케이션 개발 인터페이스

|        | 기존 게시판                     | Restful API 지원 게시판 |
| ------ | ------------------------------- | ----------------------- |
| 글읽기 | GET /list.do?no=510&name=java   | GET /bbs/java/510       |
| 글등록 | POST /insert.do                 | POST /bbs/java/510      |
| 글삭제 | GET /delete.do?no=510&name=java | DELETE /bbs/java/510    |
| 글수정 | POST /update.do                 | PUT /bbs/java/510       |

> 필요한 이유⭐

- 분산 시스템
- html 같은 파일을 보내는 것은 무겁고 브라우저가 모든 앱을 가진 것은 아니기에 RESTful API를 사용하면서 **데이터만 주고 받기 때문에 여러 클라이언트가 자유롭고 부담없이 데이터를 이용함**
- 가볍고 유지보수성이 높음



## 3. JSON과 XML

### 1) JSON

- 경량의 Date-교환 방식

- javascript가 객체를 만들 때 사용하는 표현식
- JSON 표현식은 사람과 기계 모두 이해하기 쉽고 용량이 작아서 데이터 전송에도 사용됨
- 특정 언어에 종속되지 않고, json 포맷의 데이터를 핸들링할 수 있는 `라이브러리`를 제공함

> JSON의 형식

1. name-value 형식의 pair

   : 여러 가지 언어들에서 object, hashtable, struct로 실현

   ```json
   { 
   	"firstName": "Brett", 
       "lastName":"McLaughlin", 
       "email": "brett@newInstance.com" 
   } 
   ```

   

2. 값들의 순서화된 리스트 형식

   : 여러 가지 언어들에서 array, list로 실현

   ```json
   { 
   	"firstName": "Brett", 
       "lastName":"McLaughlin", 
       "email": brett@newInstance.com, 
       "hobby":["puzzles", "swimming"]
   } 
   ```



> JSON 라이브러리 `Jackson`

json형태를 java 객체로, java 객체를 json형태로 변환해주는 java용 라이브러리

![image-20200914135325246](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200914135325246.png)



### 2) XML

- 데이터를 저장하고 전달(교환)하기 위한 언어
- 인간/ 기계 모두가 읽기 편한 언어
- 데이터의 구조와 의미를 설명

> xml과 html의 차이

| xml                                  | html                                   |
| ------------------------------------ | -------------------------------------- |
| 데이터를 전달하는데 포커스 맞춘 언어 | 데이터를 표현하는데 포커스를 맞춘 언어 |
| 사용자가 마음대로 tag 정의 가능      | 미리 정의된 tag만 사용 가능            |





## 4. Spring MVC 기반 RESTful 웹 서비스

> 구현 절차

1. RESTful 웹 서비스를 처리할 RestfulController클래스 작성 및 @RestController 를 선언하여 bean 등록
2. 요청을 처리할 메서드에 @RequestMapping 과 @RequestBody 와 @ResponseBody 선언
3. REST Client Tool(Postman)을 사용하여 각각의 메서드 테스트
4. Ajax 통신을 하여 RESTful 웹 서비스를 호출하는 html 페이지 작성



## 5. 사용자 관리 RESTful 웹 서비스 

> URI와 Method

| Action      | Resource URI | HTTP Method |
| ----------- | ------------ | ----------- |
| 사용자 목록 | /users       | GET         |
| 사용자 보기 | /users/{id}  | GET         |
| 사용자 등록 | /users       | POST        |
| 사용자 수정 | /users       | PUT         |
| 사용자 삭제 | /users/{id}  | DELETE      |



> RESTful Controller를 위한 어노테이션

- 클라이언트에서 전송한 xml이나 json 데이터를 controller에서 java 객체로 변환해서 받을 수 있는 기능 제공
- java 객체를 xml이나 json으로 변환해서 전송할 수 있는 기능 제공

- `@RequestBody`  HTTP Request Body를 Java 객체로 전달받음
- `@ResponseBody`  Java 객체를 HTTP Response Body로 전송