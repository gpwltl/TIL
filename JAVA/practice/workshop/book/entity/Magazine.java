package workshop.book.entity;

public class Magazine extends Publication{
	//변수 지정
	private String publishingPeriod;
	
	//default constructor
	public Magazine() {
		
	}
	
	// constructor overloading
	public Magazine(String title, String publishingDate, int page, int price, String publishingPeriod) {
		super(title, publishingDate, page, price);
		this.publishingPeriod=publishingPeriod;
	}

	//getter, setter
	public String getPublishingPeriod() {
		return publishingPeriod;
	}

	public void setPublishingPeriod(String publishingPeriod) {
		this.publishingPeriod = publishingPeriod;
	}
	

}
