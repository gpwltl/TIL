package workshop.person.control;

import chap03.types.referencetype.MyDate;
import workshop.person.entity.PersonEntity;

public class PersonManager {

	public static void main(String[] args) {
		PersonManager pManager = new PersonManager();
		PersonEntity[] persons = new PersonEntity[10];

		pManager.printTitle("@@@ �ι� ���� ��ȸ �ý��� @@@");
		pManager.printTitleLine();
		
		pManager.fillPerson(persons);
		pManager.showPerson(persons);
		
		pManager.findByGender(persons, '��');
		pManager.printTitleLine();
		
		pManager.showPerson(persons, "���ϴ�");

	}

	public void printTitle(String title) {
		System.out.println(title);

	}

	public void printTitleLine() {
		System.out.println("====================================================");
	}

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

	public void showPerson(PersonEntity[] persons) {
		for(PersonEntity person: persons) {
			System.out.println("[�̸�]\t"+person.getName()+"\t[����]\t"+person.getGender()+"\t[��ȭ��ȣ]\t"+person.getPhone());
			System.out.println("----------------------------------------------------");
		}
	}
	
	public void showPerson(PersonEntity[] persons, String name) {
		System.out.println("--�̸�: '"+name+"'(��)�� ã�� ����Դϴ�.");
		System.out.println("----------------------------------------------------");
		for(int i=0; i<persons.length; i++) {
			if(persons[i].getName() == name) {
			System.out.println("[�̸�]\t"+persons[i].getName()+"\n[����]\t"+persons[i].getGender()+"\n[��ȭ��ȣ]\t"+persons[i].getPhone()+"\n[�ּ�]\t"+persons[i].getAddress());
			}
		}
	}
	
	public void findByGender(PersonEntity[] persons, char gender) {
		int count=0;
		for(int i=0; i<persons.length; i++) {
			if(persons[i].getGender() == gender)
				count++;
		} System.out.println("���� : '"+gender+"'"
				+ "�� "+count+"�� �Դϴ�.");
		
	}
	
	

}
