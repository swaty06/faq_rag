 # 📚 Bookstore Chatbot with Semantic Routing

An intelligent chatbot for book-related queries that uses semantic routing to intelligently direct questions to either FAQ retrieval or SQL database queries. Built with semantic router technology and RAG (Retrieval-Augmented Generation) functionality.

## 🎯 Overview

This chatbot provides a seamless conversational experience for users looking to discover and learn about books. It intelligently routes queries between two specialized systems:

- **FAQ Route**: Handles general questions about bestselling books, recommendations, and common book-related inquiries
- **SQL Route**: Queries a structured database of mystery genre books scraped from Amazon

## ✨ Features

- **Semantic Routing**: Automatically determines the best route for each user query
- **RAG Implementation**: Combines retrieval and generation for accurate, context-aware responses
- **Dual Knowledge Sources**: 
  - CSV-based FAQ system for common questions
  - SQL database for detailed book information
- **Mystery Genre Database**: Curated collection of mystery books with metadata from Amazon
- **Natural Language Interface**: Ask questions in plain English

## 🏗️ Architecture

### Semantic Router
The chatbot uses semantic routing to classify incoming queries and direct them to the appropriate handler:

```
User Query → Semantic Router → FAQ Route OR SQL Route → Response Generation
```

### FAQ Route
- **Data Source**: CSV file containing question-answer pairs
- **Content**: Information about bestselling books, genres, recommendations
- **Use Cases**: 
  - "What are the current bestsellers?"
  - "Can you recommend popular fiction books?"
  - "What genres are trending?"

### SQL Route
- **Data Source**: SQLite/PostgreSQL database
- **Content**: Mystery genre books scraped from Amazon
- **Schema**: Book titles, authors, prices, ratings, descriptions, URLs
- **Use Cases**:
  - "Find mystery books under $15"
  - "Show me highly-rated detective novels"
  - "What mystery books are available by [author]?"

## 🛠️ Technology Stack

- **Semantic Router**: Query classification and routing
- **RAG Framework**: Retrieval-Augmented Generation for contextual responses
- **Database**: SQL (SQLite/PostgreSQL) for structured book data
- **Data Processing**: Pandas for CSV handling
- **Web Scraping**: Amazon book data collection
- **LLM Integration**: For natural language understanding and generation

## 📋 Prerequisites

```bash
python 3.8+
semantic-router
pandas
sqlalchemy
openai / anthropic (for LLM)
beautifulsoup4 (for scraping)
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bookstore-chatbot.git
cd bookstore-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-api-key"
# or
export ANTHROPIC_API_KEY="your-api-key"
```

4. Initialize the database:
```bash
python setup_database.py
```

## 📊 Data Structure

### FAQ CSV Format
```csv
question,answer
"What are the bestselling books?","Current bestsellers include..."
"How do I find book recommendations?","You can browse by genre..."
```

### SQL Database Schema
```sql
CREATE TABLE mystery_books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    price DECIMAL(10,2),
    rating DECIMAL(3,2),
    description TEXT,
    amazon_url TEXT,
    scraped_date DATE
);
```

## 💻 Usage

### Basic Usage
```python
from chatbot import BookstoreChatbot

chatbot = BookstoreChatbot()
response = chatbot.query("What are some good mystery books under $20?")
print(response)
```

### Query Examples

**FAQ Route Queries:**
- "What are the current bestselling books?"
- "Can you recommend some fiction books?"
- "What's popular in romance genre?"

**SQL Route Queries:**
- "Show me mystery books by Agatha Christie"
- "Find highly-rated mystery novels under $15"
- "What are the top-rated detective books?"

## 🔍 How RAG Works Here

The chatbot implements RAG in two ways:

1. **FAQ Retrieval**: 
   - Embeds user query and FAQ questions
   - Retrieves most relevant Q&A pairs
   - Generates response based on retrieved context

2. **SQL Retrieval**:
   - Converts natural language to SQL query
   - Retrieves relevant books from database
   - Generates natural language response with book details

## 🗂️ Project Structure

```
bookstore-chatbot/
│
├── data/
│   ├── faq_books.csv
│   └── mystery_books.db
│
├── src/
│   ├── chatbot.py
│   ├── semantic_router.py
│   ├── faq_handler.py
│   ├── sql_handler.py
│   └── rag_engine.py
│
├── scrapers/
│   └── amazon_scraper.py
│
├── setup_database.py
├── requirements.txt
└── README.md
```

## 🎨 Customization

### Adding More FAQ Data
Edit `data/faq_books.csv` and add your question-answer pairs.

### Expanding to Other Genres
Modify `scrapers/amazon_scraper.py` to scrape additional genres and update the database schema accordingly.

### Adjusting Routing Logic
Configure semantic router thresholds in `src/semantic_router.py` to fine-tune query classification.

## 🧪 Testing

```bash
python -m pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Amazon for book data source
- Semantic Router library for intelligent query routing
- Open source community for RAG frameworks

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/bookstore-chatbot](https://github.com/yourusername/bookstore-chatbot)

## 🗺️ Roadmap

- [ ] Add support for more book genres
- [ ] Implement user preference learning
- [ ] Add book cover image display
- [ ] Integration with book purchase APIs
- [ ] Multi-language support
- [ ] Voice interface integration
