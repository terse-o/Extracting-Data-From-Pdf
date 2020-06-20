# Extracting-Data-From-Pdf
Extracting data with AWS Textract
Tool: AWS Textract

Language: Python (v3.7)

Description: Employed AWS cloud service - Textract to engineer text information from pdf documents.

Note: Basic packages applied in this project are json, boto3, time, Document. Parent source code for detecting pages, 
words, keys, values, tables, cells, selection elements along with confidence scores pulled from Pluralsight repository.

OVERVIEW:

-Textract returns information from text detected in blocks.

-Block types: 1. Page 2. Line 3. Word

-Block types are returned in json (key - value pair) format after text analysis

-Key types: 1. Relationships 2. Geometry 3. Bounding Box 4. Confidence 5. BlockType 6. ID
