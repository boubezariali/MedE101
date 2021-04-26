from collections import defaultdict

from nlp.stanza_utils import get_stanza_model


class ModifierHandler:
    def __init__(self):
        self._modifiers = defaultdict(list)

    def add_modifier(self, sent_idx, word_idx, modifier):
        self._modifiers[(sent_idx, word_idx)].append(modifier)

    def get_modifier(self, sent_idx, word_idx):
        if (sent_idx, word_idx) in self._modifiers:
            return self._modifiers[sent_idx_word_idx]
        return []

    @property
    def modifiers(self):
        return self._modifiers
