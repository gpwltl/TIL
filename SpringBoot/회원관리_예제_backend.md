# 회원 관리 예제 backend

##  0. 비즈니스 요구사항

- 데이터 : 회원 id, 이름
- 기능: 회원 등록, 조회
- 아직 데이터 저장소가 선정되지 않음



> 일반적인 웹 애플리케이션 계층 구조 

![image-20200920160732562](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200920160732562.png)

- 컨트롤러: 웹 MVC의 컨트롤러
- 서비스: 핵심 비즈니스 로직 구현(예. 회원가입 중복 가입 불가)
- 리포지토리: 비즈니스 도메인 객체를 가지고 서비스를 관리
- 도메인: 비즈니스 도메인 객체 (예. 회원, 주문, 쿠폰 등 주로 DB에 저장하고 관리됨) 



## 1. 회원 도메인과 레파지토리 만들기

> 회원 객체 

- `Member.java`
- private Long id; private String name; 등 변수 선언 
- getter/setter 해줄 것

> 회원 레파지토리 인터페이스

- 인터페이스이므로 필요한 메서드 생성
- `MemberRepository.java` \<interface>

```java
Member save(Member member);
Optional<Member> findById(Long id);
Optional<Member> findByName(String name);
List<Member> findAll();
```

> 회원 레파지토리 메모리 구현체

- `MemoryMemberRepository.java`
- MemoryMemberRepository implements MemberRepository



## 2. 회원 레파지토리 테스트 케이스 작성

해당 기능을 실행해서 테스트할 때 main을 통해서 하거나 컨트롤러를 이용하면 준비, 실행시간이 오래 걸리고, 반복 실행하기 어렵다. => `JUnit` 프레임워크로 테스트 실행할 것

- 위치 : src/test/java
- 단정 메서드로 테스트 케이스의 수행 결과를 판별`assertEquals(예상 값, 실제 값)`,,,
- jUnit4,  `@Test`, `@Before`, `@After`

| jUnit4 annotation | 설명                            | jUnit5 변경 |
| ----------------- | ------------------------------- | ----------- |
| @BeforeClass      | 테스트 시작 시, 1번만 호출      | @BeforeAll  |
| @Before           | 테스트 케이스 시작전, 각각 호출 | @BeforeEach |
| @After            | 테스트 케이스 완료시, 각각 호출 | @AfterEach  |
| @AfterClass       | 모든 테스트 완료시, 1번 호출    | @AfterAll   |



## 3. 회원 서비스 개발 & 테스트

- 회원가입, 조회 등의 원하는 기능을 실제적으로 구현하는 곳 

```java
//기존에는 회원 서비스가 메모리 회원 레파지토리를 직접 생성하게 함
public class MemberService {
 private final MemberRepository memberRepository =
 new MemoryMemberRepository();
}
```

​														↓

```java
//회원 서비스 코드를 DI 가능하게 변경함
public class MemberService {
 private final MemberRepository memberRepository;
 public MemberService(MemberRepository memberRepository) {
 this.memberRepository = memberRepository;
 }
 ...
}
```

