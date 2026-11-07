"""Deterministic, extractive retrieval over a fixed set of public synthetic documents."""

from collections import Counter
from dataclasses import dataclass
from math import log
from pathlib import Path
import re
import unicodedata


STOP_WORDS = frozenset({
    "a", "about", "after", "an", "and", "are", "at", "be", "can", "could",
    "do", "does", "for", "from", "how", "i", "in", "is", "it", "long", "me", "my",
    "of", "on", "or", "our", "please", "should", "the", "their", "this",
    "to", "us", "was", "what", "when", "where", "which", "who", "why",
    "will", "window", "with", "would", "you", "your",
})


def tokenize(text: str) -> frozenset[str]:
    """Normalize accents and use whole-word terms, excluding common stop words."""
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
    words = re.findall(r"[a-z0-9]+", plain.decode("ascii").lower())
    return frozenset(word for word in words if len(word) > 1 and word not in STOP_WORDS)


@dataclass(frozen=True)
class Passage:
    source_id: str
    title: str
    line: int
    text: str
    terms: frozenset[str]


@dataclass(frozen=True)
class Hit:
    source_id: str
    title: str
    line: int
    excerpt: str
    score: float


class KnowledgeIndex:
    """An auditable lexical baseline. No model calls or network traffic."""

    def __init__(self, corpus_dir: Path) -> None:
        documents = sorted(corpus_dir.glob("*.md"))
        if not documents:
            raise ValueError("The approved corpus is empty")
        passages: list[Passage] = []
        for document in documents:
            if document.stat().st_size > 16_384:
                raise ValueError("A corpus document exceeds the size limit")
            lines = document.read_text(encoding="utf-8").splitlines()
            title = next(
                (line[2:].strip() for line in lines if line.startswith("# ")),
                document.stem,
            )
            for number, line in enumerate(lines, start=1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if len(line) > 800:
                    raise ValueError("A corpus passage exceeds the size limit")
                terms = tokenize(line)
                if terms:
                    passages.append(
                        Passage(document.name, title, number, line, terms)
                    )
        if not passages:
            raise ValueError("The approved corpus contains no searchable passages")
        self.document_count = len(documents)
        self.passages = tuple(passages)
        self.document_frequency = Counter(
            word for passage in passages for word in passage.terms
        )

    def search(self, query: str, *, top_k: int = 3) -> list[Hit]:
        if not 1 <= top_k <= 5:
            raise ValueError("top_k must be in the range 1 to 5")
        terms = tokenize(query)
        if not terms:
            return []
        # Require meaningful coverage instead of accepting a single topical word.
        # Lexical overlap alone still does NOT prove semantic answerability.
        required_overlap = 2 if len(terms) > 1 else 1
        query_numbers = {term for term in terms if term.isdecimal()}
        scored: list[Hit] = []
        total = len(self.passages)
        for passage in self.passages:
            matching = terms & passage.terms
            if len(matching) < required_overlap:
                continue
            # At least 60% of distinctive query terms must occur in the same
            # supporting passage, preventing a few shared words from triggering
            # a misleading near-domain answer. Integer comparison avoids floats.
            if len(matching) * 5 < len(terms) * 3:
                continue
            # Never cite a passage containing another number as evidence for
            # a numeric assertion in the question (e.g., 90 vs. 30 days).
            if not query_numbers.issubset(passage.terms):
                continue
            score = sum(
                1.0 + log((total + 1) / (1 + self.document_frequency[term]))
                for term in matching
            )
            scored.append(
                Hit(
                    source_id=passage.source_id,
                    title=passage.title,
                    line=passage.line,
                    excerpt=passage.text,
                    score=round(score, 4),
                )
            )
        return sorted(
            scored, key=lambda hit: (-hit.score, hit.source_id, hit.line)
        )[:top_k]
