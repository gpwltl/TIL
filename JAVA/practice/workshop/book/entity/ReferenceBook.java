package workshop.book.entity;

public class ReferenceBook extends Publication {
	// 변수 지정
	private String field;

	// default constructor
	public ReferenceBook() {

	}

	// constructor overloading
	public ReferenceBook(String title, String publishingDate, int page, int price, String field) {
		super(title, publishingDate, page, price);
		this.field = field;
	}

	// getter, setter
	public String getField() {
		return field;
	}

	public void setField(String field) {
		this.field = field;
	}

}