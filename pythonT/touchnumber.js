//無名関数でくくる
(function() {
var size = 3;
var currentNum;
var timer;
var startTime;
var isPlaying = false;
var misTouch;

document.getElementById('timerStart').onclick = function(){
    var radiolist = document.getElementsByName('radio_size');
    var setSize = 3;

    for (var i=0; i<radiolist.length; i++) {
        if (radiolist[i].checked) {
            setSize = radiolist[i].value;
        }
    }

    timerStart(setSize);
}

function timerStart(n) {
    //ボードのサイズを変える
    if (n >= 3)
    {
        size = n;
    }

    initBoard();
    currentNum = 1;
    startTime = (new Date()).getTime();
    misTouch = 0;



    if (!isPlaying) {
        isPlaying = true;
        runtimer();
    }

}

function createButton(num) {
    var btn;
    btn = document.createElement('input');
    btn.type='button';
    btn.value = num+1;

    btn.onclick =function(){
        if (this.value == currentNum) {
            this.disabled = true;
            this.value = "*";
            currentNum++;
        }
        else
        {
            misTouch++;
        }
        if (currentNum == size * size +1) {
            clearTimeout(timer);
            alert('Your Ecore : ' + document.getElementById('time').innerHTML);
            isPlaying = false;
        }
    }
    return btn;
}
//ボードの作成
function initBoard() {
    var buttons = [];
    var board;
    var button;

    //ボタンの生成
    for (var i=0; i < size * size; i++) {
        buttons.push(createButton(i));
    }

    board = document.getElementById('board');
    //現在のボタンを消し込む
    while (board.firstChild){
        board.removeChild(board.firstChild);
    }
    while (buttons.length) {
        button = buttons.splice(Math.floor(Math.random() * buttons.length), 1);
        board.appendChild(button[0]);
        //区切り線
        if (buttons.length % size == 0)
        {
            board.appendChild(document.createElement('br'));
        }
    }
}

//タイマー表示
function runtimer() {
    document.getElementById('time').innerHTML = (((new Date()).getTime() - startTime) / 1000).toFixed(1);
    document.getElementById('misTouch').innerHTML = misTouch;
    timer =setTimeout(function() {
        runtimer();
    }, 100)
}
})();
