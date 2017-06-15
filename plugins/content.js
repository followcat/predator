// Listen for messages

function onWindowLoad() {
    var url = window.location.href;
    var html = document.documentElement.outerHTML;
    sendMsg(url, html, "end");
}

window.onload = onWindowLoad;

function sendMsg(url, html, cmd){
　   chrome.extension.sendMessage({"url": url, "html": html, "cmd": cmd},
                                 function(response) {});
}
