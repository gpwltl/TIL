## 1. 자바스크립트 엔진

javascript로 작성한 코드를 해석하고 실행하는 `인터프리터`

- node.js와 함께 server sid에선 V8을 엔진으로 사용
- 대표 예. Google V8
  - Call Stack
  - Task Queue(Event queue)
  - Heap

### 1) Call Stack

자바스크립트는 단 하나의 호출 스택을 사용함

- 함수 실행 방식: Run to Completion
  > Run to Completion: 하나의 함수가 실행되면 실행이 끝날 때까지 다른 task 수행할 수 없음
- 요청시마다 해당 요청을 **순차적으로** 호출스택에 담아 처리함
- 메소드 실행하면 호출스택에 새로운 프레임이 push되고 메소드 실행 끝나면 해당 프레임이 pop되는 원리

```javascript
function foo(b) {
  var a = 10;
  return a + b;
}
function bar(x) {
  var y = 2;
  return foo(x + y);
}
console.log(bar(1));
```

![image](https://user-images.githubusercontent.com/44856614/102870419-55bec380-4480-11eb-9f6e-7d169a343bc9.png)

> task1= bar(), task2= foo()
> bar함수가 먼저 push, 이때 foo함수를 호출하여 pop되지않고 foo함수가 push됨
> foo함수 역할 마치면 pop되고 bar함수로 돌아와 값을 리턴하면서 pop됨

### 2) Heap

- 동적으로 생성된 객체는 힙에 할당됨
- 구조화되지 않는 메모리 영역

### 3) Task Queue(Event Queue)

런타임 환경에서는 처리할 task들을 임시 저장하는 `대기 큐`가 존재함

- call stack이 비어졌을 때 먼저 대기열에 들어온 순서대로 수행함
- 이벤트에 걸려있는 핸들러는 절대 먼저 실행될 수 없음

```javascript
function test1() {
  console.log("test1");
  test2();
}
function test2() {
  let timer = setTimeout(function () {
    console.log("test2");
  }, 0);
  test3();
}
function test3() {
  console.log("test3");
}

test1();
```

> console>> test1 \n test3 \n test2
>
> - 먼저 test1이 실행되면서 'test1'을 출력함 (test1 push)
> - test2은 setTimeout 함수가 실행되면 콜스택에 들어간 다음, 바로 빠져 나옴(0초) (test2 push)
>   - 이때 setTimeout 함수(핸들러(익명함수))는 빠져나와 event queue영역으로 들어가고 그 이외의 나머지 것(test2)들이 실행됨
> - test3 실행되면 'test3' 출력(test3 push)
> - 이후 test3, test2, test1 순으로 pop
> - 콜스택이 모두 비워진 후, 이벤트큐에 있는 함수를 콜스택에 가져와 익명함수 실행 : 'test2' 출력
