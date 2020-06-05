import time

import speech_recognition as sr
import smtplib

message='SOMEONE CALLED OUT YOUR NAME!'
message2='SOMEONE CALLED OUT YOUR NAME IN A SENTENCE!'
email="sendtorohanvj@gmail.com"
passw="Rohan@123"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,passw)
def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached orZZZZZZZZZZZZ
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        #recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    maxvalue = 1000000000
    PROMPT_LIMIT = 10000

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(chunk_size=4096)

    # get a random word from the list
    word = 'Rohan'
    word2='rohan rohan'

    

    for i in range(maxvalue):
    
        print('Speak!'.format(i+1))
        for j in range(PROMPT_LIMIT):
            
            guess = recognize_speech_from_mic(recognizer, microphone)
           
            if guess["transcription"]:
                
                break
            if not guess["success"]:
                print("....")
                continue
            else:
                print("----")
            

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            continue

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))
        if guess["transcription"].find("Rohan")!=-1 or guess["transcription"].find("Roman")!=-1 and len(guess["transcription"])>5:
            message2=guess["transcription"]
            server.sendmail(email,email,message2)
           # server.quit()
            print("YOUR NAME WAS CALLED IN A SENTENCE, MAIL SENT")
        # determine if guess is correct and if any attempts remain
        guess_is_correct = (guess["transcription"].lower() == word.lower() or guess["transcription"].lower() == word2.lower())
        user_has_more_attempts = i < maxvalue - 1

        if guess_is_correct:
            
            server.sendmail(email,email,message)
           # server.quit()
            print("YOUR NAME WAS CALLED, MAIL SENT")
            continue
        