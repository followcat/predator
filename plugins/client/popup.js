function onWindowLoad() {
    window.document.getElementById('id').innerHTML = localStorage['id'];
    window.document.getElementById('url').innerHTML = localStorage['url'];
    window.document.getElementById('result').innerHTML = localStorage['result'];
}

window.onload = onWindowLoad;
