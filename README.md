AI Course Prerequisite Validator
Build Status License Docs
A market‑relevant SaaS that converts college course catalogs into a graph model, validates prerequisite logic, and delivers actionable insights to registrars, curriculum committees, advisors, and students. The validator finds structural issues such as circular prerequisites, hidden requirements, bottlenecks, and overly long prerequisite chains, and exposes them through reports, exports, and an interactive dashboard.

Table of Contents
- Project Overview
- Features and Specifications
- Core Capabilities
- Data Model Summary
- API Examples
- Architecture and Technology Stack
- High Level Architecture
- Recommended Technologies
- Roadmap and Milestones
- MVP Plan 8–12 Weeks
- Post MVP Enhancements
- Go to Market Strategy
- Privacy Compliance and Operational Notes
- Getting Started and Contribution
- License

Project Overview
Purpose
Turn static course catalogs into an auditable directed graph and apply graph algorithms to validate curriculum structure, surface errors, and recommend remediation. The product reduces catalog errors, improves student planning, and helps institutions allocate resources more effectively.
Primary users
- Registrars and curriculum committees
- Academic advisors and institutional researchers
- Students (via optional planning assistant)
- Deans and department chairs
Value proposition
- Detect impossible or inconsistent prerequisite rules before they affect students
- Reveal hidden prerequisites that inflate credit requirements
- Identify bottleneck courses and long prerequisite chains that delay graduation

Features and Specifications
Core Capabilities
- Catalog Ingestion
- HTML scraping, PDF extraction, and catalog API connectors
- Configurable parsers per vendor and fallback NLP for free‑form prerequisite text
- Graph Construction
- Build directed graph G = (V, E) where nodes are courses and edges are prerequisite relationships
- Represent AND/OR logic and annotate co‑requisites without forcing cycles
- Validation Engine
- Cycle Detection using DFS or Kahn’s algorithm with cycle path reporting
- Hidden Prerequisite Detection via transitive closure against program requirements
- Longest Path Analysis to measure curriculum depth using topological ordering and DP
- Bottleneck Detection via out‑degree and betweenness centrality metrics
- Redundancy Heuristics to flag overlapping prerequisite coverage
- Reporting and Exports
- Issue lists with severity, affected courses, and remediation suggestions
- Exports: CSV, GraphML, JSON
- Interactive Dashboard
- Visual graph explorer with color‑coded issues and course drilldown
- Program simulator to preview the impact of changes
- APIs and Integrations
- REST API for ingestion, analysis jobs, and issue retrieval
- Optional connectors for SIS and degree audit systems
Data Model Summary
- Course: course_id, title, level, description, credits, terms_offered
- Program: program_id, name, required_courses[], electives[]
- PrereqExpression: raw_text, expression_tree (AND/OR nodes), resolved_course_ids[]
- GraphEdge: from_course, to_course, edge_type (prereq/coreq/recommended)
API Examples
POST /ingest/catalog
Content-Type: application/json

{
  "source_url": "https://catalog.university.edu/courses",
  "format": "html",
  "program_id": "CS-BS"
}


GET /programs/{program_id}/issues
Response 200 OK
[
  {
    "issue_type": "cycle",
    "severity": "high",
    "courses": ["BIO310", "CHEM250", "BIO310"],
    "message": "Cycle detected: BIO310 -> CHEM250 -> BIO310"
  }
]


GET /courses/{course_id}/graph
Response 200 OK
{
  "prereqs": ["MATH101", "PHYS110"],
  "dependents": ["CS201", "ENGR210"]
}



Architecture and Technology Stack
High Level Architecture
- Ingestion Layer: scrapers, PDF extractor, API connectors, parsing pipeline
- Processing Layer: parser/NLP → normalizer → graph builder
- Analysis Layer: validation engine running graph algorithms and heuristics
- Storage Layer: PostgreSQL for metadata, S3 for raw snapshots, optional graph DB for scale
- API Layer: REST service exposing ingestion, job status, and analysis results
- UI Layer: React dashboard with interactive graph visualization
- Worker Queue: asynchronous job processing for heavy analyses and scheduled re‑runs
Recommended Technologies
- Backend: Python with FastAPI for rapid prototyping and production readiness
- Graph Processing: NetworkX for prototype; Neo4j or TigerGraph for production scale if needed
- NLP Parsing: rule‑based regex plus lightweight transformer models for ambiguous text
- Frontend: React with Cytoscape.js or D3 for interactive graph visualization
- Async Jobs: Celery + Redis or cloud queue (AWS SQS)
- Database: PostgreSQL; object store S3 for snapshots
- Auth: SAML/OAuth for institutional SSO
- Deployment: Docker + Kubernetes or managed cloud services
Design Principles
- Idempotent ingestion with raw snapshot retention
- Explainability with human‑readable rationale for each flagged issue
- Extensibility via plugin parsers and a rules engine
- Privacy by design for any optional student data

Roadmap and Milestones
MVP Plan 8–12 Weeks
- Week 1–2 Ingestion Prototype
- Parser for one catalog format (HTML or a common vendor) and unit tests
- Week 3–4 Graph Builder and Core Analysis
- Graph model, cycle detection, topological layering, longest path calculation
- Week 5–6 API and Minimal UI
- REST endpoints for ingestion and analysis; simple React dashboard to visualize graph and issues
- Week 7–8 Pilot and Export Features
- CSV/GraphML export, job status endpoints, pilot with one institution or public catalog sample
Post MVP Enhancements 3–9 Months
- Parser coverage for multiple catalog vendors and robust PDF extraction
- Advanced analytics: centrality metrics, redundancy detection, offering frequency simulation
- Rules engine for institution‑specific policies and overrides
- SIS integrations for degree audit and optional student planning assistant
- Enterprise features: SSO, multi‑tenant support, audit logs, SLA guarantees
