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
- A PC capable of running Python
- Python websockets 8.1 (may work with other versions).


# Install instructions
1. Install the extension on Tampermonkey
1. (Optional) Generate new certificates: `openssl  req  -x509  -nodes  -newkey rsa:2048  -keyout cert.key  -out cert.crt  -days 365  -subj "/C=US/ST=/L=/O=/OU=/CN=mywebsocket"`

# Usage instructions
1. On the PC run python script to start server
1. On the PC make sure that you can access https://localhost:8000 (accept SSL warnings).
1. On your smartphone open this URL replacing the IP for your PC (eg: https://192.168.1.33:8000/websocket-speed-video-controller). Accept SSL warnings.
1. On your PC go to Youtube, play a video and start swiping in your phone. The playback speed of the video should change accordingly.

# Demo

https://www.youtube.com/watch?v=L5VJ6WUKl_0
