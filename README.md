# WebSocket-Speed-Video-Controller
Control speed of videos playing in your browser using your phone.

This project has 3 parts:
- A user extension that reads websocket events using HTML5 API, and then applies speed changes to current video.
- An HTML controller interface for your smartphone.
- A Websocket server in Python to communicate the previous parts.

# Requirements
- A browser (currently tested on Chrome)
- A user script engine extension installed in the browser (currently tested with Tampermoneky)
- A smartphone
- A PC capable of running Python and serve Web Pages


# Install instructions
1. Install the extension on Tampermonkey
1. (Optional) Generate new certificates
1. Configure a Web server on your PC to serve the HTML pages (using HTTPS).
1. Edit "index.html" (the line that contains the function "WebSocket") so it matches the IP of your PC.
1. Run the python part

# Usage instructions
1. In the PC make sure that you can access https://localhost (accept SSL warnings).
1. In your smartphone accept SSL warnings of the WebSocket (eg: https://192.168.1.33:8000), then close the tab.
1. In your smartphone open the HTML page (eg: https://192.168.1.33) and accept SSL warnings.
1. In your PC go to Youtube, play a video and start swiping in your phone. The playback speed of the video should change accordingly.

# Demo

TODO
