from dataclasses import dataclass

@dataclass
class Document:
    document_id: int
    title: str
    content: str

@dataclass
class ProcessResult:
    document_id: int
    normalized_content: str
    character_count: int