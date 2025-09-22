# Student_Study_Assistant

**Student_Study_Assistant** is a command-line tool that leverages Groq’s Large Language Model (LLM) to answer students’ questions about the contents of a text-based study document. By using intelligent text chunking and keyword matching, it provides focused, context-rich answers directly from relevant document sections.

---

## Features

- Loads study material from a local `.txt` file.
- Chunks large documents into overlapping sections for context preservation.
- Intelligently selects the most relevant section of text based on user questions.
- Formats and sends prompts to Groq’s LLM API (Llama-3.3-70b).
- Displays targeted AI-generated answers to user questions.

---

## How It Works

1. **Document Loading:**  
   Loads the content from `document.txt` or a file path provided in code, reading the entire file into a single string.

2. **Text Chunking with Overlap:**  
   Splits the document into chunks (default 300 words, with 50-word overlap) to ensure context-rich sections for retrieval.

3. **Keyword-Based Chunk Retrieval:**  
   Analyzes user questions, finds the chunk with the highest overlap between question keywords and chunk content.

4. **Prompt Formatting:**  
   Creates a prompt with the selected chunk as context and the user’s question, suitable for LLM processing.

5. **API Query to Groq LLM:**  
   Sends the prompt to Groq’s Llama-3.3-70b via the Groq API and retrieves the AI-generated answer.

6. **Result Display:**  
   Presents the answer directly on the terminal.

---

## Setup Instructions

1. **Prerequisites:**
   - Python 3.7+
   - groq Python client library
   - python-dotenv for API key management
   - An active Groq API Key (add to `.env` as `GROQ_API_KEY`)

2. **Install Requirements:**
    - `pip install groq python-dotenv`

3. **Environment Variable:**  
Create a `.env` file in your project directory with this content:
    - `GROQ_API_KEY = your_groq_api_key_here`

4. **Prepare Study Material:**  
Place your document as `document.txt` in the working directory, or adjust the file path in the script.

5. **Run the Assistant:**
    - `python your_script.py`

- Enter your study-related question at the prompt.

---

## Usage Example
Loading Document...

Splitting into chunks...

Enter your question: What are the main points of chapter three?

Answer:

<AI-generated answer based on the best-matching section>


---

## Project Structure

| File            | Purpose                                              |
|-----------------|-----------------------------------------------------|
| `your_script.py`| Main code: text processing, chunking, LLM querying  |
| `document.txt`  | Text document containing study material             |
| `.env`          | Holds the Groq API Key                              |

---

## Key Functions

- `load_document(file_path)`: Handles file reading.
- `chunk_text(text, chunk_size, overlap)`: Chunks document for context.
- `score_chunk(chunk, keywords)`: Scores chunk relevance.
- `get_best_chunk(chunks, question)`: Retrieves best chunk by score.
- `build_prompt(context, question)`: Creates prompt for Groq LLM.
- `get_answer_from_groq(prompt, api_key)`: Sends prompt and gets response.
- `get_api_key()`: Loads API key from environment.

---

## Notes

- The assistant currently matches based on exact keyword overlaps. For broader semantic search or multilingual support, consider integrating advanced retrieval (embeddings, vector search).
- Make sure the document is in clear, well-separated paragraphs for best chunking results.
- The script is easily customizable for other LLM providers or alternative file types.

---

## License

This project is educational and intended for student-driven use, demonstration, and non-commercial research.

---

## Contact

For improvements, suggestions, or contributions, feel free to open an issue or contact the maintainer.

---

**Student_Study_Assistant helps students quickly find precise, contextual answers from dense study material using advanced LLM technology.**

