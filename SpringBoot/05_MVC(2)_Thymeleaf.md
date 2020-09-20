# Spring Boot Web MVC

### :white_check_mark:Thymeleaf

스프링 부트가 자동 설정을 지원하는 웹 템플릿 엔진

- HTML5 문법으로 HTML 문서에 서버쪽 로직을 수행하고 적용시킬 수 있음

- HTML 디자인에 전혀 영향 안끼치고 웹 템플릿 엔진을 통해 HTML 생성
- 템플릿 엔진, th:xx 형식으로 속성을 html태그에 값 처리
- html의 위치는 `src/main/resources/templates/`



> JSP를 권장하지 않는 이유 
>
> - jar 패키징할 때 동작하지 않고, war 패키징 해야 함
> - servlet engine는 jsp 지원하지 않음



##### 타임리프 표현식

| 표현 | 설명                                                         |
| ---- | ------------------------------------------------------------ |
| ${ } | Variable Expression : 해당 context의 포함된 변수들을 사용    |
| *{ } | Selection Variable Expression : 가까운 DOM에 th:object로 정의된 변수가 있으면 그 변수에 포함된 값 |
| #{ } | Message Expression : 미리 정의된 message.properties가 있다면 사용 |
| @{ } | @표현식을 이용해 다양하게 url 표현 가능                      |



> Thymeleaf를 이용한 간단한 문장 출력

1. 의존성 추가

   ```xml
   <dependency>     
       <groupId>org.springframework.boot</groupId>     
       <artifactId>spring-boot-starter-thymeleaf</artifactId> 
   </dependency> 
   ```



2. Controller 설정

```java
	@GetMapping("/leaf") // localhost:8085/leaf치면 leaf_first.html을 불러서 띄움
	public String hello(Model model) {
		model.addAttribute("myName", "타임리프");
		return "leaf_first";
	}
```



3. html 파일 생성 (리턴 값) - `resource/templates/leaf_first.html`

- Controller에 있는 값(myName)을 th:text로 가져다 써서 치환되어 "타임리프"를 출력해낼 수 있음 
- 이때, 치환될 것인데 Hello Thymeleaf을 써주는 이유는 ! 서버를 사용하지 않고 해당 페이지를 열었을 때 어떠한 화면이라도 출력하도록 하기 위해서 :smile_cat:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2 th:text="${myName}">Hello Thymeleaf</h2>
	<h2>Hello, <span th:text="${myName}"></span></h2>
	<h2>헬로우, [[${myName}]]</h2>	<!-- [[]] 생략하면 변수로 인식을 못해서 '타임리프'가 뜨지 않는다. -->
</body>
</html>
```

5. 브라우저에서 `localhost:8085/leaf` 입력하면 leaf_first.html에 내용 출력



> Thymeleaf를 이용한 게시판 기능 구현

1. 메인페이지 `/static/index.html`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

</head>
<body>
	<h2>Hello, spring boot~ </h2>
	<h2><a href="/index">사용자관리</a></h2>
</body>
</html>
```



2. Controller 설정  `/main/~/controller/UserController.java` 

   1) User 리스트 Controller

```java
@Autowired
private UserRepository userRepository;
@GetMapping("/index")
	public ModelAndView getUsers() {
		List<User> userList = userRepository.findAll();
		return new ModelAndView("index", "users", userList); 
	}
```

​		2)  User 등록 Controller

					- 등록할 때 User.java(Entity)에 name과 email 값에 대해 앞에
					   `@NotBlank(message = "데이터 없음!") ` 붙여준다!! 

```java
@GetMapping("/signup")
public String addUserForm(User user) {
	return "add-user";
}

@PostMapping("/addUser")
	public String addUser(@Valid User user, BindingResult result, Model model) {
		// 입력항목에 에러가 있는지 check
		if (result.hasErrors()) {
			// 에러가 있으면 입력form 페이지가 다시 요청됨 (계속 그 페이지에 머물러있음)
			return "add-user";
		}
		userRepository.save(user);
		model.addAttribute("users", userRepository.findAll());
		return "redirect:/index"; // 등록을 완료해도 /index로 넘어감 (왜냐, 안쓰면 해당 id값이 주소에 뜨게 되니까 좋은 것이 아님. )
	}
```



