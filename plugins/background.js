chrome.webNavigation.onCompleted.addListener(function( tab ){
　　sendMsg( tab.tabId );
});

chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
    var url = request.url;
    var html = request.html;
    fetch('http://10.0.0.105:4888/api/browsersync', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url,
        html: html,
      })
    })
});

function sendMsg( tabid ){
　　chrome.tabs.sendMessage(tabid, {greeting: "start working"}, function(response) {
　　});
}
