# DOM

## DOM 정의 (Document Object Model)

브라우저의 렌더링 엔진은 웹 문서를 로드한 후, 파싱하여 웹 문서를 브라우저가 이해할 수 있는 구조로 구성하여 메모리에 적재하는 것

- html, xml 문서의 프로그래밍 api 
- w3c의 표준 객체 모델
- 문서의 구조화된 표현 제공, 프로그래밍 언어가 dom구조에 접근하도록 방법 제공
- 문서 구조, 스타일, 내용을 변경

> DOM과 HTML의 다른점?
>
> - HTML작성시 필요한 태그가 생략되어도 브라우저에서 고쳐서 생성
> - 예. HTML \<table>안에 \<tbody>없이 \<tr>,\<th>를 사용하여도 개발자도구에서 \<tbody>를 발견할 수 있다. `즉, \<tbody>는 DOM에 존재하는 것`



## 렌더링 순서(웹 문서-브라우저)

### HTML 문서에 대한 모델 구성

1. 브라우저는 HTML 문서를 로드하고 데이터를 파싱함
2. HTML을 파싱한 결과로 DOM Tree 생성함
3. 파싱 중 css파일 링크만나면 css파일 요청해서 받아옴
4. Css 파일 읽어서 CSSOM(css object model)을 만듬
5. DOM Tree와 CSSOM가 모두 만들어지면 둘을 사용해 Render Tree를 만듬
6. Render Tree에 있는 노드들이 화면에 어디 위치할 지 layout과정을 거쳐 paint함



## DOM Tree

브라우저가 html 문서를 로드한 후 파싱하여 생성하는 모델

: 모든 element는 HTMLElement의 자식, HTMLElement는 Element의 자식.....

- Object 

- Node 
- Element 
- HTMLElement 

### dom tree 구성

1. **Document Node**
   - 프로퍼티 값: #document
   - 최상위 노드
   - 각각 요소, 어트리뷰트, 텍스트 노드에 접근하여면 document node 통해야 함
2. **Element Node**
   - 프로퍼티 값: 태그 이름
   - HTML 요소를 표현
   - HTML 요소는 중첩에 의해 부자관계를 가지고 정보를 구조화하여 문서의 구조를 서술함
   - 어트리뷰트, 텍스트 노드에 접근하여면 element node 찾아 접근해야 함
3. **Attribute Node**
   - 프로퍼티 값: 속성 이름
   - HTML 요소의 어트리뷰터를 표현
   - 어트리뷰트가 지정된 요소의 자식이 아니라 해당 요소의 일부로 표현됨. 해당 element node를 찾아 접근하면 어트리뷰터를 참조, 수정가능함
4. **Text Node**
   - 프로퍼티 값: #text
   - HTML 요소의 텍스트를 표현함



## DOM 접근(DOM method)

#### 1. 요소 선택 메서드

##### 1) 한 개의 요소 노드 선택

1. Document.getElementById(id)
   - `id 속성 값으로` 한 개의 노드 선택(복수개면 첫번 째 요소만 반환)
2. Document.querySelector(cssSelector)
   - `cssSelector으로` 한 개의 노드 선택(복수개면 첫번 째 요소만 반환)

##### 2) 여러 개의 요소 노드 선택

1. Document.getElementsByClassName(class)
   - `해당 클래스에 속한` 요소를 모두 선택
   - 공백으로 구분하여 여러 개의 class 지정함
   - HTMLCollection(live) 리턴
2. Document.getElementsByName(name)
   - `해당 name 속성값`을 가진 요소를 모두 선택
   - NodeList(non-live) 리턴
3. Document.getElementsByTagName(tagName)
   - `해당 tagName`의 요소를 모두 선택
   - NodeList(non-live) 리턴

##### 3) 요소 생성 메서드 

1. Document.createElement(tagName)
   - `tagName에 맞는` HTML 요소 생성

2. Document.createTextNode(text)
   - `해당 text의  ` text노드 요소를 생성함

3. Document.write(text)
   - HTML 출력 스트림을 통해 텍스트를 출력

##### 4) 기본 내장 함수

1. document.cookie : HTML 문서의 쿠키를 반환
2. document.referrer : 링크되어 있는 문서의 url를 반환
3. document.URL : HTML 문서의 완전한 url 주소를 반환



#### 2. 노드 접근 활용 방법

##### 1) 프로퍼티로 접근 

\* *공백 주의*   <small>공백/ 줄바꿈 문자를 텍스트 노드로 취급하기 때문</small>

- parentNode: 부모 노드
- childNodes: 자식 노드 리스트(non-live, text 요소 포함) 
  - Children : 자식 요소 중 element type 요소만 반환(live)
- firstChild : 첫 번째 자식 노드 반환(text 요소 포함)
  - firstElementChild : 첫 번째 자식 엘리먼트 반환(element type 요소만)
- lastChild
  - lastElementChild
- nextSibling : 다음 형제 노드를 반환(text 요소 포함)
  - nextElementSibling : 다음 형제 요소 중 element type 요소만 반환
- previousSibling
  - previousElementSibling

##### 2) 노드에 대한 접근/ 수정

- nodeName : 노드의 이름 반환
- nodeValue : 노드의 값 반환 (text-> 문자열, element-> null)

- nodeType : 노드의 타입 반환

##### 3) 어트리뷰트에 대한 접근/ 수정

- className : class 어트리뷰트의 값 리턴/ 변경
- classList : add, remove, item, toggle, contains, replace 메소드 제공
- id : id 어트리뷰트의 값을 리턴/ 변경

- hasAttribute(attribute), getAttribute(attribute), setAttribute(attribute, value), removeAttribute(attribute)

##### 4) HTML 조작

- textContent
  - 노드의 내부 콘텐츠를 text/plain으로 파싱한 결과를 리턴/ 변경
  - 요소에 새로운 텍스트를 할당하면 텍스트 변경가능
  - 보안적으로, 속도적으로 유리
- innerText (사용x)
  - 요소의 텍스트 콘텐츠에만 접근 가능
  - css에 순종적이고 textcontent보다 느림
- innerHTML
  - innerHTML 프로퍼티의 값은 text/html으로 파싱한 결과를 리턴/ 변경
  - xss공격에 취약한 사례로 언급됨을 유의해야 함