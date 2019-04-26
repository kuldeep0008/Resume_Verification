# Resume_Verification
An Internal project, to filter out valid vs invalid resumes

It takes Two input parameters 1. Path of the folder where resumes(docx files) are available and string ( ie. Sql, Python, C# etc) on the basis of which we are filtering resumes are valid or invalid


# How it is working
It Takes input of the folder and then filters the Docx files and convert those into a list of strings
It futher apllies Regular expression to filter out unncessory special charechters.
It then create a corpus of the data

Then it searches the word(ie. sql, java, python etc) in the corpus, and then creates another column containg the count of the the word in the resume.

Then it creates another column which on the basis of count of the word tells that resume is vaid or invalid ( I have given the count 8)

If the word count is greater then or equal to 8, then it is 'Valid" else "Invalid"

Thank You :)
