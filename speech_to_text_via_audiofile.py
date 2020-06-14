# NOTE: this example requires SpeechRecognition because it uses the recognizer class (pip install SpeechRecognition)

#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('male.wav') as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)

        #Adding french langauge option
       #text = r.recognize_google(audio_text, language = "fr-FR")

        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')
