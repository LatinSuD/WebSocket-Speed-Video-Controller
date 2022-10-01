// ==UserScript==
// @name         WebSocket video speed controller
// @namespace    http://tampermonkey.net/
// @version      0.2.1
// @description  try to take over the world!
// @author       You
// @match        file://*/*
// @match        http://*/*
// @match        https://*/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    var wss = 'wss://localhost:8000';

    // Threshold around speed 1x
    var threshold = 0.1;

    // Whether to invert
    var invert=0;


    var desiredSpeed = null;
    var lastSetSpeed = null;

    var myTimer = null;

    function timerHandler() {
        if (desiredSpeed && ( desiredSpeed != lastSetSpeed )) {
            document.querySelectorAll('video').forEach(function(aVideo) {
                if (!aVideo.paused && !aVideo.ended && aVideo.readyState > 2) {
                    lastSetSpeed=desiredSpeed;
                    aVideo.playbackRate=desiredSpeed;
                    console.log("WebSocket Set speed to " + desiredSpeed);
                }
            })
        }
    }


    // WebSocket received data
    function dataHandler(valor2) {        
        var valor3;

        if (invert)
            valor2 = 1-valor2;

        // Apply threshold
        if (valor2 <= 0.5 - threshold ) {
            valor3 = valor2 * (0.5/(0.5-threshold));
        } else if (valor2 > 0.5 - threshold && valor2 < 0.5 + threshold) {
            valor3 = 0.5
        } else {
            valor3 = valor2 * (0.5 / (0.5-threshold)) + (1-(0.5 / (0.5-threshold)));
        }

        // Calculate speed curve
        var speed;
        if (valor3 < 0.5) {
            // lower speeds linear
            speed=2*valor3;
        } else {
            // higher speeds polynomial
            speed=Math.pow(2*valor3,3)
        }

        console.log(parseInt(valor2*100), parseInt(valor3*100), parseInt(speed*100))

        if (speed < 0.0625) speed = 0.0625;
        if (speed > 16) speed = 16;

        desiredSpeed = speed;

        if (!myTimer) {
            myTimer = setInterval(timerHandler, 100);
        }
    }


    function setUpWSS() {
        // Launch WebSocket
        const socket = new WebSocket(wss);

        socket.addEventListener('open', function (event) {
            socket.send('player');
        });

        socket.addEventListener('message', function (event) {
            dataHandler(event.data);
        });
    }

    setTimeout(setUpWSS, 1000);


})();
