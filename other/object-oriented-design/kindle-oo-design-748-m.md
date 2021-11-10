# Kindle OO Design 748 (M)

## Problem



Design Kindle, which can support `3` type of book format: `PDF`, `MOBI` and `EPUB`.

* Consider using ENUM for book format.
* Consider using simple factory to create reader for each format.

Example

Input:

```
readBook("EPUB")readBook("PDF")readBook("MOBI")
```

Output:

```
Using EPUB reader, book content is: epubUsing PDF reader, book content is: pdfUsing MOBI reader, book content is: mobi
```

## Procedure

### Clarify:

* Don't need to consider a different version
* Don't need to consider memory / book's size
* Need to support **pdf**, **epub** and **mobi** format

### Use Cases

* Upload book
* Download book
* Read book
* Remove book

### Factory Design&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-07-15 at 1.10.57 PM.png>)

## Solution&#x20;

{% tabs %}
{% tab title="Java" %}
```java
import java.util.ArrayList;
import java.util.List;

public class Kindle {
	private List<Book> books;
	private EBookReaderFactory readerFactory;

	public Kindle() {
		//write your code here
		books = new ArrayList<>();
		readerFactory = new EBookReaderFactory();
	}

	public String readBook(Book book) throws Exception {
		//write your code here
		EBookReader reader = readerFactory.createReader(book);
		if (reader == null) {
			throw new Exception("Can't read this format");
		}
		return reader.displayReaderType() + ", book content is: " + reader.readBook();
	}

	public void downloadBook(Book b) {
		//write your code here
		books.add(b);
	}

	public void uploadBook(Book b) {
		//write your code here
		books.add(b);
	}

	public void deleteBook(Book b) {
		//write your code here
		books.remove(b);
	}
}

enum Format {
	EPUB("epub"), PDF("pdf"), MOBI("mobi");

	private String content;

	Format(String content) {
		this.content = content;
	}

	public String getContent() {
		return content;
	}
}

class Book {
	private Format format;

	public Book(Format format) {
		this.format = format;
	}

	public Format getFormat() {
		return format;
	}
}

abstract class EBookReader {
	
	protected Book book;
	
	public EBookReader(Book b){
		this.book = b;
	}
	
	public abstract String readBook();
	public abstract String displayReaderType();
}

class EBookReaderFactory {

	public EBookReader createReader(Book b) {
		//write your code here
		if (b.getFormat() == Format.EPUB) {
			return new EpubReader(b);
		} else if (b.getFormat() == Format.MOBI) {
			return new MobiReader(b);
		} else if (b.getFormat() == Format.PDF) {
			return new PdfReader(b);
		} else
		    return null;
	}
}

class EpubReader extends EBookReader{

	public EpubReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		//write your code here
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using EPUB reader";
		
	}
}

class MobiReader extends EBookReader {

	public MobiReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		//write your code here
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using MOBI reader";
	}

}
class PdfReader extends EBookReader{

	public PdfReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		//write your code here
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using PDF reader";
	}
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: N/A**
* **Space Complexity: N/A**
