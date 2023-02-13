from typing import Dict

from flair.data import Sentence


def jsonify_flair(sentence: Sentence) -> Dict:
    for span in sentence.get_spans():
        yield {'entity_txt': span.text,
               'tag': span.tag,
               'score': span.score,
               'start_idx': span.start_pos,
               'end_idx': span.end_pos}

