import PyPDF2 as p

# Open the PDF file in binary mode
file = open(r"C:\Users\navee\Downloads\Copy-of-Company-Fact-Sheet.pdf", 'rb')

# Create a PdfReader object
pd = p.PdfReader(file)

# Get the first and second pages of the PDF
X = pd.pages[0]
Y = pd.pages[1]
Y = pd.pages[2]
Y = pd.pages[3]
Y = pd.pages[4]

# Extract text from the pages
print(X.extract_text())
print(Y.extract_text())

# Close the file after extracting
file.close()
