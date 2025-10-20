# Test Results for C:\git\github\Logikbug\prompd-base\production\@prompd.io\invoice-processor@1.0.0\prompts\invoice-extractor.prmd

## Parameters Used:
- invoice_text: Invoice #123 Amount: $500
- invoice_image: none
- company_info: TestCorp

## Command:
```
C:\Users\sbake\AppData\Local\Programs\Python\Python311\python.exe -m prompd.cli run C:\git\github\Logikbug\prompd-base\production\@prompd.io\invoice-processor@1.0.0\prompts\invoice-extractor.prmd --provider anthropic --model claude-3-haiku-20240307 -p invoice_text=Invoice #123 Amount: $500 -p invoice_image=none -p company_info=TestCorp
```

## Status: ✅ SUCCESS

## LLM Response:
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Thank you for the detailed requirements for the Invoice Data Extraction System. I understand the importance of       |
| accurate data extraction, especially when it comes to financial records. Let's go through the process step-by-step:  |
|                                                                                                                      |
| ## Step 1: Document Analysis                                                                                         |
|                                                                                                                      |
| 1. **Identify document type and layout**: Analyze the provided invoice image/PDF to determine if it is a valid       |
| invoice document and assess the overall layout and structure.                                                        |
|                                                                                                                      |
| 2. **Assess image quality and readability**: Evaluate the quality of the image or PDF, ensuring that the text and    |
| data are clearly legible and can be accurately extracted.                                                            |
|                                                                                                                      |
| 3. **Determine if document is a valid invoice**: Verify that the document is indeed an invoice and not some other    |
| type of financial document.                                                                                          |
|                                                                                                                      |
| 4. **Check for multiple pages or attachments**: Identify if the invoice spans multiple pages or has any additional   |
| attachments that need to be processed.                                                                               |
|                                                                                                                      |
| ## Step 2: Data Extraction                                                                                           |
|                                                                                                                      |
| Using the provided JSON format, extract the following data from the invoice:                                         |
|                                                                                                                      |
| ```json                                                                                                              |
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
| ## Step 3: Validation Checks                                                                                         |
|                                                                                                                      |
| 1. **Mathematical Accuracy**:                                                                                        |
|    - Verify line item calculations (qty × price = total)                                                             |
|    - Confirm subtotal = sum of line items                                                                            |
|    - Validate tax calculations                                                                                       |
|    - Ensure subtotal + tax = total amount                                                                            |
|                                                                                                                      |
| 2. **Data Completeness**:                                                                                            |
|    - Ensure all required fields are present                                                                          |
|    - Validate date formats                                                                                           |
|    - Verify proper currency formatting                                                                               |
|    - Confirm complete vendor information                                                                             |
|                                                                                                                      |
| 3. **Business Rules**:                                                                                               |
|    - Ensure invoice date is not in the future                                                                        |
|    - Verify due date is after invoice date                                                                           |
|    - Confirm all amounts are positive numbers                                                                        |
|    - Validate tax rates are within reasonable ranges                                                                 |
|                                                                                                                      |
| ## Step 4: Confidence Assessment                                                                                     |
|                                                                                                                      |
| Assess the overall confidence level of the extracted data based on the following criteria:                           |
|                                                                                                                      |
| - Image/document clarity (25%)                                                                                       |
| - Field completeness (25%)                                                                                           |
| - Mathematical consistency (25%)                                                                                     |
| - Standard format recognition (25%)                                                                                  |
|                                                                                                                      |
| If the confidence level is 0.85 or higher, the invoice can be auto-approved. Otherwise, it will require manual       |
| review.                                                                                                              |
|                                                                                                                      |
| ## Vendor Matching                                                                                                   |
|                                                                                                                      |
| If a vendor database is provided, cross-reference the extracted vendor information against the known vendors in the  |
| database. Match on:                                                                                                  |
|                                                                                                                      |
| 1. Exact company name                                                                                                |
| 2. Tax ID number                                                                                                     |
| 3. Address similarity                                                                                                |
| 4. Phone number                                                                                                      |
|                                                                                                                      |
| Flag any discrepancies for manual review.                                                                            |
|                                                                                                                      |
| ## Error Handling                                                                                                    |
|                                                                                                                      |
| If the extraction confidence level is below 0.85:                                                                    |
+----------------------------------------------------------------------------------------------------------------------+

