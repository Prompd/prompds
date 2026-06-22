# @prompd/invoice-extractor

Extracts structured invoice data from raw text or OCR output. Parses vendor information, line items, totals, tax, purchase order numbers, and payment terms — returning a single, schema-compliant JSON object suitable for direct ingestion by accounts payable systems.

Designed for high-volume invoice processing pipelines where reliability matters. The extractor returns null for any field it cannot confidently trace to source text, never fabricating values. Monetary normalization, line item extraction, and currency detection are configurable per invocation.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `invoice_text` | string | yes | — | Raw invoice text or OCR output to extract data from |
| `currency_normalize` | boolean | no | `true` | Strip currency symbols and return monetary values as plain floats |
| `extract_line_items` | boolean | no | `true` | Include detailed line item breakdown in output |

## Example

Input:
```json
{
  "invoice_text": "INVOICE\nAcme Supplies Inc.\n123 Main St, Springfield, IL 62701\nTax ID: 12-3456789\n\nInvoice #: INV-2024-08821\nDate: November 15, 2024\nDue: December 15, 2024\nPO Number: PO-98234\nPayment Terms: Net 30\n\nWidget Type A    100 x $4.50    $450.00\nShipping                         $25.00\n\nSubtotal: $475.00\nTax (8%): $38.00\nTotal Due: $513.00",
  "currency_normalize": true,
  "extract_line_items": true
}
```

Output:
```json
{
  "vendor": {
    "name": "Acme Supplies Inc.",
    "address": "123 Main St, Springfield, IL 62701",
    "tax_id": "12-3456789"
  },
  "invoice_number": "INV-2024-08821",
  "invoice_date": "2024-11-15",
  "due_date": "2024-12-15",
  "po_number": "PO-98234",
  "payment_terms": "Net 30",
  "line_items": [
    {"description": "Widget Type A", "quantity": 100, "unit_price": 4.50, "total": 450.00},
    {"description": "Shipping", "quantity": 1, "unit_price": 25.00, "total": 25.00}
  ],
  "subtotal": 475.00,
  "tax_rate": 0.08,
  "tax_amount": 38.00,
  "total": 513.00,
  "currency": "USD"
}
```

## Install

```
prompd install @prompd/invoice-extractor
```
