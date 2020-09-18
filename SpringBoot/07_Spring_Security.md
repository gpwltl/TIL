# Spring Security

spring 애플리케이션의 보안(인증, 권한, 인가)을 담당하는 스프링 하위 프레임워크

- 인증 Authorization  - 해당 사용자가 본인이 맞는지 확인하는 절차
- 인가 Authentication - 인증된 사용자가 요청한 자원에 접근 가능한지 결정하는 절차



> 특징

- 스프링 부트 시큐리티 자동설정 `SecurityAutoConfiguration`, `UserDetailsServiceAutoConfiguration`

- 모든 요청에 인증 필요
- 기본 사용자를 자동으로 생성해줌



> 인증 구현

1. 의존성 추가 

```xml
<dependency>     <groupId>org.springframework.boot</groupId>     <artifactId>spring-boot-starter-security</artifactId> </dependency> 
```

2. 브라우저에 localhost:8085/login 에 접속하여 기본 설정된 정보로 로그인을 해줍니다.
   - Username : user
   - Password : 서버 실행 시, 랜덤 값 생성

3. 로그아웃은 Cookie를 clear해서 로그아웃함
   (쿠키삭제는 '개발자도구-> Application-> Storage-> Cookies')



> Security 설정 커스터 마이징

0. 기초 작업

![image-20200918161443852](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200918161443852.png)

1. 로그인 정보 페이지 작성	 `resources/template/mypage.html`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<meta charset="UTF-8">
<body>
	<h1>My Page</h1>
	<div>
		Logged in user: <b th:inline="text" class="user">
			[[${#httpServletRequest.remoteUser}]] </b>
		<form th:action="@{/app-logout}" method="POST">
			<input type="submit" value="Logout" />
		</form>
	</div>
</body>
</html>
```



2. SecurityConfig 클래스 작성	 `main 폴더에서 SecurityConfig.java`
   - 로그인 기능 :heavy_check_mark:
   - 로그아웃 기능:heavy_check_mark:

```java
@Configuration
public class SecurityConfiguration extends WebSecurityConfigurerAdapter{
	@Override
    protected void configure(HttpSecurity http) throws Exception {
		//로그인
        http
        .authorizeRequests()	//인증이 필요한 모든 요청에 대해
		.antMatchers("/mypage/**").authenticated() 	  //mypage 경로에만 인증 요청
		.antMatchers("/**").permitAll()		//다른 경로들은 인증 요청 필요없음   
		.and()
		.formLogin()
		.and()
            
        //로그아웃
		.logout()
		.logoutUrl("/app-logout")
		.deleteCookies("JSESSIONID")
		.logoutSuccessUrl("/");

	}
```



3. AccountService 클래스 작성	`main에서 AccountService.java`

```java
import org.springframework.security.core.userdetails.UserDetailsService;

@Service
public class AccountService implements UserDetailsService {
	private final AccountRepository repository;
	private final GpwltlProperties props;
	private final PasswordEncoder passwordEncoder;
    
    //Generate Constructor using Field
	public AccountService(AccountRepository repository, GpwltlProperties props, PasswordEncoder passwordEncoder) {
		this.repository = repository;
		this.props = props;
		this.passwordEncoder = passwordEncoder;
	}
	
	//이 메서드 추가함(SecurityConfiguration 추가)으로써 설정된 id,pw로 login 가능
	//Account 레코드 추가
    public Account createAccount(String email, String password) {
		Account account = new Account();
		account.setEmail(email);
		//passwordEncoder의 빈을 주입받아 password인코딩
		account.setPassword(passwordEncoder.encode(password));
		return repository.save(account);
	}
    
    //createAccount() 메서드 호출
    @PostConstruct
	public void init() {
		Optional<Account> optEmail = repository.findByEmail(props.getEmail());
		//이메일 주소와 매칭되는 Account가 없으면
		if(optEmail.isEmpty()) {
			Account account = this.createAccount(props.getEmail(), props.getPassword());
			System.out.println(account);
		}
	}
    
	//여길 추가하면서 id(email:boot@abc.com)값과 password(1234)를 내가 지정한 값으로 가능
    //login할 때 사용자가 입력한 정보가 유효한지 체크
	@Override
	public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
		Optional<Account> optEmail = repository.findByEmail(email);
		Account account = optEmail.orElseThrow(()->new UsernameNotFoundException(email+" Not Found"));
		return new User(account.getEmail(), account.getPassword(), authorities());
	}
	
    //User 객체의 세번째 인자 USER라는 ROLE을 가진 사용자이다라고 설정하는 부분
	private Collection<? extends GrantedAuthority> authorities(){
		return Arrays.asList(new SimpleGrantedAuthority("ROLE_USER"));
	}
}
```

```java
//SecurityConfiguration 파일에 추가
//passwordEncoder를 빈으로 등록
@Bean
	public PasswordEncoder passwordEncoder() {
		return PasswordEncoderFactories.createDelegatingPasswordEncoder();
	}
}
```



4. 로그인 실행
   - 설정한 username과 password로 로그인 가능