```mermaid
flowchart TD
    A[File Upload API] --> B{File Type}
    
    B -->|.pdf| C["PyPDFLoader<br/>(pypdf binary parser)"]
    B -->|.docx| D["Docx2txtLoader<br/>(XML DOM + zipfile)"] 
    B -->|.txt| E["TextLoader<br/>(chardet encoding)"]
    
    C --> F[LangChain Document]
    D --> F
    E --> F
    
    F --> G["Regex Cleaning Pipeline<br/>(URLs, emails, metadata)"]
    G --> H["Text Chunking<br/>(3000 chars, overlap=0)"]
    H --> I[SimCSE Ready Text]
    
    %% Technical Details
    C -.-> C1["PDF: Binary stream to page objects to text reconstruction"]
    D -.-> D1["DOCX: ZIP to XML parsing to w:p/w:r/w:t elements"]
    E -.-> E1["TXT: Encoding detection to UTF-8 normalization"]
```

**Key Technical Implementation:**

**Format-Specific Parsing:**
- **PDF**: pypdf library for binary stream parsing and page object extraction
- **DOCX**: zipfile + xml.etree.ElementTree for XML DOM navigation (w:p to w:r to w:t hierarchy)  
- **TXT**: chardet for encoding detection with UTF-8 normalization

**Common Processing Pipeline:**
- LangChain Document object standardization
- Regex cleaning: URLs (http patterns), emails (word@domain patterns), DOI patterns
- RecursiveCharacterTextSplitter: 3000 character chunks, no overlap
- Output optimization for SimCSE token processing
```