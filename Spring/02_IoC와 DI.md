## IoC와 DI

### 0. 컨테이너

> 객체의 생성과 소멸같은 부분을 전담해주는 역할 
> (주식을 주식 전문가에게 맡기는 것과 유사)



### 1. IoC

> Inversion of Control 제어의 역전

무언가를 조종하고 다루는 존재가 바뀌는 것을 의미하게 되는데 
즉, 개발자 대신 컨테이너가 스프링의 객체를 생성하고 제어하고 소멸(생명주기 관리)한다.



#### 용어정리

- `bean` : 스프링에서 제어권을 가지고 직접 만들어 관계를 부여하는 오브젝트

- `bean factory` : 스프링의 IoC를 담당하는 핵심 컨테이너

  > 보통 바로 사용하지 않고 확장한 application context를 이용한다. 

- `application context` : bean factory를 확장한 IoC 컨테이너

  > 추가적으로 spring의 각종 부가 서비스를 제공함

- `configuration metadata` : application context 혹은 bean factory가 IoC를 적용하기 위해 사용하는 메타정보

- `container (ioC container)` : IoC 방식으로 bean을 관리한다는 의미에서 bean factory나 application context를 가리킨다.



### 2. DI

> Dependency Injection 의존성 주입

소스 코드 내에서 모든 것이 이루어지는 것이 아니고 구현체를 외부에서 주입받는 것 

