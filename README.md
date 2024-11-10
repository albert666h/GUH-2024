# Memora

Memora is a Web Application built using Python, JS, HTML, and CSS. 
The purpose of the app is to read chat logs from a WhatsApp Chat Backup zip file (containing the media)
and convert it into a nice memory timeline that will include top 5 core memories. If any memories or events 
have a relevant photo attached, it will be displayed too. Additionally, the images are analyzed for their vibe
or mood, and based on this the background color changes when focused on the particular event.
On top of that, there is a second webpage, where users can take a quiz on their interesting memories. The test includes
2 modified memories and one unchanged and the user's task is to identify which is the unmodified one.

# How to run

* The program uses Python libraries Flask and OpenAI.

* Make sure you have a file named 'key' in the same directory as the python files, containing the openapi key.

* After installing the requirements, in terminal run the app.py file to start the server.

* In your browser, go to localhost:5000 and the webpage will appear.

# What not to do.

* If you do not intend on breaking the program:
  * do not upload non zip or empty files
  * do not call the Get or Post requests on your own and only run them through browser
  * do not close the selection.html page (the page where you choose timeline or quiz) as
    it is required for keeping all of the backup files on the server. After closing this window, all
    of the files will be removed forever
  * Sometimes there are some prompt issues and some errors might occur, just close the window and reopen it from the selection page.
