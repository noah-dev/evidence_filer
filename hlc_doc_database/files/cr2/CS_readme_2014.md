# PITCH Exercise

### Summary:

I've been awake for the last 8 hours to get this completed. Unfortunately I am starting to tap out, so the documentation will be sparse; my next couple weeks are going to be bus. While I'd love to rebuild and improve, out of respect, I wanted to complete this exercise before anything else could get in the way.
In Summary:

* Functional: Yes (returns count of message types)
* Unit-tested: Only back-end 
* Documentation: This readme file and demo gif

The front-end is a AngularJS SPA that communicates with a Django backend. The Django projects serve the AngularJS app, and provides a RESTFUL API at /dashboard/file_upload endpoint. That endpoint will accept a POST request containing a file, and will return JSON. The JSON contains a count of all messages by message type, as well as the message formatted according to specs. 

### In Depth: What went right, what went wrong?

Originally, the project only requested a simple count of all the messages by their types. At the start, I thought I could do way better, and build a cool SPA with a nice spreadsheet. Well 7 weeks later, and here we are. Let's start with the positives:

1) The application accepts a file via a POST request and parses it. In addition to returning a count, it returns a JSON object of all the messages, parsed into fields and their appropriate types. 
2) I created a message class which is responsible for parsing the PITCH strings and turn them into their appropriate fields and data types (e.g. Price goes from a string to a float). This reduces the complexity of the views.py file and makes for nice code. 
3) The back-end has unit tests. The message class, which sits within the message package, has a full set of unit tests located under the test folder. The unit tests cover all 12 different message types. IN addition, a test was implemented for the views.py to check HTTP POST behavior. 
4) The front-end is a Single Page Application and displays the message counts. 

On to the negatives: Put simply, the front-end is a mess, bordering on spaghetti code. In retrospect, this effort suffered terrible project management. 
1) The decision to use new technology and new techniques. Originally I sought to use ExtJS, but that resulted in the loss of several weeks. I switched to AngularJS, which was better, but this was my first attempt at building a Single Page Application. The front-end's code reflects that. 
2) Scope creep gone bad. So this whole idea of a spreadsheet was my own doing; an idea to go above and do more. It was a terrible mistake. To much effort was spent on a feature that was not requested, and for a front-end that is, while maybe functional, is otherwise messy and not unit tested. 
3) Schedule mismanagement. I should have failed forward faster and implemented an initial version earlier. This would have revealed  the limitations of my approach, and granted me time to refactor and/or reduce the scope. 
4) The fabled spreadsheet feature has huge performance issues. If the pitch_example_data file is loaded, trying to see the spreadsheet for the Add Orders will freeze the browser for some period of time. My technique is too primitive; I need some sort of pagination or to filter/load data as the user scrolls.

### Front-end warning:

When building the spreadsheet, the table headers are created using the Object.keys() method. According to the internet, this approach does not guarantee the order of the dict keys will come out in the same order as the data below it. Anecdotal evidence has not yet revealed this issue, but that is far from reliable. 

It should also be noted that the approch used to populate the table does not garauntee the order of dict keys either. 