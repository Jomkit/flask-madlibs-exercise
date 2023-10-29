"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, words, text):
        """Create story with words and template text."""
        self.name = name
        self.prompts = words
        self.template = text
    
    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    "Basic Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    "Outing",
    ["place", "noun", "2nd_noun", "past_tense_verb", "verb", "adverb", "proper_noun"],
    """Today I went to the {place} to get some {noun}. 
    On my way home, my {2nd_noun} {past_tense_verb} so I had to 
    {verb} {adverb} for {proper_noun}"""
)
story3 = Story(
    "Limerick",
    ["person","place", "past_tense_verb", "verb", "noun"],
    """There once was a {person} in {place}, who {past_tense_verb} they could {verb} a {noun}"""
)

stories = {story1, story2, story3}