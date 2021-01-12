# Angular 

구글이 만든 웹 애플리케이션 플랫폼으로서 다양한 플랫폼에서 동작할 수 있게 하는 개발 툴과 기능들을 제공

- 완전한 프레임워크 - 프로젝트 생성, 테스트, 빌드, 배포를 위한 모든 기능 제공
- Typescript 사용
- angular cli를 제공하여 개발환경 지원
- 모듈과 컴포넌트 기반
- 웬만한 기능의 라이브러리는 모두 포함시켜 자체적으로 제공함(라우팅, http, form 등)
- 기본적으로 spa(single page application) 개발을 위한 프레임워크 + server side rendering

> #### 장점
> - 프레임워크 
> - 유지 관리가 용이함
> - 모든 길은 angular-cli (여러가지 편리한 기능 제공)
>   - 프로젝트 생성(with 의존성 패키지)
>   - 라이트한 서버 제공 : 코드 수정시 즉시 변경사항 반영되어 웹페이지에서 렌더링
>   - webpack 내장되어 빌드 수행 가능(typescript를 컴파일해서 javascript로 압축하는 것까지 자동으로 진행)
>   - 테스트 가능
> #### 단점
> - 앵귤러만의 패턴 존재
## Angular 시작하기 

#### Angular CLI 설치

`npm install -g @angular/cli`	

#### 프로젝트 생성 / 개발 서버 실행

`ng new first-app` : angular 프로젝트 생성

`ng serve` : 빌드 시키고 url 리턴 (포트번호: 4200)



## Module (ES6 Module)

세부 구현이 숨겨지고 공개 api를 이용해 다른 코드에서 재사용 가능한 코드

(\+ 변수의 스콥이 모듈로 제한)
  


## Angular Module

컴포넌트, 파이프, 서비스 등과 같은 앵귤러 애플리케이션의 주요 부분을 기능 단위로 그룹핑하게 해준다.

- 모든 앵귤러 애플리케이션은 하나의 root module을 가진다. 
- 여러 feature module을 가질 수 있다. 
- 재사용할 수 있는 기능을 외부에 배포하기 위해 사용되기도 한다. 
  - MdbuttonModule(meterial)
  - ModalModule(bootstrap)

### module 생성

`ng generate module todo`	: /app/todo 폴더가 생성됨을 확인

`ng g c todo/todos --module todo/todo.module.ts --export`	: /app/todo/todos 폴더 생성 확인함(.css, html, ts 파일들을 포함한)





## Component

- 빌딩 블록
- html 요소들의 그룹
- 뷰와 로직으로 구성

### Component 생성

plugin 이용하여 new component : 

`todo --inline-template --inline-style`

- --inline-template : html, css는 따로 생성되지 않고 todo.component.ts안에 포함시킨다. 
  - Template 안에 생성하면 됨:  ``(백틱을 이용해서 )



### Angular Template

- HTML 코드로서 템플릿을 표현
- Template 표현식과 Template문장을 가짐
- 바인딩  <small>(커뮤니케이션)</small>
  - 바인딩의 대상: 속성, 이벤트, ngModel, class, style



### 컴포넌트 커뮤니케이션

- 부모 -> 자식 
  - @Input()
  - ES6 setter
  - @ViewChild()
- 자식 -> 부모
  - @Output()
  - EventEmitter를 사용하여 부모에게 이벤트 전달
  - 부모 컴포넌트는 $event로 이벤트의 데이터를 전달 받음
  - 자식이 부모 컴포넌트를 직접 주입받을 수 있음



### 파이프

- 템플릿에서 보이는 데이터를 변환해줌
- 사용법: 
  - `{{express | pipeName: paramValue}} `	{{ today | date: "M월 d일" }}

