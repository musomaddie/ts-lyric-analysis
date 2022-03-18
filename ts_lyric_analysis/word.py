from functools import total_ordering
from util import remove_punctuation

# The docs mention that using total_ordering may take significantly more time. 
# If this becomes an issue replace with the implementation of the rich
# comparison methods

@total_ordering
class Word:
    """
    Just containing all the information to start with - not going with a linked
    list approach more as a container as python lists are quite versatile and so
    I have to do less manual work myself.

        Parameters:
            original_word (string): the word as it originally appeared in the
                lyrics
            formatted_word (string): the word formatted to assist with matching.
                i.e. in lower case with punctuation removed
            is_line_break (bool): is this word a special line break character
            duplicates (list<Word): a list containing all the Word objects that
                are the same as this one within the same song.
            parent (Word): initially None, only used if this word is a duplicate
                of another in the same song to link back to it. (TODO: not
                strictly sure if this is actually necessary - if I just updates
                duplicates when I find a match I shouldn't need to refer back to
                parent at any point.

        Methods:
            add_duplicate(Word): marks the word as a duplicate of this one.
    """

    def __init__(self, word, is_line_break=False, is_paragraph_break=False):
        """ Creates a new Word object using the provided word. If is_line_break
        is true, then the word is set to an empty string. 

            Parameters:
                word (str): the word of this word object.
                (optional) is_line_break (bool): if this 'word' is a line break
                (optional) is_paragraph_break (bool): is this 'word' a paragraph
                break.
        """

        self.is_line_break = is_line_break
        self.is_paragraph_break = is_paragraph_break
        # TODO: I lowkey kinda hate this class layout but that's ok.
        if is_line_break or is_paragraph_break:
            self.original_word = ""
            self.formatted_word = ""
        else:
            self.original_word = word
            self.formatted_word = remove_punctuation(word.lower())
        self.duplicates = []
        self.matched_word = None  # TODO: change to compare multiple songs.
        self.parent = None

    def __repr__(self):
        if self.is_line_break:
            return "<BREAK>"
        if self.is_paragraph_break:
            return "<PARAGRAPH>"
        return (f"{self.original_word} ({self.formatted_word})" \
                f" [{len(self.duplicates)}]")

    def __eq__(self, other):
        return self.formatted_word == other.formatted_word

    def __lt__(self, other):
        return self.formatted_word < other.formatted_word

    def add_duplicate(self, other_word):
        """ Marks the given word as a duplicate of this one. 

            Parameters:
                other_word (Word): the word to be marked as a duplicate.
        """
        self.duplicates.append(other_word)
        other_word.parent = self

    def mark_match(self, matched_word):
        """ Marks that this word has a match! 
        
            Parameters:
                matched_word (Word): the word that matches this one.
        """
        self.matched = matched_word
        for dup in self.duplicates:
            dup.matched = matched_word
