from groq import Groq

def load_document(file_path):
    """
    Load the text from a file and return its content.

    Args: 
        file_path (str): Path to the text file.

    Returns:
        str : Entire file content as a single string
    """
    try:
        with open(file_path,'r') as file:
            content = file.read() 
        return content
    except FileNotFoundError:
        return f"Error : The file {file_path} you're looking for cannot be found."
    except Exception as e:
        return f"An unknow error {e} occured. Please try again."

def chunk_text(text,chunk_size=300,overlap=50):
    """
    Split the text into chunks of specified size with overlap.
    
    Args:
        text (str): The full text of the document.
        chunk_size (int): Maximum number of words per chunk.
        overlap (int): Number of overlapping words between chunks.

    Returns:
        list: List of chunks of text (each as a string).
    """

    words = text.split()
    chunks = []
    i = 0
    n = len(words)
    while i<n:
        chunk_words = words[i:i+chunk_size]
        if not chunk_words:
            break
        chunks.append(" ".join(chunk_words))
        i+=chunk_size-overlap
    return chunks

def score_chunk(chunk,keyowords):
    """
    Computes a score for a given chunk based on the overlapping words with thep passed set of keywords.

    Args:
        chunk (str): A text chunk.
        keywords (set): Set of keywords from the qusetion.
    
    Returns:
        int: Number of overlapping words.
    """
    chunk_words = set(chunk.lower.split())
    return len(chunk_words & keyowords)

def get_best_chunk(chunks,question):
    """
    Select the chunk that best matches the question.

    Args:
        chunks (list): List of text chunks.
        question (str): User's input question.
    
    Returns: 
        str: The chunk with the highest keywords overlap.
    """
    best_chunk = None
    best_score = -1
    keywords = set(question.lower().split())
    for chunk in chunks:
        score = score_chunk(chunk,keywords)
        if score>best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk

def build_prompt(context,question):
    """
    Formatting the prompt with the context and question from the user.

    Args:
        context (str): Best-Matching text chunk.
        questions (str): User's input question.
    
    Returns:
        str: Prompt string formatted for the LLM.
    """
    return f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"    

def get_answer_from_groq(prompt,api_key):
    """
    Send the prompt to groq API and return the model's answer.

    Args:
        prompt (str): The input prompt containing context + question.
        api_key (str): Groq API key either built in through env or provided directly by the user.
    
    Returns:
        str: Model-Generated Answer.
    """
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"user","content":prompt}
        ],
        model = "llama-3.3-70b-versatile",
        temperature = 0.3,
        max_completion_tokens = 512
    )
    return chat_completion.choices[0].message.content

def get_api_key():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    return api_key

if __name__ == "__main__":
    print("Loading Document...")
    doc_content = load_document("document.txt")

    print("Splitting into chunks...")
    chunks = chunk_text(doc_content)

    # Ask the user question
    question = input("Enter your question: ").lower()

    # Find the best chunk
    best_chunk = get_best_chunk(chunks,question)

    # Bulild the prompt
    prompt = build_prompt(best_chunk,question)

    # Retrieve the API key
    api_key = get_api_key()

    # Call Groq for reply
    try:
        reply = get_answer_from_groq(prompt,api_key)
        print("\nAnswer: ")
        print(reply.strip())
    except Exception as e:
         print(f"An unexpected error {e} occured. Please try again.")

