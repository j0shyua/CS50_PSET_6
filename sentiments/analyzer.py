import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()
        
        # Load the list of positive words into memory
        with open("positive-words.txt") as positive:
            for line in positive:
                if line.startswith(';') != True:
                    self.positives.add(line.strip(" \n"))
            positive.close()

        # Load the list of negative words into memory
        with open("negative-words.txt") as negative:
            for line in negative:
                if line.startswith(";") != True:
                    self.negatives.add(line.strip(" \n"))
            negative.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        # For every token, score > 1 = smile, < 1 is frown, and else neutral.
        for token in tokens:
            token.lower()
            
            if token in self.positives:
                score += 1
            if token in self.negatives:
                score -= 1

        return score