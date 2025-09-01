
def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

        return contents
    
def word_count(file:str):
    word_list = get_book_text(file).split()
    return len(word_list)

def letter_count(file:str):
    text = get_book_text(file).lower()
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True) 

