# Spring Boot Web MVC

Model, View, Controller의 약자로 사용자 인터페이스와 비즈니스 로직을 분리하여 웹 개발을 하기 위해 사용

- Model: 데이터로 애플리케이션 정보 나타내기
- View: 화면으로 사용자에게 보여주는 인터페이스
- Controller: 비즈니스 로직과 모델, 뷰 간 상호관계의 조정자 역할



## 1. RestController 

### :white_check_mark: JSON

1. Entity와 Repository 

- `src/main ~ /entity/User.java` 에 Entity를 설정
  - \+ getter/setter 해줄 것

```java
@Entity 
public class User {  
    @Id  
    @GeneratedValue  
    private Long id;  
    @Column  
    private String name;  
    @Column(unique=true)  
    private String email; 
}
```

- `src/main ~ /repository/UserRepository.java`에 Repository 설정

```java
public interface UserRepository extends JpaRepository<User, Long>{     Optional<User> findByName(String name); }
```



2. Controller

- `src/main ~ /controller/RestUserController.java`에 RestController 설정

```java
@RestController
public class RestUserController {
    
    //오토와이드 대신 기본생성자에서 가져와 주입
    private final UserRepository repository;
    public RestUserController(UserRepository repository) {
      this.repository = repository;
   }

   //1. insert-save-findAll
   @PostMapping("/users")
   public User insert(@RequestBody User addUser) {
      return repository.save(addUser);//insert하고 바로 save
   }
   @GetMapping("/users")
   public List<User> getUsers(){
      return repository.findAll();
   }
    

    //2. update
    @PutMapping("/users/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User userDetail) {
      //값 조회
      User user = repository.findById(id).orElseThrow(() -> new ResourceNotFoundException("User", "Id", id));//repository.findById(id)이 자체가 옵셔널이기 때문에 바로 붙일 수 있다.
        
      //값을 변경
      user.setName(userDetail.getName());
      user.setEmail(userDetail.getEmail());
      //DB에 save() 변경된 유저를 받아서 그 유저를 반환
      User updateUser = repository.save(user);
      return updateUser;
   }

    
    //3. delete
	@DeleteMapping("/users/{id}")
    public ResponseEntity<?> deleteUser(@PathVariable Lond id){
        Optional<User> optional = repository.findById(id);
        //요청한id와 매핑하는 User가 없는 경우, java11 추가
        if(optional.isEmpty()){
            return new ResponseEntity<>("요청한 User가 없습니다.", HttpStatus.NOT_FOUND);
        }
        //DB에서 삭제
        repository.deleteById(id);
        return new ResponseEntity<>(id+"User가 삭제됨", HttpStatus.OK);
    }
}
```



3. 예외처리 - 사용자 정의 Exception 클래스
   `src/main ~ /exception/ResourceNotFoundException.java`

```java
@ResponseStatus(value = HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
	private String resourceName;
	private String fieldName;
	private Object fieldValue;

	public ResourceNotFoundException(String resourceName, String fieldName, Object fieldValue) {
		super(String.format("%s not found with %s : '%s'", resourceName, fieldName, fieldValue));
		this.resourceName = resourceName;
		this.fieldName = fieldName;
		this.fieldValue = fieldValue;
	}

	public String getResourceName() {
		return resourceName;
	}

	public String getFieldName() {
		return fieldName;
	}

	public Object getFieldValue() {
		return fieldValue;
	}
}
```



###  :white_check_mark:XML

1. 의존성 추가

   ```xml
   <dependency>
    	<groupId>com.fasterxml.jackson.dataformat</groupId>
    	<artifactId>jackson-dataformat-xml</artifactId>
   	<version>2.9.6</version>
   </dependency>
   ```



2. Entity 설정 - `src/main ~ /entity/User.java`

```java
@Entity
public class User implements Serializable {
	private static final long serialVersionUID = 21L;
	@Id
	@GeneratedValue
	@JacksonXmlProperty(isAttribute = true)
	private Long id;
	@JacksonXmlProperty
 	private String name;
	@JacksonXmlProperty
 	private String email;
}
```

​						-  `src/main ~ /entity/Users.java`

```java
@JacksonXmlRootElement
public class Users implements Serializable{
	private static final long serialVersionUID = 22L;
	@JacksonXmlProperty(localName="User")
	@JacksonXmlElementWrapper(useWrapping=false)
	private List<User> users = new ArrayList<>();
	public void setUsers(List<User> users) {
		this.users = users;
	}
	public List<User> getUsers() {
		return users;
	}
}

```



3. Controller.java -  기존의 `src/main ~ /controller/RestUserController.java` 에서 수정-추가

```java
@RequestMapping(value = "/usersXml", produces = { "application/xml" })
public Users getUsersXml() { //User를 사용하는 것이 아닌 Users에서 가져옴
	Users userXml = new Users();
	userXml.setUsers(repository.findAll());
	return userXml;	
}
```



###  :heavy_check_mark: 정적 리소스 맵핑 커스터마이징

WebMvcConfigurer의 `addResourceHandlers `메서드로 커스터마이징하여 Spring MVC가 제공하는 기본 리소스 설정을 그대로 유지하면서 리소스 맵핑 설정 추가

- ResourceHandlers를 통해 리소스 위치와 이 리소스와 매칭될 url을 등록
- setCachePeriod는 캐시를 얼마나 지속할 지 정하는 메서드 (디폴트 - 20초)



### :heavy_check_mark: ​webjar

jQuery문 사용 가능. Maven에서 다운받거나 webjars-locator-core 의존성을 추가한다.



### :heavy_check_mark: favicon

 https://favicon.io/favicon-generator/  

해당 사이트에 들어가서 원하는 형태의 파비콘을 만들어서 다운로드 
-> 다운로드 파일에서 favicon.ico 을 resource/**static** 폴더에 넣어준다. 