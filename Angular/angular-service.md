# Service

컴포넌트에 제공할 목적으로 외부에 정의한 클래스.

- 모든 컴포넌트에 공통적으로 존재할 수 있는 공통 관심 기능을 서비스로 만듬
- `ng g service 서비스명`



## 🍏 정의 @Injectable

서비스 정의는 @Injectable 장식자를 사용 (주입 가능한 클래스 의미)

- 서비스 : 서비스 정의

```typescript
import { Injectable } from '@angular/core';
@Injectable()
export class HelloService {
  sayHello(){
    return "Hello 서비스!";
  }
  constructor() {}
}
```

<br/>

> **컴포넌트에서 서비스를 사용하는 방법**

- 컴포넌트
  `providers`에 서비스를 등록하고 사용한다. +constructor

```typescript
import { Component } from '@angular/core';
import { HelloService } from './hello.service';

@Component({
  selector: 'hello',
  template: `{{welcome}}`,
  providers: [HelloService]
})
export class HelloComponent {
  welcome: string;

  constructor(helloService: HelloService) {
    this.welcome = helloService.sayHello();    
  }
}
```



## 🍏 데이터 교환

부모 컴포넌트에는 제공자 설정을 통해 주입. 

- 자식 컴포넌트에는 제공자 설정하지 않고 서비스를 받아서 사용하면 같은 서비스를 통해 값 공유 가능
- 바로 위의 부모 컴포넌트에서 존재하지 않는다면 그 컴포넌트의 상위 컴포넌트로 이동하여 존재한다면 사용

<br/>

> injector 검색 순서 

자신의 컴포넌트

-> 부모 컴포넌트

-> 루트 컴포넌트까지 계속 부모-자식 관계를 타고 올라감

-> 루트모듈

-> 하위 모듈 

-> 자신이 속한 모듈까지 계속 내려옴

-> 도중에 해당 서비스에 대한 providers값이 있다면 검색 종료



## 🍏 Angular 의존성 주입

객체 생성과 설정에 들어가는 코드를 최소화하고, 컴포넌트마다 일관된 방법으로 생성한 객체를 제공하기 위해서 필요

- @Injector : 주입할 클래스 선택
- Provider : 주입할 클래스를 제공자에 등록
- Dependency Injection : 생성자로 의존성 주입을 받음



### 제공자를 통한 의존성 주입

- 클래스 제공자 

  1) `@Injectable() `

  2) `@Component({ ...providers: [주입할 클래스]})`

  3) 생성자 패턴 이용해 의존성 주입  `constructor(public [주입할 클래스명 : 클래스])`