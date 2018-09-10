//For Speech Recognition
window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition || null;

if (window.SpeechRecognition === null) {
    alert("Browser won't support");
}

else{

    var recognizer = new window.SpeechRecognition();
    var transcription = document.getElementById('nltext');
    var patience = 1;   // Time in seconds to wait before the recorder stops

    recognizer.continuous = false;


    function restartTimer() {
        timeout = setTimeout(function() {
            recognizer.stop();
            sendData();
        }, patience * 1000);
    }

    
    recognizer.onresult = function(event) 
    {
        transcription.textContent = '';

        for (var i = event.resultIndex; i < event.results.length; i++){
            
            if (event.results[i].isFinal){
                
                transcription.value = event.results[i][0].transcript;
                console.log("Recording is done");
                restartTimer();
            }
            
            else{
                transcription.value += event.results[i][0].transcript;
            }
        }
    };


    document.getElementById('startRecording').addEventListener('click', function() {
        
        // Set if we need interim results
        recognizer.interimResults = false;

        //Play a sound to acknowledge
        PlaySound();

        try{

            recognizer.start();
            console.log("Recognition started")
        }
        
        catch(ex){

            console.log('Recognition error: ' + ex.message)
        }
    });


    function PlaySound() {
        
        var sound = document.getElementById("audio");
        sound.play()
    }

}