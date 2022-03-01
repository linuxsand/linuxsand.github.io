// post.js

var main = function() {
    var div = document.createElement('div');
    div.innerHTML = '<p style="text-align: center;">（本文完）<br/><br/></p>';
    div.innerHTML += '<div><table style="width: 480px;margin-left: auto; margin-right:auto; border-collapse:collapse; border: none;">' +
'<tbody><tr><td style="text-align: center;">支付宝打赏</td><td style="border: none;"></td><td style="text-align: center;">微信打赏</td></tr>' +
'<tr><td><img style="max-width: 200px;" src="http://media.linuxsand.info/image/pay/alipay.png"></td><td style="border: none;"></td>' +
'<td><img style="max-width: 200px;" src="http://media.linuxsand.info/image/pay/weixin.png"></td></tr></tbody></table></div>';
    div.style = "padding-top: 20px; padding-bottom: 40px;";

    document.body.append(document.createElement('hr'));
    //return;
    document.body.append(div);
}; // end main

