
infos_cont = document.getElementById('container-after-start');
btn_start = document.getElementById('start-bot-btn');
btn_stop = document.getElementById('stop-bot-btn');



function startbot(){
    btn_stop.classList.remove('d-none');
    btn_start.classList.add('d-none');
    infos_cont.classList.remove('d-none')
};
function stopbot(){
    btn_stop.classList.add('d-none');
    btn_start.classList.remove('d-none');
    infos_cont.classList.add('d-none')

};



var socket = new WebSocket('ws://localhost:8000/dashboard');

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);


}
