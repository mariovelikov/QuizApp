window.onload = initAll()
var saveBtn;


function initAll() {
    saveBtn = document.getElementById('save_ans')
    saveBtn.onclick = saveAns
}

function saveAns() {
    var ans = $('input:radio[name=name]:checked').val()

    var req = new XMLHttpRequest();
    var url = 'saveans?ans=' + ans

    req.open('GET', url, true)
    req.send()
}