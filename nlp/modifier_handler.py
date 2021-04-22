from collections import defaultdict


class ModifierHandler:
    def __init__(self):
        self._modifiers = defaultdict(list)

    def add_modifier(sentence, word, modifier):
        self._modifiers[(sentence, word)].add(modifier)

    @property
    def modifiers(self):
        return self._modifiers
