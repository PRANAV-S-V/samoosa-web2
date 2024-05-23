// background.js

chrome.runtime.onStartup.addListener(function() {
    // Open a new tab to access the Flask app
    chrome.tabs.create({ url: 'http://localhost:5000' });

    // You can also log a message to the console to indicate that app.py is starting
    console.log('Starting app.py server...');
});
