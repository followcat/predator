// Listen for messages

function onWindowLoad() {
    var url = window.location.href;
    var html = document.documentElement.outerHTML;
    var email = document.getElementsByClassName('email')[0];
    var telephone = document.getElementsByClassName('telphone')[0];
    var base64email = getBase64Image(email);
    var base64phone = getBase64Image(telephone);
    sendMsg(url, html, base64email, base64phone, "end");
}

window.onload = onWindowLoad;

function sendMsg(url, html, base64email, base64phone, cmd){
　   chrome.extension.sendMessage({"url": url, "html": html, "cmd": cmd,
                                  "base64email": base64email, "base64phone": base64phone},
                                 function(response) {});
}

function getBase64Image(img) {
    // Create an empty canvas element
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    // Copy the image contents to the canvas
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    // Get the data-URL formatted image
    // Firefox supports PNG and JPEG. You could check img.src to
    // guess the original format, but be aware the using "image/jpg"
    // will re-encode the image.
    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}
