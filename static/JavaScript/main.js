window.onload = initAll;

function initAll() {
    let saveBtn = document.getElementById('save_ans');
    saveBtn.addEventListener('click', saveAns)
}

function saveAns() {
    const ans = document.querySelector('input:checked').value;

    let req = new XMLHttpRequest();
    let url = 'saveans?ans=' + ans

    req.open('GET', url, true)
    req.send()
}
