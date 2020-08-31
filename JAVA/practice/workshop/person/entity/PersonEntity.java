package workshop.person.entity;

/**
 * Person의 정보를 담는 클래스
 * @author 윤혜지
 *
 */
public class PersonEntity {
		//변수 지정
		private String name;		
		private char gender;
		private String ssn;
		private String address;
		private String phone;
		
		//기본 생성자 생성
		public PersonEntity() {
			System.out.println("PersonEntity default constructor called...");
		}
		//constructor overloading(생성자 중복정의)
		public PersonEntity(String name, String ssn, String address, String phone) {
			setName(name);
		    setAddress(address);
		    setPhone(phone);
		    setSsn(ssn);
		}
		
		//getter method - setter method
		public String getName() {
			return name;
		}
		public void setName(String name) {
			this.name = name;
		}
		public char getGender() {
			return gender;
		}
		public void setGender(char gender) {
			this.gender = gender;
		}
		public String getSsn() {
			return ssn;
		}
		public void setSsn(String ssn) {
			if(ssn.charAt(6)=='1' || ssn.charAt(6)=='3') {
				gender = '남';
			} else if(ssn.charAt(6)=='2' || ssn.charAt(6)=='4') {
				gender = '여';
			}
		}
		public String getAddress() {
			return address;
		}
		public void setAddress(String address) {
			this.address = address;
		}
		public String getPhone() {
			return phone;
		}
		public void setPhone(String phone) {
			this.phone = phone;
		}
		
		
	
		
}
