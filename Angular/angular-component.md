# Component

angular는 컴포넌트를 중심으로 구성됨. 애플리케이션의 화면을 구성하는 **뷰를 생성하고 관리**

- 동작 가능한 하나의 부품
- 컴포넌트 내에서만 유효한 상태 정보와 로직, 스타일을 소유한 완결된 뷰를 생성하기 위한 것
- 독립적이고 완결된 뷰를 생성하기 위해 HTML, CSS, JAVASCRIPT를 하나의 단위로 묶는 것



## :green_apple: web component

웹 애플리케이션에서 재사용이 가능하도록 캡슐화된 htlm 커스텀 요소를 생성하는 웹 플랫폼 api의 집합

- 컴포넌트의 뷰를 생성할 수 있어야 함 `html template`

- 외부로부터의 간섭을 제어하기위해 scope를 분리하여 dom을 캡슐화할 수 있어야 함 `shadow dom`
- 외부에서 컴포넌트를 호출할 수 있어야 함 `html import`
- 컴포넌트의 명칭alias를 선언하여 마치 네이티브 html 요소와 같이 사용할 수 있어야 함 `custom element`



## :green_apple: ​component tree

컴포넌트는 재사용이 용이한 구조로 분할하여 작성하며 분할된 컴포넌트를 조립하여 코드의 중복없이 ui를 생성한다. 

![image](https://user-images.githubusercontent.com/44856614/104283105-64cee980-54f3-11eb-8e64-2999f3300e86.png)

- 컴포넌트 트리로 표현되는 `부모-자식` 관계 형성
  - 데이터와 이벤트 등 상태 공유



## :green_apple: 코드 구조

$ng new hello

$cd hello

$ng serve --open : 앵귤러는 webpack을 사용하여 소스코드와 의존 모듈을 자바스크립트로 번들링하고 angular cli가 내장하고 있는 개발용 서버를 실행한다. 

<br/>

**src/app/app.component.ts (루트 컴포넌트)**

1. 임포트 영역

2. @component 데코레이터 영역 : 메타데이터 객체를 인자로 전달

   - selector
   - templateUrl  : 컴포넌트의 뷰를 정의한 템플릿의 상대경로 설정
   - styleUrls

3. 컴포넌트 클래스 영역 : 뷰를 관리하는 로직을 담은 클래스 정의

   (데코레이터와 클래스 영역 사이에는 아무것도 존재해서는 안된다!!)



## :green_apple: 기본 동작 구조

**src/app/app.component.html (templateUrl 템플릿)**

- {{ title }}  : 데이터 바인딩

  \- 컴포넌트 클래스의 데이터를 템플릿에 바인딩

- (click)="function()"

- []

<br/>

- 새로운 컴포넌트 만들 때 
  **ng generate component 컴포넌트명**  (축약형 `ng g c 컴포넌트명`)
  - 하위 컴포넌트 만들 때
    `ng g c 상위컴포넌트명/하위컴포넌트명`



## :green_apple: component class

컴포넌트 뷰를 관리하기 위한 로직을 정의 

`export class HelloComponent{}`	(src/app/hello/hello.component)

> ES6 모듈과 Angular 모듈의 차이
>
> - ES6 모듈 : 애플리케이션을 구성하는 개별적 요소 (파일 단위로 분리) -> 개별적으로 존재하다가 애플리케이션의 로드에 의해 애플리케이션의 일원이 된다. 
> - Angular 모듈(NgModule) : angular 구성 요소를 하나로 묶어 애플리케이션을 구성하는 하나의 단위로 만드는 역할 (컴포넌트, 디렉티브, 서비스 등이 모듈에 등록되어야 사용 가능)



## :green_apple: @Component decorater

@Component()를 해당 클래스 바로 앞에 호출하여 angular에게 해당 클래스가 일반 클래스가 아닌 **컴포넌트 클래스임을 알린다.** 

-> 자신의 바로 아래에 있는 클래스를 컴포넌트 클래스로 인식

![image](https://user-images.githubusercontent.com/44856614/104284945-36064280-54f6-11eb-9cff-40a05050dc58.png)



## :green_apple: 모듈에 컴포넌트 등록

**src/app/app.module.ts** (루트 모듈)

ng g c 명령어로 컴포넌트를 추가했을 경우, 추가된 컴포넌트는 자동으로 모듈에 등록된다. 

![image](https://user-images.githubusercontent.com/44856614/104285344-d8262a80-54f6-11eb-98a4-99911eeecaff.png)