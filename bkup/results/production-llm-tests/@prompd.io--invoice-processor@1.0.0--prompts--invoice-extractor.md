# LLM Test Results: @prompd.io\invoice-processor@1.0.0\prompts\invoice-extractor.prmd

**Source:** ..\prompd-base\production\@prompd.io\invoice-processor@1.0.0\prompts\invoice-extractor.prmd
**Date:** 2025-09-12 21:19:43
**Status:** PASS

## LLM Response

```
Warning: Required parameter 'invoice_image' not provided
Warning: Required parameter 'company_info' not provided
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # Invoice Data Extraction System                                                                                     |
|                                                                                                                      |
| As an expert Accounts Payable specialist with 15+ years of experience processing invoices for Fortune 500 companies, |
| I understand the importance of extracting accurate, structured data from invoice documents with zero tolerance for   |
| errors that could impact financial records.                                                                          |
|                                                                                                                      |
| ## Extraction Requirements                                                                                           |
|                                                                                                                      |
| ### Primary Invoice Data                                                                                             |
| I will extract the following fields with **exact accuracy**:                                                         |
|                                                                                                                      |
| 1. **Vendor Information**                                                                                            |
|    - Company name (exact legal name)                                                                                 |
|    - Vendor address (complete with postal code)                                                                      |
|    - Tax ID/VAT number                                                                                               |
|    - Contact information (phone, email if present)                                                                   |
|                                                                                                                      |
| 2. **Invoice Details**                                                                                               |
|    - Invoice number (exact alphanumeric)                                                                             |
|    - Invoice date (validate format: YYYY-MM-DD)                                                                      |
|    - Due date (if present)                                                                                           |
|    - Purchase order number (if referenced)                                                                           |
|                                                                                                                      |
| 3. **Financial Data**                                                                                                |
|    - Line items (description, quantity, unit price, total)                                                           |
|    - Subtotal (pre-tax amount)                                                                                       |
|    - Tax amount (itemized by rate if multiple)                                                                       |
|    - Total amount due                                                                                                |
|    - Currency (validate against USD)                                                                                 |
|                                                                                                                      |
| 4. **Payment Terms**                                                                                                 |
|    - Payment terms (Net 30, 2/10 Net 30, etc.)                                                                       |
|    - Discount terms if applicable                                                                                    |
|    - Late payment penalties                                                                                          |
|                                                                                                                      |
| ## Processing Workflow                                                                                               |
|                                                                                                                      |
| ### Step 1: Document Analysis                                                                                        |
| ```                                                                                                                  |
| Analyze the provided invoice image/PDF:                                                                              |
| {{invoice_image}}                                                                                                    |
|                                                                                                                      |
| 1. Identify document type and layout                                                                                 |
| 2. Assess image quality and readability                                                                              |
| 3. Determine if document is a valid invoice                                                                          |
| 4. Check for multiple pages or attachments                                                                           |
| ```                                                                                                                  |
|                                                                                                                      |
| I will carefully analyze the provided invoice image or PDF to determine the document type and layout, assess the     |
| image quality and readability, confirm that the document is a valid invoice, and check for multiple pages or         |
| attachments.                                                                                                         |
|                                                                                                                      |
| ### Step 2: Data Extraction                                                                                          |
| ```                                                                                                                  |
| Extract structured data using this JSON format:                                                                      |
|                                                                                                                      |
| {                                                                                                                    |
|   "document_info": {                                                                                                 |
|     "type": "invoice",                                                                                               |
|     "confidence_score": 0.0-1.0,                                                                                     |
|     "processing_notes": "Any issues or observations"                                                                 |
|   },                                                                                                                 |
|   "vendor": {                                                                                                        |
|     "name": "extracted_name",                                                                                        |
|     "address": {                                                                                                     |
|       "street": "street_address",                                                                                    |
|       "city": "city",                                                                                                |
|       "state": "state_or_province",                                                                                  |
|       "postal_code": "postal_code",                                                                                  |
|       "country": "country"                                                                                           |
|     },                                                                                                               |
|     "tax_id": "tax_identification_number",                                                                           |
|     "contact": {                                                                                                     |
|       "phone": "phone_number",                                                                                       |
|       "email": "email_address"                                                                                       |
|     }                                                                                                                |
|   },                                                                                                                 |
|   "invoice_details": {                                                                                               |
|     "invoice_number": "invoice_number",                                                                              |
|     "invoice_date": "YYYY-MM-DD",                                                                                    |
|     "due_date": "YYYY-MM-DD",                                                                                        |
|     "po_number": "purchase_order_number",                                                                            |
|     "currency": "USD"                                                                                                |
|   },                                                                                                                 |
|   "line_items": [                                                                                                    |
|     {                                                                                                                |
|       "description": "item_description",                                                                             |
|       "quantity": numeric_quantity,                                                                                  |
|       "unit_price": numeric_price,                                                                                   |
|       "line_total": numeric_total,                                                                                   |
|       "tax_rate": "tax_percentage_if_applicable"                                                                     |
|     }                                                                                                                |
|   ],                                                                                                                 |
|   "financial_summary": {                                                                                             |
|     "subtotal": numeric_subtotal,                                                                                    |
|     "tax_details": [                                                                                                 |
|       {                                                                                                              |
|         "tax_type": "sales_tax",                                                                                     |
|         "rate": "percentage",                                                                                        |
|         "amount": numeric_amount                                                                                     |
|       }                                                                                                              |
|     ],                                                                                                               |
|     "total_amount": numeric_total,                                                                                   |
|     "payment_terms": "payment_terms_text"                                                                            |
|   },                                                                                                                 |
|   "validation": {                                                                                                    |
|     "math_check": "pass/fail",                                                                                       |
|     "required_fields": "complete/incomplete",                                                                        |
|     "confidence_level": 0.0-1.0,                                                                                     |
|     "auto_approval_eligible": true/false                                                                             |
|   }                                                                                                                  |
| }                                                                                                                    |
| ```                                                                                                                  |
|                                                                                                                      |
| I will extract the structured data from the invoice using the provided JSON format, ensuring that all required       |
| fields are populated accurately.                                                                                     |
|                                                                                                                      |
| ### Step 3: Validation Checks                                                                                        |
| I will perform the following critical validations:                                                                   |
|                                                                                                                      |
| 1. **Mathematical Accuracy**                                                                                         |
|    - Verify line item calculations (qty × price = total)                                                             |
|    - Confirm subtotal = sum of line items                                                                            |
|    - Validate tax calculations                                                                                       |
|    - Ensure subtotal + tax = total amount                                                                            |
|                                                                                                                      |
| 2. **Data Completeness**                                                                                             |
|    - All required fields present                                                                                     |
|    -                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------+

```
