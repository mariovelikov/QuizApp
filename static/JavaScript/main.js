window.onload = initall()
var saveBtn;


function initall() {
    saveBtn = document.getElementById('save_ans')
    saveBtn.onclick = saveAns
}

function saveAns() {
    var ans = $('input:radio[name=name]:checked').val()
    alert('Answer is submitted !!!')

    var req = new XMLHttpRequest();
    var url = 'saveans?ans=' + ans
    console.log(req)

    req.open('GET', url, true)
    req.send()
}