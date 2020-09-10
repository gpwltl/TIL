# Servlet 과 JSP

## 1. Servlet

> Servlet이란? 

- 웹 프로그래밍에서 클라이언트 요청을 처리하고 처리 결과를 클라이언트에 전송하는 기술
- 자바로 구현된 CGI 
  <small>*CGI란 별도로 제작된 웹 서버와 프로그램간의 교환 방식 - HTML의 GET, POST방법으로 클라이언트의 데이터를 환경변수로 전달하고 표준 출력 결과를 클라이언트에 전송</small>
- **자바 소스코드 속에** HTML이 들어간 형태



> 특징

- **클라이언트의 요청에 대해 동적으로 작동**하는 웹 어플리케이션 컴포넌트
  (동적인 페이지? 사용자의 요청에 의해 변화된느 무언가를 제공하는 것)
- HTML로 요청, 응답
- 자바 스레드를 통해 동작
- MVC 패턴 중 Controller로 이용함
- HTML 변경시 서블릿 재컴파일 해야 함



> 동작 방식

1. 사용자가 url 클릭하면 `http request를 서블릿 컨테이너로 전송`
2. 요청받은 서블릿 컨테이너는 `HttpServletRequest, HttpServletResponse 두 객체를 생성함`
3. `web.xml`은 사용자가 요청한 url을 분석해 `어느 서블릿에 대해 요청한 것인지 찾음`
4. 해당 서블릿에서 `service 메소드`를 호출하여 클라이언트의 `요청종류(GET, POST)`에 따라 doGet / doPost를 호출함
5. `doGet, doPost 메소드`는 동적 페이지를 생성한 후 `HttpServletResponse 객체에 응답을 보냄`
6. 응답이 끝나면 HttpServletRequest, HttpServletResponse `두 객체를 소멸시킴`



> HTTP 프로토콜 방식 (요청, 응답 방식)

- GET방식
  - `http://localhost:8087/myweb.hello?key=value1`
  - url에 append해서 보냄 ( ? 뒤는 query string)
  - 사이즈 제한 있음
- POST방식
  - `http://localhost:8087/myweb.hello`  뒤에 정보 표시x
  - stream의 body에 append해서 보냄
  - 사이즈 제한 없음



## 2. Servlet Container

> Servlet Container란 ?

- 서블릿을 관리해주는 컨테이너를 말함 - `Tomcat`
- 클라이언트의 요청을 받아주고 응답하도록 웹서버와 소켓을 만들어 통신함



> 역할

- 서블릿과 웹 서버가 쉽게 통신하도록 지원
  (소켓기능은 api로 제공하여 복잡한 과정 생략, 개발자는 비즈니스 로직에만 포커스)
- 서블릿의 탄생과 죽음(생명주기) 관리
  - 서블릿 클래스 로딩하여 인스턴스화
  - 초기화 메소드 호출
  - 요청이 들어오면 적절한 서블릿 메소드 호출
- 요청시마다 새로운 자바 스레드를 하나 생성하는데, http 서비스 메소드를 실행한 후에는 자동적으로 스레드가 죽음(멀티 스레드) - 컨테이너가 관리
- 보안관리는 xml배포 서술자가 기록하여 자바 소스를 수정할 일이 없음



> 서블릿 생명주기란 ?

1. 클라이언트가 요청하면 해당 서블릿이 메모리에 존재하는지 확인

2. 없으면, init() 메소드를 호출하여 적재함

   `init()` : 최초 한번만 실행. 서블릿의 스레드에서 공통적으로 사용해야 한다면 **오버라이딩**

3. init() 호출된 후 클라이언트의 요청에 따라 service 메소드를 통해 응답이 doGet, doPost로 나뉨
   `service()` : 새로고침할 때 마다 실행

4. 서블릿 컨테이너가 클라이언트의 요청에 의해 가장 먼저 HttpServletRequest와 HttpServletResponse로 request, response 객체를 제공함

5. 컨테이너가 서블릿에 종료 요청하면 destory() 메소드가 호출
   `destory()` : 한번만 실행. 종료시 처리해야 할 작업들 오버라이딩하여 구현



> 한글 인코딩할 때 유의점

**요청 데이터에 대한 한글 인코딩**

- `request.setCharacterEncoding("EUC-KR");`
- 입력 데이터를 요청하기 전 선언해야 함

**응답 데이터에 대한 한글 인코딩**

- `response.setContentType("text/html; charset=EUC-KR");`
- 응답 데이터를 출력하기 전 선언해야 함



## 3. JSP

> JSP란? 

- JAVA 코드가 들어있는 **HTML 코드**
- 웹 서버 내에서 실행함 (브라우저에 전송x)
- 서블릿 컨테이너에 의해 서블릿으로 변환되어 사용



> 동작 방식 

1. 웹 서버가 사용자의 요청을 받으면 서블릿 컨테이너에 요청을 넘김
2. 서블릿 컨테이너는 서블릿객체로 변환
3. 기존 서블릿 처리를 진행하듯이 동작 결과를 웹 브라우저로 응답