​		3)  User 수정 Controller

```java
@GetMapping("/edit/{id}")
	public String showUpdateForm(@PathVariable("id") long id, Model model) {
		User user = userRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Invalid user Id:" + id));
		model.addAttribute("user", user);
		return "update-user";
	}

	@PostMapping("/update/{id}")
	public String updateUser(@PathVariable("id") long id, @Valid User user, BindingResult result, Model model) {
		if (result.hasErrors()) {
			user.setId(id);
			return "update-user";
		}
		userRepository.save(user);
		model.addAttribute("users", userRepository.findAll());
		return "redirect:/index";
	}
```

​		

​		4) User 삭제 Controller

​			- 삭제 시, 삭제되고 리스트에서 머물러있음

```java
@GetMapping("/delete/{email}")
	public String deleteUser(@PathVariable String email, Model model) {
		System.out.println("Email" + email);
		User user = userRepository.findByEmail(email).orElseThrow(() -> new IllegalArgumentException("Invalid user email:" + email));
		userRepository.delete(user);
		return "redirect:/index";
	}
```





3. return 값에 해당하는 페이지 생성

   1) (유저리스트) "index" 페이지 생성  `resource/template/index.html`

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<!-- script를 이용하여 삭제시, 바로 삭제되지 않고 한번 물어보고 삭제하는 기능 구현 -->
<script type="text/javascript">
	function deleteUser(email) {
		console.log('--->'+email);
		var repEmail=email.replace(/(^"|"$)/g, '');
		console.log('--->'+repEmail);
		var result = confirm(repEmail + " 사용자를 정말로 삭제하겠습니까?");
		if (result) {
			location.href = "/delete/" + repEmail;
		}
	}
</script>
</head>
<body>
	<table>
		<tr>
			<th>Name</th>
			<th>Email</th>
			<th>Edit</th>
			<th>Delete</th>
		</tr>
        
        <!-- User 리스트 -->
		<tr th:each="user : ${users}">
			<td th:text="${user.name}"></td>
			<td th:text="${user.email}"></td>
			<td><a th:href="@{/edit/{id}(id=${user.id})}">update</a></td>
			<td><button th:onclick="deleteUser('[[${user.email}]]')">delete</button></td>
			
		</tr>
	</table>
    
    <!-- User 등록 -->
	<a href="/signup">사용자 등록</a>
</body>
</html>
```

​	

​		2) (유저 등록) add-user 페이지 생성 `resource/template/add-user.html`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>사용자 등록</h2>
	<form th:action="@{/addUser}" th:object="${user}" method="post">
		<lable>Name: </lable>
		<input type="text" th:field="*{name}"> 
		<!-- 에러(입력x)나면 발생 -->
		<span th:if="${#fields.hasErrors('name')}" th:errors="*{name}"></span>
		<br/>
		<lable>Email: </lable>
		<input type="text" th:field="*{email}">
		<span th:if="${#fields.hasErrors('*{email}')}" th:errors="*{email}"></span>
		<input type="submit" value="등록">

	</form>
</body>
</html>
```



​		3)  (유저 수정) update-user 페이지 생성 `resource/template/update-user.html`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>사용자 업데이트</h2>
	<form action="#" th:action="@{/update/{id}(id=${user.id})}" th:object="${user}" method="post">
		<label for="name">Name</label> 
		<input type="text" th:field="*{name}" id="name"> 
		<span th:if="${#fields.hasErrors('name')}" th:errors="*{name}"></span> 
		<br /> 
		<label for="email">Email</label>
		<input type="text" th:field="*{email}" id="email"> 
		<span th:if="${#fields.hasErrors('email')}" th:errors="*{email}"></span> <br />
		<input type="submit" value="Update User">
	</form>
</body>
</html>
```