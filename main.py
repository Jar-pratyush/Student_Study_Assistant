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

