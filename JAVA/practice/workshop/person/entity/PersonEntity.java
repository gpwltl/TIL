package workshop.person.entity;

/**
 * Person�� ������ ��� Ŭ����
 * @author ������
 *
 */
public class PersonEntity {
		//���� ����
		private String name;		
		private char gender;
		private String ssn;
		private String address;
		private String phone;
		
		//�⺻ ������ ����
		public PersonEntity() {
			System.out.println("PersonEntity default constructor called...");
		}
		//constructor overloading(������ �ߺ�����)
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
				gender = '��';
			} else if(ssn.charAt(6)=='2' || ssn.charAt(6)=='4') {
				gender = '��';
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
