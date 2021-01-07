# AJAX

#### Asynchronous Javascript And XML

javascript의 라이브러리 중 하나.

- XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법
- Javascript를 사용한 비동기 통신, 클라이언트와 서버간에 XML데이터를 주고받는 기술



## 비동기 방식

웹 페이지를 리로드하지 않고 데이터를 불러오는 방식

- Ajax를 통해서 서버에 요청한 후 멈추지않고 그 프로그램은 계속 돌아간다는 의미 내포

- 리로드하게되면 전체 리소스를 다시 불러오기에 불필요한 리소스 낭비가 발생하지만 **비동기를 사용한다면 필요한 부분만 불러와 사용할 수 있으므로 매우 큰 장점**



## AJAX 사용 이유

단순하게 web화면에서 무언가 부르거나 데이터를 조회하고 싶을 경우, 페이지 전체를 새로고침하지 않기위해 사용함

> http 프로토콜은 클라이언트쪽에서 request를 보내고, 서버에서 response를 받으면 이어졌던 연결이 끊기게 된다. 이후 화면 갱신을 위해 request를 하고 response를 하며 페이지 전체 갱신을 진행해야 한다. -> 엄청난 자원 낭비와 시간 낭비

:arrow_right: AJAX는 HTML 페이지 일부분만 갱신하도록 XMLHttpRequest 객체를 통해 서버에 request한다. -> JSON이나 XML형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있음



### 장점

- 웹 페이지 속도향상
- 서버의 처리가 완료될때가지 기다리지 않아도 됨
- 서버에서 data만 전송하면 되어 전체적인 코딩 양이 줄어듬
- 기존 웹에서는 불가능했던 다양한 ui를 가능케 함

### 단점

- 히스토리 관리x
- 페이지 이동없는 통신으로 보안상 문제 발생
- 연속으로 데이터 요청하면 서버 부하 증가
- XMLHttpRequest 통신의 경우, 사용자에게 아무런 진행정보를 주어지지 않음



## AJAX 진행과정

1. XMLHttpRequest Object 생성
   - Request 보낼 준비를 브라우저에게 시킴
2. Callback 함수 생성
   - 서버에서 response가 왔을 때 실행시키는 함수
   - HTML 페이지 업데이트
3. Open a request
   - 서버에서 response가 왔을 때 실행시키는 함수
   - HTML 페이지 업데이트
4. send the request



## Fetch

Ajax를 구현할 수 있는 여러 기술 중 최신 기술인 fetch! 

```js
fetch(response, init)
  .then(callback)
  .catch(callback)
```

- response : url경로, 요청 주소
- init: 설정 객체

> Init 객체 작성 예시 
>
> ```js
> const init={
>   method: 'GET',
>   headers: {
>     'Content-Type': 'application/json',
>   },
>   credentials: 'same-origin'
> };
> ```
>
> 
>
> 

### fetch API 원리 

```js
fetch('work1.html').then(function(response){
	response.text().then(function(text){
		document.querySelector('article').innerHTML = text;  
	})
})
```

- Fetch('work1.html')  : 첫번째 인자로 전달된 데이터를 서버에게 요청하는 함수
- then(function(response){ ...) : 앞에 요청한 서버의 응답 끝나면 then함수 실행.
  - 응답 올 때까지 기다리는게 아니라 then 함수 진행중