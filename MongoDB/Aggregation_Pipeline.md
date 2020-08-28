## Aggregation Pipeline

- 기존의 find() 함수로는 원하는 데이터로 가공하려면 제약이 있는데 aggregate() 함수를 이용하면 해결 가능

- mongoDB aggregation :

  - Sharding을 통해 bigdata를 저장하고, aggregation framework를 통하여 bigdata를 처리
  - documents를 grouping, filtering 등 다양한 연산을 적용해 계산된 결과 반환

  

- `{$match:{}}`   조건에 만족하는 document만 filtering

- `{$group: {_id: , : {:},    }}`   document에 대한 grouping 연산 수행 -그룹에 대한 id를 지정해야 하고, 특정 필드에 집계 연산 가능



#### 1. 기본 스테이지 소개

- `$project`  어떤 필드를 숨기고, 어떤 필드를 새로 만들지 정함

- `$group`   _id 값으로 지정된 내용이 같은 도큐먼트끼리 그룹화

- `$match`  도큐먼트를 필터링해서 반환 

- `$unwind`  입력 도큐먼트에서 배열 필드를 분해해 각 요소에 대한 도큐먼트로 분리하여 출력

- `$out`  파이프라인의 결과를 컬렉션에 기록

  

| SQL      | MongoDB Aggregation Operators |
| -------- | ----------------------------- |
| WHERE    | $match                        |
| GROUP BY | $group                        |
| HAVING   | $match                        |
| SELECT   | $project                      |
| ORDER BY | $sort                         |
| LIMIT    | $limit                        |
| SUM()    | $sum                          |
| COUNT()  | $sum                          |
| join     | $lookup                       |

*<small> \*Aggregation 함수를 사용한 예제는 Aggregation.sql , Aggregation_EX.sql 파일로 작성하여 올렸습니다.</small>*



