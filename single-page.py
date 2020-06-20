import boto3
from trp import Document

#Document
s3BucketName = "pl-textract"
documentName = "e6c3942c-b902-4d22-a3b9-1f13e94b15b0.jpg"

#Amazon Textract client
textract = boto3.client('textract')

def lines(doc):
    for page in doc.pages:
        print("PAGE\n====================")
        for line in page.lines:
            print("Line: {}--{}".format(line.text, line.confidence))
            for word in line.words:
                print("Word: {}--{}".format(word.text, word.confidence))

def forms(doc):
    for page in doc.pages:
        print("Fields:")
        for field in page.form.fields:
            print("Key: {}, Value: {}".format(field.key, field.value))

def tables(doc):
    for page in doc.pages:
        print("Tables:")
        for table in page.tables:
            for r, row in enumerate(table.rows):
                for c, cell in enumerate(row.cells):
                    print("Table[{}][{}] = {}".format(r, c, cell.text))

def analyze():
    response = textract.analyze_document(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
            }
        },
        FeatureTypes=["FORMS", "TABLES"])
    
    doc = Document(response)
    #lines(doc)
    #forms(doc)
    tables(doc)

def detect():
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
        }
    })

    #print detected text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print(item["Text"])

#detect()

analyze()