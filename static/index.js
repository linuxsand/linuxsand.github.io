var main = function() {
    let blacklist = [
        "fcc83_tutorial.html",
        "my-2016.html",
        "my-2015.html",
        "my-2014.html",
        "xinjing-and-seal-cutting.html",
        "merida-warrior-500.html",
        "hangout-2.html",
        "fengtang-poems.html",
        "hangout-1.html",
        "insensitive-people.html",
        "hometown-1.html",
        "best-xxx-in-2012.html",
        "offer.html",
        "manual-focus.html",
        "root-your-android-device.html",
        "trifles-2.html",
        "get-animal-farm.html",
        "trifles-1.html",
        "went-to-nanjing-again.html",
        "xinjing.html",
        "long-message-and-short-message.html",
        "using-bat-file-to-save-time-for-edit-apk-file.html",
        "root-huawei-android-phones.html",
        "the-life-of-others.html",
        "time-to-have-a-haircut-again.html"
    ];

    let liArray = document.getElementsByClassName("blog_title");
    let len = liArray.length;
    let postsCount = len;
    for (let index = 0; index < len; index++) {
        let parts = liArray[index].firstChild.href.split('/');
        let link = parts[parts.length-1];
        if (blacklist.includes(link)) {
            liArray[index].style.display = 'none';
            //console.log('hit one');
            postsCount--;
        }
    }
    return postsCount;
}; // end main



