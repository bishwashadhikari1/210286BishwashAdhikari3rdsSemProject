
function changeNetwork(network){
    var selectedvalue= '/static/images/' + network.value + '.png';
    console.log(selectedvalue);
    const imgelement = document.getElementById('qrimg');
    imgelement.setAttribute('src', selectedvalue);
}