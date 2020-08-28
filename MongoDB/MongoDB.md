# MongoDB

### 1. MongoDB란?

JSON 기반의 Document 기반 데이터 관리

#### 1-1. 특징

- 모든 데이터가 JSON 형태로 저장, 스키마 존재x
- 다양한 인덱싱 제공
- 데이터 복제를 통해 가용성 향상
- 여러 서버에 데이터를 나누는 scale-out 가능
- 다양한 쿼리 제공
- 고성능의 atomic operation 지원
- 맵리듀스 지원
- 별도 스토리지 엔진을 통해 파일을 저장 가능



#### 1-2. 데이터 구조

| SQL      | MongoDB    |
| -------- | ---------- |
| database | database   |
| table    | collection |
| row      | document   |
| column   | field      |
| index    | index      |



### 2. MongoDB 시작하기

#### 1) Database Create

`Create database` -> database의 이름을  설정

> **Collections, Function, Users**의 파일 세개가 생성됨

#### 2) Collection Create 

`Create collection` -> collection 이름 설정

> collection 생성됨 

#### 3) Insert Document

`Insert collection` 에 아래와 같은 값을 넣어줌

```sql
{"id":"01", "language":"java", "edition": { "first": "1st", "second":"2nd", "third":"third" }}
```

> 해당 collection을 들어가보면 key들이 생성된 것을 확인할 수 있음
>
> > _id가 생성된 것을 확인할 수 있는데, 이는 내부에서 생성되는 랜덤의 id값 (일종의 PK)

* 각각의 Document마다 Field의 개수가 달라도 상관없음



---

### 2-1. Shell 이용하여 MongoDB 생성

- 데이터 베이스 생성

  - `use mymongo_db`

- 데이터 베이스 현황 확인

  - `db.stats()`

- collection 생성 및 삭제 

  - 생성: `db.createCollection("employees", {capped: true, size:10000})`

    > capped: true -> 최초 제한된 크기로 생성된 공간에서만 데이터를 저장하는 설정
    >
    > (고성능, 기존 공간 재사용, 일정시간만 저장)
    >
    > > - PK(_id)가 자동생성되어 별도의 컬럼을 만들 필요가 없음
    > >
    > > - 컬럼마다 데이터 타입을 지정할 필요 없음(컬럼값이 기본 형태)

  - capped 확인 : `db.employees.isCapped()`

  - 삭제: `db.employees.drop()`

- collection 확인

  - 가지고 있는 collection 모두 확인: `show collections`
  - 해당 collection만 확인: `db.employees.stats()`

- collection 이름 변경

  - `db.employees.renameCollection("emp")`



### 3. 데이터 CRUD

#### 1. Create

> Document 

- `db.emp.insertOne()` : 한개의 document 생성
- `db.emp.insertMany()` : 여러개 document 생성

```sql
db.emp.insertOne(
	{name: "yoon", age: 24, status: "pending"}
)
```

```sql
db.emp.insertMany([
	{user_id: "abc001", age: 25, status: "B"},
    {user_id: "abc002", age: 22, status: "A"},
    {user_id: "abc003", age: 28, status: "A"},
    {user_id: "abc004", age: 26, status: "B"},
])
```

​	

#### 2. Read

> Document 읽기 (검색)

- `db.emp.findOne()` : 매칭되는 한 개의 document 검색
- `db.emp.find()` :  매칭되는 여러개의 document 검색



- find() / findOne() 명령과 sql문 비교

```sql
--select * from emp
db.emp.find()

--select _id, user_id, status from emp
db.emp.find({ }, {user_id: 1, status: 1})

--select user_id, status from emp
db.emp.find({ }, {user_id: 1, status: 1, _id: 0})

--select * from emp where status='A'
db.emp.find({status: "A"})

--select user_id, status from emp where status='A'
db.emp.find({status: "A"}, {user_id:1, status:1, _id:0})

--select * from emp where status='A' and age=50
db.emp.find({status: "A", age: 50})

--select * from emp where status='A' or age=50
db.emp.find({$or: [{status:"A"}, {age:50}]})
```



- 비교 연산자

  | mongo 연산자 | 연산자 |
  | ------------ | ------ |
  | $eq          | =      |
  | $gt          | >      |
  | $gte         | \>=    |
  | $lt          | <      |
  | $lte         | <=     |
  | $ne          | !=     |
  | $in          | in     |
  | $nin         | not in |
  | $regex       | like   |

  

  - 예제

  ```sql
  --select * from emp where age > 25
  db.emp.find({age: {$gt: 25}})
  
  --select * from emp where user_id like "%bc%"
  db.emp.find({user_id: {$regex: /bc/ }})
  --select * from emp where user_id like "bc%"
  db.emp.find({user_id: {$regex: /^bc/}})
  --select * from emp where user_id like "%bc"
  db.emp.find({user_id: {$regex: /bc$/}})
  
  --select * from emp where status="A" order by user_id asc
  db.emp.find({status:"A"}).sort({user_id:1})
  --select * from emp hwere status="A" order by user_id desc
  db.emp.find({status:"A"}).sort({user_id:-1})
  
  --select count(*) from emp
  db.emp.count()
  --select count(*) from emp where age>30
  db.emp.count({age: {$gt: 30}})
  
  --select distinct(status) from emp
  db.emp.aggregate([{$group: {_id: "$status"}}])
  
  --select * from emp limit 1 
  db.emp.findOne()
  db.emp.find().limit(1)
  ```




#### Update

> Document Update

- `db.emp.updateOne()` : 매칭되는 한 개의 document 업데이트
- `db.emp.updateMany()` : 매칭되는 여러 개의 document 업데이트



- `$set` : 필드 값 설정
- `$inc` : 필드 값을 증가/감소



- updateOne() / updateMany() 명령과 sql 비교

```sql
--update emp set status="C" where age>45
db.emp.updateMany({age: {$gt: 45}}, {$set: {status: "C"}})

--updeat emp set age = age+3 where status="A"
db.emp.updateMany({status: "A"}, {$inc: {age: 3}})
```



#### Delete

> Document 삭제

- `db.emp.deleteOne()`  : 매칭되는 한 개의 document 삭제

- `db.emp.deleteMany()` : 매칭되는 여러 document 삭제

  

- deleteOne() / deleteMany() 명령과 sql 비교

```sql
--delete from people
db.emp.deleteMany({})

--delete from emp where status="D"
db.emp.deleteMany({status: "D"})
```