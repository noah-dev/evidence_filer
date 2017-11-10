# UMKCFS2017_Hackathon

### Problem statement:

UMKC will need a tool that will manage the 1,500+ documents collected and used to support the university’s Higher Learning Commission Accreditation Reaffirmation process. Help us keep UMKC accredited!

#### Application Specifications:

There are two main interactions for the tool. Document Submission:

* A form that will allow UMKC committee members to submit documents. It should be able to handle different types of documents, such as text, doc, pdf, image, and spreadsheet. UMKC committee members should also be able to provide descriptive information that includes department, document name, document year, HLC category, justification, and submitter.

Upon submission, the tool will do the following:

* Programmatically rename the file to department_documentname_year.
* Save the file to the appropriate HLC category.
* Generate a unique doc # and log it and the form metadata into an accessible table.
* Organize the documents based on different categories such as submitter, academic unit or department, HLC category, type of document, etc.


### Document Retrieval:

Provide an interface for UMKC committee members to search for or browse submitted documents.

* Allow members to browse all documents by the department, HLC category, etc.
* Provide a search box to allow members to search for documents by keywords in the department or document name. Ideally also provide full-text document searching.
* Members would be able to access and open the file within the browse/search results.

### Document taxonomies:

* The tool will need to control values for department and HLC category and related assumed practices. Admins will need to be able to maintain value lists for those fields. Bonus points for analytics functionality (# documents by department, category, and year).
