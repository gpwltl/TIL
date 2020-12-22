### python 컴파일 방식

java(컴파일 언어)는 컴파일러를 수행해서 소스코드를 컴파일된 class 파일로 만든다.
**`python`은 이런 과정을 거치지 않는 것처럼 보여 interpreted 언어라고 불리지만 모두 작성된 코드를 bytecode로 바꿔주는 작업 후 vm 통해 코드 실행**

- 특정 프로그래밍 언어로 작성된 코드가 어떻게 실행되냐는 단순히 언어적인 특성이 아니라 언어가 구현체에 따라 다름.
- 보통 CPython을 사용
- just-in-time(JIT)방식을 사용한 PyPy는 다른 구현체이고, CPython보다 훨씬 빠름

### python 특징

1. 쉽고 간결하다.
2. 빠른 개발 속도
3. 오픈소스 개발 언어, 흡수성(다른 언어로 제작된 모듈들도 포함시켜 사용 가능)

#### python 문법적 특징

1. Dynamic typing
   - 변수의 타입을 자동으로 검사(객체라서 가능)
2. Script Language
   - 한 줄씩 실행하여 바로 바로 확인가능하지만, 속도가 느림
   - 속도향상을 위해 JIT 사용
3. Multi paradigm
   - 절차적, 객체지향, 함수형, 관점형 프로그래밍 가능
4. Unlimited access
   - 접근제어 없이 객체, 구조체 member에 무제한적 접근가능
5. Everything is object
   - 변수와 함수 모두 객체
