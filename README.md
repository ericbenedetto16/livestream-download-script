Wrote this for a baseball game livestream video which was being sent in blobs and played. I found the URL for the video in the Chrome Inspector under the Network tab. The URL contained a different number before the .ts extension. Using this information I tried to visit the URL and it downloaded the video clip.

In conclusion, I was able to use the pattern in the URL to create a for loop which changed the prefix for each video clip I wanted. For the best use, I:

1. Scrubbed through the beginning and the last few seconds of the LiveStream playback in order to find the first and last video clip filenames.
2. Changed my Google Chrome setting for the Download path to both:
  - Make my download path to a src folder.
  - Turn off the ask each time for a directory to save to.
3. After downloading all of the clips searched online for a program to combine the .ts files. This could be done manually but is resource consuming and I found easier to do online.

This could be used for most LiveStream playbacks that are being sent in blobs or small segments if you can find the URL in the Network tab and also a filename pattern.

Prerequisites:
- Python
- Selenium
- ChromeDriver
- Google Chrome

Notes:
  This same process could probably be done with the 'requests' package on Python to just send the request and download the file rather than selenium having windows pop up, however I have limited experience with it and if you have a second display or are running it overnight for a large livestram, this really should not be a big concern.
