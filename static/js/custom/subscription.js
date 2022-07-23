// const networkelement = document.getElementById('network')

// network.onchange(() =>{
//     var selectedone = network.value + '.png';
//     console.log(selectedone)
//     // const imgele = document.getElementById('qrimg') 
//     // imgele.setAttribute('src', '/static/images/' + selectedone);
// })

function changeNetwork(network){
    var selectedvalue= '/static/images/' + network.value + '.png';
    console.log(selectedvalue);
    const imgelement = document.getElementById('qrimg');
    imgelement.setAttribute('src', selectedvalue);
}