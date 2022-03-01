// post.js

var main = function() {
    var div = document.createElement('div');
    div.innerHTML = '<p style="text-align: center;">（本文完）<br/>如果本文内容对你有帮助，欢迎小额赞赏。<br/></p>';
    div.innerHTML += '<div><table style="max-width: 96%;margin-left: auto; margin-right:auto; border-collapse:collapse; border: none;">' +
'<tbody><tr><td style="text-align: center;">支付宝</td><td style="border: none;"></td><td style="text-align: center;">微信</td></tr>' +
'<tr><td style="max-width: 40%;"><img src="http://media.linuxsand.info/image/pay/alipay.png"></td><td style="border: none;"></td>' +
'<td style="max-width: 40%;"><img src="http://media.linuxsand.info/image/pay/weixin.png"></td></tr></tbody></table></div>';
    div.style = "padding-top: 20px; padding-bottom: 40px;";

    document.body.append(document.createElement('hr'));
    //return;
    document.body.append(div);
}; // end main

