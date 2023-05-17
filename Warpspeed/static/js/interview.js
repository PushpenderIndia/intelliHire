// Get the necessary DOM elements
var gifBox = document.getElementById('gif-box');
var speakButton = document.getElementById('speak-button');

let mediaRecorder;
let recordedChunks = [];
let audioUrl;
localStorage.setItem('question_no', 1);
let question_no = sessionStorage.getItem("question_no");

// Add event listeners
speakButton.addEventListener('mousedown', startRecording);
speakButton.addEventListener('mouseup', stopRecording);
speakButton.addEventListener('mouseleave', stopRecording);

// Function to start recording
function startRecording() {
  // Request access to the user's microphone
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(stream) {
      // Create a new MediaRecorder instance
      mediaRecorder = new MediaRecorder(stream);

      // Add event listeners to handle the data
      mediaRecorder.addEventListener('dataavailable', function(e) {
        recordedChunks.push(e.data);
      });

      // Start recording
      mediaRecorder.start();
    })
    .catch(function(error) {
      console.error('Error accessing microphone:', error);
    });
}

// Function to stop recording and send the voice to the backend
function stopRecording() {
    // Stop recording
    mediaRecorder.stop();

    // Clear the recorded chunks
    recordedChunks = [];

    // Retrieve the session_id from URL query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const interview_id = urlParams.get('id');

    // Check if the interview_id exists
    if (interview_id) {
        // TODO: Send the voice to the backend

        // Create FormData object to send the recorded audio to the backend
        var formData = new FormData();
        formData.append('voice', new Blob(recordedChunks), 'voice.mp3');
        formData.append('question_no', question_no);
        formData.append('interview_id', interview_id);
        question_no += 1;
        localStorage.setItem('question_no', question_no);

        // Make an AJAX request to send the recorded audio to the backend
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/ask_follow_ups', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Handle the response from the backend
                var response = JSON.parse(xhr.responseText);
                var responseAudio = response.response;
                var responseType = response.type;

                // Play the response audio
                var audio = new Audio(responseAudio);
                audio.play();

                // Set the GIF to Talking.gif when audio is playing
                var gifElement = document.getElementById('gif-box');
                gifElement.src = '/static/img/Idle.gif';

                // Update the GIF based on the response type
                
                if (responseType.includes("200")) {
                    gifElement.src = '/static/img/Talking.gif';
                } else if (responseType.includes("500")) {
                    gifPath = '/static/img/Error.gif';
                }

                // Set the GIF back to Idle.gif when audio playback ends
                audio.addEventListener('ended', function() {
                    gifElement.src = '/static/img/Idle.gif';
                });
            }
        };
        xhr.send(formData);
    }
}

function playFirstQuestion(first_audio, total_ques_to_ask) {
    console.log("First Audio: ", first_audio);
    console.log("Total Question: ", total_ques_to_ask);
    localStorage.setItem('total_ques_to_ask', total_ques_to_ask);
  
    // Create an audio element
    const audio = new Audio();
    audio.src = first_audio;
  
    // Get the button and gifBox elements
    var startButton = document.getElementById('start_interview');
    var gifBox = document.getElementById('gif-box');
  
    // Play the audio when the button is clicked
    startButton.addEventListener('click', function() {
      // Remove the button from the page
      startButton.remove();
      gifBox.style.backgroundImage = 'url(/static/img/Talking.gif)';
      var hiddenQues = document.getElementById('hiddenQues');
      hiddenQues.style.display = 'block';
  
      audio.play();
    });
  
    // Handle the audio 'ended' event
    audio.addEventListener('ended', function() {
      console.log("Audio Ended!")
      gifBox.style.backgroundImage = 'url(/static/img/Idle.gif)';
      var hiddenButton = document.getElementById('speak-button');
      hiddenButton.style.display = 'block';
    });
}
  