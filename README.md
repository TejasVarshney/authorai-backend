# AuthorAI Backend

A FastAPI backend service that generates AI-powered books using Google's Gemini model. This service works in conjunction with the [AuthorAI Frontend](https://github.com/TejasVarshney/authorai).

## Features

- Book content generation using Google's Gemini AI model
- Chapter-wise content organization
- JSON and Markdown file generation
- Caching support for generated content
- Cross-origin resource sharing (CORS) enabled

## Tech Stack

- Python 3.x
- FastAPI
- Google Gemini AI
- Python-dotenv

## Project Structure

```
althor-backend/
├── bookGeneration.py    # Handles full book generation
├── contentGeneration.py # Generates content structure
├── file_handling.py    # File I/O operations
├── main.py            # FastAPI server
├── pageGeneration.py  # Page content generation
├── requirements.txt   # Dependencies
└── cache/            # Generated content storage
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd althor-backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the server:
```bash
uvicorn main:app --reload
```

## API Endpoints

### POST /
Generate a book based on the provided topic.

Request body:
```json
"your_book_topic"
```

Response:
```json
{
    "title": "Book Title",
    "total_pages": number,
    "total_chapters": number,
    "chapters": [...],
    "category": "Fiction|Non-Fiction"
}
```

## Frontend Repository

The frontend application is available at [AuthorAI Frontend](https://github.com/TejasVarshney/authorai).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
