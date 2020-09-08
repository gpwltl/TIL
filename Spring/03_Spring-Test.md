# Spring-Test

## 1. Spring-Test에서 테스트를 지원하는 어노테이션

#### @RunWith(SpringJUnit4ClassRunner.class)

- @RunWith는 jUnit 프레임워크의 테스트용으로 구동하기 위해 환경을 잡아주기 위해 사용하는 어노테이션
- SpringJUnit4ClassRunner.class라는 클래스로 지정해주어 테스트시 ApplicationContext를 만들고 관리해줌
- 별도 객체가 생성되어도 싱글톤의 ApplicationContext를 보장함

#### @ContextConfiguration

- 스프링 빈 설정 파일의 위치를 지정할 때 사용되는 어노테이션

#### @Autowired

- 스프링 DI에서 사용되는 특별한 어노테이션
- 해당 변수에 자동으로 빈을 매핑
- 스프링 빈 설정 파일을 읽기 위해 굳이 GenericXmlApplicationContext를 사용할 필요가 없음 



## 2. Bean 등록 메타정보 구성 전략

### 전략1. xml 설정 단독 사용

> 모든 Bean을 명시적으로 xml에 등록하는 방법

- 생성되는 bean을 xml에서 확인할 수 있으나 빈의 개수가 많아지면 관리하기 번거러움
- 같은 설정파일을 공유해서 개발하면 설정파일을 동시에 수정하다가 충돌이 일어날 수 있음
- DI에 필요한 적절한 setter 메서드나 constructor가 코드내 반드시 존재해야 함
- 운영중에도 관리의 편의성을 위해 xml설정으로 변경하는 전략 사용 가능

### 전략2. 어노테이션과 xml 설정 혼용해서 사용

- Bean으로 사용될 클래스에 특별한 어노테이션을 부여하면 클래스를 자동으로 찾아서 빈으로 등록
- @Component이 선언된 클래스를 자동으로 찾아 빈으로 등록해주는 방식
  -> 빈 스캐닝을 통한 자동인식 빈 등록 기능
- xml 문서 생성과 관리에 따른 수고를 덜어주고 개발 속도를 향상시킴
- 등록될 빈이 어떤 것들이 있고, 빈들 간 의존관계가 어떻게 되는지 한눈에 파악하기 어려움

> Bean 등록 Annotation

- `@Component`  컨포넌트를 나타내는 일반적인 스테레오 타입 (\<bean>과 동일)
- `@Repository`  영속성을 가지는 속성(파일, 데이터베이스)을 가진 클래스
- `@Service`  서비스 레이어, 비즈니스 로직을 가진 클래스
- `@Controller`  웹 요청과 응답을 처리하는 클래스



#### Bean 의존관계 설정 Annotation

#### 1) @Autowired

- DI가 필요한 경우에 유용함
- @Autowired는 변수, setter 메서드, 생성자, 일반 메서드에 적용 가능
- 의존하는 객체를 주입할 때 주로 `Type` 이용
- \<property>, \<constructor-arg> 태그와 동일한 역할

#### 2) @Resource

- 어플리케이션에서 필요로 하는 자원을 자동 연결할 때 사용
- @Resource는 변수, setter 메서드에 적용 가능
- 의존하는 객체를 주입할 때 주로 `Name` 이용

#### 3) Value

- 단순한 값을 주입할 때 사용
- @Value("Spring")은 \<property ... value="Spring" /> 과 동일한 표현

#### 4) Qualifier

- @Autowired 와 같이 사용함
- @Autowired는 타입으로 찾아서 주입하므로, 동일한 타입의 Bean객체가 여러 개 존재할 때 특정 Bean을 찾기 위해선 @Qualifier를 같이 사용해야 함



#### Component Scan을 지원하는 태그

#### 1) <context: component-scan>

- @Component를 통해 자동으로 bean을 등록
- @Autowired로 의존관계를 주입받는 어노테이션을 클래스에서 선언하여 사용했을 때 해당 클래스가 위치한 **특정 패키지를 scan하기 위한 설정을 xml에 해줘야 함**

`<context:conponent-scan base-package="myspring.di.annotation" />` (공백 주의)

- \<context:inclue-filiter>와 \<context:exclue-filter>를 같이 사용하면 자동 스캔 대상에 포함시킬 클래스와 포함시키지 않을 클래스를 구체적으로 명시가능



### 전략3. 어노테이션 설정 단독 사용

- Spring JavaConfig 프로젝트는 xml이 아닌 자바 코드를 이용해서 컨테이너를 설정할 수 있는 기능을 제공
- @Configuration과 @Bean을 이용해서 스프링 컨테이너에 새로운 빈 객체를 제공함

#### Bean 등록과 설정 annotaion

#### 1) @Bean

- 새로운 빈 객체를 제공할 때 사용되며, @Bean이 적용된 메서드의 이름을 Bean의 식별값으로 사용함

#### 2) @Configuration

- 클래스에 선언하면 스프링 IoC 컨테이너가 해당 클래스를 빈 정의의 설정으로 사용한다는 것을 나타냄



#### Spring-Test에서 테스트 지원하는 annotation

#### 1) @ContextConfiguration

`@ContextConfiguration(classes=HelloBeanConfig.class, loader=AnnotationConfigContextLoader.class)`

이전과 달리 locations을 사용하지않고 classes와 loader를 구분하여 사용함



## 3. Property 파일을 이용한 설정 방법

- xml의 빈 설정 메타정보는 애플리케이션 구조가 바뀌지 않으면 자주 변경되지 않는다. 
- 프로퍼티 값으로 제공하는 **설정 정보는 애플리케이션이 동작하는 환경에 따라 자주 변경됨 **
- 환경에 따라 자주 변경될 수 있는 내용은 properties 파일로 분리하는 것이 가장 깔끔함 
- 키와 값의 쌍(key=value)으로 구성함



> 사용방법

- 프로퍼티 파일로 분리한 정보는 ${} (프로퍼티 치환자)을 이용하여 설정함
- \<context:property-placeholder>에 의해 자동으로 등록되는 PropertyPlaceHolderConfigurer Bean이 담당함