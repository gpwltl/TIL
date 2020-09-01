package workshop.book.entity;

public class Publication {
	// 변수 지정
	private String title;
	private String publishingDate;
	private int page;
	private int price;

	//default constructor
	public Publication() {

	}

	// constructor overloading
	public Publication(String title, String publishingDate, int page, int price) {
				setTitle(title);
				setPublishingDate(publishingDate);
				setPage(page);
				setPrice(price);
			    
	}

	//getter, setter
	public String toString() {
		return title;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getPublishingDate() {
		return publishingDate;
	}

	public void setPublishingDate(String publishingDate) {
		this.publishingDate = publishingDate;
	}

	public int getPage() {
		return page;
	}

	public void setPage(int page) {
		this.page = page;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}
	
	
}
