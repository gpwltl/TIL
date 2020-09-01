package workshop.person.control;

import workshop.person.entity.PersonEntity;
import java.util.Scanner; 

/**
 * Person의 정보를 담는 클래스 
 * @author 윤혜지
 *
 */

//java PersonManager "여" args[0] "서울" args[1]
public class PersonManager {

	public static void main(String[] args) {
		//PersonManager 객체생성
		PersonManager pManager = new PersonManager();
		//PersonEntity 배열 생성
		PersonEntity[] persons = new PersonEntity[10];

		pManager.printTitle("@@@ 인물 정보 조회 시스템 @@@");
		pManager.printTitleLine();
		
		pManager.fillPerson(persons);
		pManager.showPerson(persons);
		
		Scanner scanGender = new Scanner(System.in);
		System.out.println("확인하고 싶은 성별을 입력해주세요(남 or 여)");
		char findGender=scanGender.next().charAt(0);
		pManager.findByGender(persons, findGender);
		pManager.printTitleLine();
		
		Scanner scanName = new Scanner(System.in);
		System.out.println("확인하고 싶은 이름을 입력해주세요.");
		String findName=scanName.next();
		pManager.showPerson(persons, findName);

	}

	/**
	 * 타이틀을 출력해주는 메소드
	 * @param title
	 */
	public void printTitle(String title) {
		System.out.println(title);

	}

	/**
	 * 밑줄 출력(=, -)
	 */
	public void printTitleLine() {
		for(int i=0; i<60; i++) {
			System.out.print("=");
		} 
		System.out.println();
	}
	public void printItemLine() {
		for(int i=0; i<60; i++) {
			System.out.print("-");
		} 
		System.out.println();
	}

	
	/**
	 * 데이터 배열에 넣어주는 메소드
	 * @param persons: PersonEntity 배열
	 */
	public void fillPerson(PersonEntity[] persons) {

		persons[0] = new PersonEntity("이성호", "7212121028102", "인천 계양구", "032-392-2932");
		persons[1] = new PersonEntity("김하늘", "7302132363217", "서울 강동구", "02-362-1932");
		persons[2] = new PersonEntity("박영수", "7503111233201", "서울 성북구", "02-887-1542");
		persons[3] = new PersonEntity("나인수", "7312041038988", "대전 유성구", "032-384-2223");
		persons[4] = new PersonEntity("홍정수", "7606221021341", "서울 양천구", "02-158-7333");
		persons[5] = new PersonEntity("이미숙", "7502142021321", "서울 강서구", "02-323-1934");
		persons[6] = new PersonEntity("박성구", "7402061023101", "서울 종로구", "02-308-0932");
		persons[7] = new PersonEntity("유성미", "7103282025101", "서울 은평구", "02-452-0939");
		persons[8] = new PersonEntity("황재현", "7806231031101", "인천 중구", "032-327-2202");
		persons[9] = new PersonEntity("최철수", "7601211025101", "인천 계양구", "032-122-7832");
	}

	/**
	 * 저장된 모든 데이터 출력해주는 메소드
	 * @param persons
	 */
	public void showPerson(PersonEntity[] persons) {
		for(PersonEntity person: persons) {
			System.out.println("[이름]\t"+person.getName()+"\t[성별]\t"+person.getGender()+"\t[전화번호]\t"+person.getPhone());
			printItemLine();
		}
	}
	
	/**
	 * 특정 인물에 대한 데이터 출력해주는 메소드
	 * @param persons
	 * @param name : 이름
	 */
	public void showPerson(PersonEntity[] persons, String name) {
		System.out.println("--이름: '"+name+"'(으)로 찾기 결과입니다.--");
		printItemLine();
		for(PersonEntity person: persons) {
			if(person.getName().equals(name)) {		
			System.out.println("[이름]\t"+person.getName()+"\n[성별]\t"+person.getGender()+"\n[전화번호]\t"+person.getPhone()+"\n[주소]\t"+person.getAddress());
			}
		}
	}
	
	
	/**
	 * 해당 성별이 몇명인지 알아보는 메소드
	 * @param persons
	 * @param gender : 성별
	 */
	public void findByGender(PersonEntity[] persons, char gender) {
		int count=0;
		for(PersonEntity person: persons) {
			if(person.getGender()==gender)
				count++;
		} 
		System.out.println("성별 : '"+gender+"'"+ "는 "+count+"명 입니다.");
		
	}

}
