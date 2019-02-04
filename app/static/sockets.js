// Connect to Socket
var socket = io.connect('http://' + document.domain + ':' + location.port);


// Send input data to server
function sendData(){

    var inputbox = document.getElementById("nltext");
    console.log(inputbox.value)
    if(inputbox.value == 'compile')
    {
        // console.log("Compile");
        var current_code = document.getElementById('outcode');

        var code_copy = current_code.textContent || current_code.innerText;
        // console.log(code_copy);

        //Paste the copied code into a file
        socket.emit('generate_output', {data: code_copy});
        console.log("Socket emited");

    }
    else{
        socket.emit('nl_event', {data: inputbox.value });
    }
    inputbox.value = '';
    return false;

}


// Recieve output Code from server and place in outputBox
socket.on('nl_event', function(data) {
    
    console.log("Message reveived: " + data);
    var outputBox = document.getElementById("outcode");
    datacode = hljs.highlight('python', data);
    outputBox.insertAdjacentHTML( 'beforeend', datacode.value);

});


// Place the output of the complied code in output box
socket.on('compile', function(data) {
    
    $('body,html').animate({scrollTop: $(window).height()}, 800);

    var outputBox = document.getElementById("output_area");
    datacode = hljs.highlight('python', data);
    outputBox.innerHTML = datacode.value

});
