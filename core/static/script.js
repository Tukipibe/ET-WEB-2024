async function fetchRandomBook() {
    const response = await fetch('http://openlibrary.org/search.json?q=the');
    const data = await response.json();
    const randomBook = data.docs[Math.floor(Math.random() * data.docs.length)];
    
    const bookTitle = randomBook.title || "Título no disponible";
    const bookAuthor = randomBook.author_name ? randomBook.author_name[0] : "Autor no disponible";
    const bookYear = randomBook.first_publish_year || "Año no disponible";
    const coverId = randomBook.cover_i;

    document.getElementById('book-title').textContent = bookTitle;
    document.getElementById('book-author').textContent = `Autor: ${bookAuthor}`;
    document.getElementById('book-year').textContent = `Año de publicación: ${bookYear}`;
    
    const bookCover = document.getElementById('book-cover');
    if (coverId) {
        bookCover.src = `https://covers.openlibrary.org/b/id/${coverId}-L.jpg`;
        bookCover.style.display = 'block';
    } else {
        bookCover.style.display = 'none';
    }
}
