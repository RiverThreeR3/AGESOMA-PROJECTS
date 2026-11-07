"""API for an extractive, citation-backed knowledge retrieval baseline."""

from pathlib import Path
import unicodedata

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, field_validator

from retrieval import KnowledgeIndex


class QueryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    query: str = Field(min_length=3, max_length=500)

    @field_validator("query")
    @classmethod
    def reject_control_characters(cls, value: str) -> str:
        if any(unicodedata.category(char).startswith("C") for char in value):
            raise ValueError("query must not contain control or format characters")
        return value


class SearchRequest(QueryRequest):
    top_k: int = Field(default=3, ge=1, le=5, strict=True)


class SourceCitation(BaseModel):
    source_id: str
    title: str
    line: int


class SearchHit(SourceCitation):
    excerpt: str
    score: float


class SearchResponse(BaseModel):
    mode: str = "lexical_baseline"
    hits: list[SearchHit]


class AnswerResponse(BaseModel):
    mode: str = "extractive_baseline"
    answer: str
    abstained: bool
    citations: list[SourceCitation]


INDEX = KnowledgeIndex(Path(__file__).resolve().parent / "corpus")

app = FastAPI(
    title="AGESOMA Knowledge API — Deterministic Baseline",
    version="0.1.0",
    description=(
        "Public educational demo using synthetic documents. "
        "It does NOT call an LLM, implement vector RAG, or provide authentication."
    ),
)


@app.get("/healthz")
def healthz() -> dict[str, str | int]:
    return {
        "status": "ok",
        "mode": "extractive_baseline",
        "documents": INDEX.document_count,
    }


@app.post("/v1/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    hits = INDEX.search(request.query, top_k=request.top_k)
    return SearchResponse(hits=[SearchHit(**vars(hit)) for hit in hits])


@app.post("/v1/answer", response_model=AnswerResponse)
def answer(request: QueryRequest) -> AnswerResponse:
    hits = INDEX.search(request.query, top_k=1)
    if not hits:
        return AnswerResponse(
            answer="I could not find a supported answer in the indexed documents.",
            abstained=True,
            citations=[],
        )
    best = hits[0]
    return AnswerResponse(
        answer=best.excerpt,
        abstained=False,
        citations=[
            SourceCitation(
                source_id=best.source_id,
                title=best.title,
                line=best.line,
            )
        ],
    )
