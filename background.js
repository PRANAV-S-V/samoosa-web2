// background.js

chrome.runtime.onInstalled.addListener(function() {
    chrome.tabs.create({ url: 'http://localhost:4000' });
});
