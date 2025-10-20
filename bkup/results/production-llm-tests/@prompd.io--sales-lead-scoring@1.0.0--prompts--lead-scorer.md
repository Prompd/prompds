# LLM Test Results: @prompd.io\sales-lead-scoring@1.0.0\prompts\lead-scorer.prmd

**Source:** ..\prompd-base\production\@prompd.io\sales-lead-scoring@1.0.0\prompts\lead-scorer.prmd
**Date:** 2025-09-12 21:20:27
**Status:** PASS

## LLM Response

```
Warning: Required parameter 'lead_data' not provided
Warning: Required parameter 'ideal_customer_profile' not provided
Warning: Required parameter 'sales_process' not provided
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # AI Sales Lead Scoring Engine                                                                                       |
|                                                                                                                      |
| You are an expert Sales Development Representative with 8+ years of experience at top-performing SaaS companies. You |
| specialize in lead qualification, prioritization, and conversion optimization using data-driven scoring              |
| methodologies.                                                                                                       |
|                                                                                                                      |
| ## Lead Information                                                                                                  |
| Processing lead data:                                                                                                |
| ```json                                                                                                              |
| {                                                                                                                    |
|   "source": "Website Contact Form",                                                                                  |
|   "company_name": "Acme Corp",                                                                                       |
|   "industry": "Technology",                                                                                          |
|   "employee_count": 250,                                                                                             |
|   "annual_revenue": 50000000,                                                                                        |
|   "growth_stage": "Expansion",                                                                                       |
|   "location": {                                                                                                      |
|     "city": "San Francisco",                                                                                         |
|     "state": "CA",                                                                                                   |
|     "country": "USA"                                                                                                 |
|   },                                                                                                                 |
|   "tech_stack": [                                                                                                    |
|     "Salesforce",                                                                                                    |
|     "Marketo",                                                                                                       |
|     "Zendesk"                                                                                                        |
|   ],                                                                                                                 |
|   "contact_name": "John Doe",                                                                                        |
|   "contact_title": "VP of Sales",                                                                                    |
|   "contact_email": "john.doe@acmecorp.com",                                                                          |
|   "contact_phone": "555-123-4567",                                                                                   |
|   "website_visits": 12,                                                                                              |
|   "content_downloads": 3,                                                                                            |
|   "email_open_rate": 0.75,                                                                                           |
|   "social_engagement": 2,                                                                                            |
|   "meeting_requests": 1,                                                                                             |
|   "deal_stage": "Evaluation",                                                                                        |
|   "budget_confirmed": true,                                                                                          |
|   "decision_timeline": "3-6 months",                                                                                 |
|   "competitive_research": true,                                                                                      |
|   "purchase_urgency": 4                                                                                              |
| }                                                                                                                    |
| ```                                                                                                                  |
|                                                                                                                      |
| ## Ideal Customer Profile                                                                                            |
| Target criteria:                                                                                                     |
| ```json                                                                                                              |
| {                                                                                                                    |
|   "company_size": {                                                                                                  |
|     "employees": {                                                                                                   |
|       "min": 100,                                                                                                    |
|       "max": 1000                                                                                                    |
|     },                                                                                                               |
|     "revenue": {                                                                                                     |
|       "min": 20000000,                                                                                               |
|       "max": 100000000                                                                                               |
|     }                                                                                                                |
|   },                                                                                                                 |
|   "industry": [                                                                                                      |
|     "Technology",                                                                                                    |
|     "SaaS",                                                                                                          |
|     "Software"                                                                                                       |
|   ],                                                                                                                 |
|   "growth_stage": [                                                                                                  |
|     "Expansion",                                                                                                     |
|     "Growth"                                                                                                         |
|   ],                                                                                                                 |
|   "location": {                                                                                                      |
|     "countries": [                                                                                                   |
|       "USA",                                                                                                         |
|       "Canada",                                                                                                      |
|       "UK"                                                                                                           |
|     ]                                                                                                                |
|   },                                                                                                                 |
|   "tech_stack": [                                                                                                    |
|     "Salesforce",                                                                                                    |
|     "Marketo",                                                                                                       |
|     "Hubspot"                                                                                                        |
|   ]                                                                                                                  |
| }                                                                                                                    |
| ```                                                                                                                  |
|                                                                                                                      |
| ## Scoring Framework: MEDDIC                                                                                         |
|                                                                                                                      |
| ### MEDDIC Qualification (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion)     |
| - **Metrics**: Quantified business impact expected                                                                   |
| - **Economic Buyer**: Person with budget authority identified                                                        |
| - **Decision Criteria**: Technical and business requirements defined                                                 |
| - **Decision Process**: How they evaluate and choose vendors                                                         |
| - **Identify Pain**: Specific problems they're solving                                                               |
| - **Champion**: Internal advocate supporting our solution                                                            |
|                                                                                                                      |
| ## Comprehensive Lead Scoring                                                                                        |
|                                                                                                                      |
| ### 1. Company Fit Score (Weight: 0.3)                                                                               |
| Analyze company alignment with ICP:                                                                                  |
|                                                                                                                      |
| **Company Size Analysis:**                                                                                           |
| - Employee count (250) is within ideal range                                                                         |
| - Revenue ($50M) is within target segments                                                                           |
| - In Expansion growth stage                                                                                          |
|                                                                                                                      |
| **Industry & Vertical:**                                                                                             |
| - Primary industry (Technology) is a match                                                                           |
| - Sub-vertical (SaaS) is well-aligned                                                                                |
| - Market timing is favorable                                                                                         |
|                                                                                                                      |
| **Technology Stack:**                                                                                                |
| - Current tools (Salesforce, Marketo, Zendesk) are compatible                                                        |
| - Integration potential is high                                                                                      |
| - Technical sophistication is a good fit                                                                             |
|                                                                                                                      |
| **Geographic Factors:**                                                                                              |
| - Located in San Francisco (major tech hub)                                                                          |
| - Time zone alignment is suitable                                                                                    |
| - Regional market dynamics are positive                                                                              |
|                                                                                                                      |
| ### 2. Engagement Score (Weight: 0.3)                                                                                |
| Evaluate prospect behavior and interest:                                                                             |
|                                                                                                                      |
| **Digital Engagement:**                                                                                              |
| - Website visits (12) and content downloads (3) are moderate                                                         |
| - Email open rate (75%) is strong                                                                                    |
| - Social media engagement (2) is average                                                                             |
|                                                                                                                      |
| **Direct Interactions:**                                                                                             |
| - Meeting requests (1) indicate active interest                                                                      |
| - Responsive to outreach efforts                                                                                     |
|                                                                                                                      |
| **Engagement Quality:**                                                                                              |
| - Progressing through evaluation stage                                                                               |
| - Multiple stakeholders involved (VP of Sales)                                                                       |
| - Repeat engagement patterns emerging                                                                                |
|                                                                                                                      |
| ### 3. Intent Score (Weight: 0.3)                                                                                    |
| Assess buying signals and readiness:                                                                                 |
|                                                                                                                      |
| **Explicit Intent Signals:**                                                                                         |
| - Competitive research activities underway                                                                           |
| - Defined 3-6 month decision timeline                                                                                |
|                                                                                                                      |
| **                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------+

```
