// Listen for messages

chrome.runtime.onMessage.addListener(
    function(message, sender, sendResponse) {
        var url = window.location.href;
        var html = document.documentElement.outerHTML;
        sendMsg(url, html, "end");
});

function sendMsg(url, html, cmd){
　   chrome.extension.sendMessage({"url": url, "html": html, "cmd": cmd},
                                 function(response) {});
}
