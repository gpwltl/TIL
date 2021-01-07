# Promise

## 프로미스 필요한 이유

promise는 주로 서버에서 받아온 데이터를 화면에 표시할 때 사용함

> - 웹 애플리케이션을 구현할 때 서버에서 데이터를 요청하고 받아오기 위해 api를 사용함 
>
> >  $.get('url 주소/product/1', function(response){ })
> >
> > 서버에다가 '데이터 하나 보내주세요'라는 요청을 보내고 데이터를 받아오기 전에 마치 데이터를 받아온 것 마냥 화면에 데이터를 표시하려고 하면 오류 발생!! `빈화면 뜰 것 -> 이를 해결하기 위해 promise 사용`



## Promise 코드

```js
function getData(){
  return new Promise(function(resolve, reject){
    $.get('url/product/1', function(response){
      if(response){
        resolve(response);
      }
      reject(new Error("Request is failed"));
    })
  })
}

getData().then(function(data){
  console.log(data);
}).catch(function(err){
  console.log(err);
})
```

> 이해가 안된다면 아래 3가지 상태를 읽고 다시 살펴볼 것 !

### 프로미스 3가지 상태 

`new Promise()` : 프로미스를 생성하고 종료될 때까지 3가지 상태를 가짐

- Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태
- Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과값을 반환해준 상태
- Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태



#### Pending(대기)

`new Promise()` => 메서드 호출되면 대기 상태

- 메서드 호출 시 **콜백 함수**를 선언할 수 있고 이때 인자는 `resolve`, `reject`

  `new Promise(function(resolve, reject){});`



#### Fulfilled(이행)

콜백함수의 인자 `resolve` => 실행하면 이행 상태

```javascript
new Promise(function(resolve, reject){
	resolve();
})
```

- 이행상태가 되면 `then()` 을 이용하여 처리 결과값 받을 수 있음

  ```js
  function getData(){
    return new Promise(function(resolve, reject){
      var data=100;
      resolve(data);
    });
  }
  
  //resolve()의 결과 값 data를 resolvedData로 받음
  getData().then(function(resolvedData){
    console.log(resolvedData);	//100
  });
  ```

  

#### Rejected(실패)

콜백함수의 인자 `reject` => 호출하면 실패 상태

```javascript
new Promise(function(resolve, reject){
	reject();
})
```

- 실패상태가 되면 실패한 이유(실패 처리값)를 `catch()`로 받을 수 있음

```js
function getData(){
  return new Promise(function(resolve, reject){
    reject(new Error("Request is failed"));
  });
}

//reject()의 결과 값 Error를 err 받음
getData().then().catch(function(err){
  console.log(err);		//Error: Request is failed
});
```

![image](https://user-images.githubusercontent.com/44856614/103854232-5055b000-50f3-11eb-949f-ce00c979f5de.png)



## Promise Chaining(연결)

```javascript
var userInfo={
  id: 'test@abc.com',
  pw: '****'
};

function parseValue(){
  return new Promise({})
}
function auth(){
  return new Promise({})
}
function display(){
  return new Promise({})
}

getDate(userInfo)
  .then(parseValue)
  .then(auth)
  .then(display);
```



## Promise 에러 처리 방법

```js
function getData(){
  return new Promise(function(resolve, reject){
    reject('failed');
  })
}

//1. then() 두번째 인자로
getData().then(function(){
  
}, function(err){
  console.log(err);
})

//2. catch()로
getData().then().catch(function(err){
  console.log(err)
})
```



#### 1. then() 두 번째 인자로 에러처리

```js
getData().then(
	handleSuccess,
  handleError
);
```

#### 2. catch() 이용 :star2:

**가급적 catch()를 사용해서 에러처리 할 것 !!** (더 많은 예외처리를 해결하기 위해)

```js
getData().then().catch();
```



## Promise all/race

### 1. Promise.All

동기화처리 할 Promise를 **묶어서 한 번에 실행**

```js
const pm1 = new Promise((resolve, reject)=>{
  resolve('즉시 호출')
});
const pm2 = new Promise((resolve, reject)=>{
  setTimeout(()=>resolve('3초뒤 호출'), 3000)
});

Promise.all([pm1, pm2]).then(v=>console.log(v))	//['즉시 호출', '3초뒤 호출']
```



### 2. Promise.race

Promise들 중에서 제일 빠른 하나만 실행

```js
const pm3 = new Promise((resolve, reject)=>{
  setTimeout(()=> resolve(2000), 2000)
});
const pm4 = new Promise((resolve, reject)=>{
  setTimeout(()=> resolve(), 0)
});

const res = Promise.race([pm3, pm4]).then(v=> console.log(v))	//0
```

