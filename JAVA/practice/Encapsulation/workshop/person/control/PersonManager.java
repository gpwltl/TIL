package workshop.person.control;

import workshop.person.entity.PersonEntity;
import java.util.Scanner; 

/**
 * Person�� ������ ��� Ŭ���� 
 * @author ������
 *
 */

//java PersonManager "��" args[0] "����" args[1]
public class PersonManager {

	public static void main(String[] args) {
		//PersonManager ��ü����
		PersonManager pManager = new PersonManager();
		//PersonEntity �迭 ����
		PersonEntity[] persons = new PersonEntity[10];

		pManager.printTitle("@@@ �ι� ���� ��ȸ �ý��� @@@");
		pManager.printTitleLine();
		
		pManager.fillPerson(persons);
		pManager.showPerson(persons);
		
		Scanner scanGender = new Scanner(System.in);
		System.out.println("Ȯ���ϰ� ���� ������ �Է����ּ���(�� or ��)");
		char findGender=scanGender.next().charAt(0);
		pManager.findByGender(persons, findGender);
		pManager.printTitleLine();
		
		Scanner scanName = new Scanner(System.in);
		System.out.println("Ȯ���ϰ� ���� �̸��� �Է����ּ���.");
		String findName=scanName.next();
		pManager.showPerson(persons, findName);

	}

	/**
	 * Ÿ��Ʋ�� ������ִ� �޼ҵ�
	 * @param title
	 */
	public void printTitle(String title) {
		System.out.println(title);

	}

	/**
	 * ���� ���(=, -)
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
	 * ������ �迭�� �־��ִ� �޼ҵ�
	 * @param persons: PersonEntity �迭
	 */
	public void fillPerson(PersonEntity[] persons) {

		persons[0] = new PersonEntity("�̼�ȣ", "7212121028102", "��õ ��籸", "032-392-2932");
		persons[1] = new PersonEntity("���ϴ�", "7302132363217", "���� ������", "02-362-1932");
		persons[2] = new PersonEntity("�ڿ���", "7503111233201", "���� ���ϱ�", "02-887-1542");
		persons[3] = new PersonEntity("���μ�", "7312041038988", "���� ������", "032-384-2223");
		persons[4] = new PersonEntity("ȫ����", "7606221021341", "���� ��õ��", "02-158-7333");
		persons[5] = new PersonEntity("�̹̼�", "7502142021321", "���� ������", "02-323-1934");
		persons[6] = new PersonEntity("�ڼ���", "7402061023101", "���� ���α�", "02-308-0932");
		persons[7] = new PersonEntity("������", "7103282025101", "���� ����", "02-452-0939");
		persons[8] = new PersonEntity("Ȳ����", "7806231031101", "��õ �߱�", "032-327-2202");
		persons[9] = new PersonEntity("��ö��", "7601211025101", "��õ ��籸", "032-122-7832");
	}

	/**
	 * ����� ��� ������ ������ִ� �޼ҵ�
	 * @param persons
	 */
	public void showPerson(PersonEntity[] persons) {
		for(PersonEntity person: persons) {
			System.out.println("[�̸�]\t"+person.getName()+"\t[����]\t"+person.getGender()+"\t[��ȭ��ȣ]\t"+person.getPhone());
			printItemLine();
		}
	}
	
	/**
	 * Ư�� �ι��� ���� ������ ������ִ� �޼ҵ�
	 * @param persons
	 * @param name : �̸�
	 */
	public void showPerson(PersonEntity[] persons, String name) {
		System.out.println("--�̸�: '"+name+"'(��)�� ã�� ����Դϴ�.--");
		printItemLine();
		for(PersonEntity person: persons) {
			if(person.getName().equals(name)) {		
			System.out.println("[�̸�]\t"+person.getName()+"\n[����]\t"+person.getGender()+"\n[��ȭ��ȣ]\t"+person.getPhone()+"\n[�ּ�]\t"+person.getAddress());
			}
		}
	}
	
	
	/**
	 * �ش� ������ ������� �˾ƺ��� �޼ҵ�
	 * @param persons
	 * @param gender : ����
	 */
	public void findByGender(PersonEntity[] persons, char gender) {
		int count=0;
		for(PersonEntity person: persons) {
			if(person.getGender()==gender)
				count++;
		} 
		System.out.println("���� : '"+gender+"'"+ "�� "+count+"�� �Դϴ�.");
		
	}

}
