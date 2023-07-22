from gtts import gTTS
texts ="from manchester to madrid then to turin and then to man united .. excellence beyond valuation beyond forgery or imitation 18 year old since that trembling teenagaer"
language='en'
obj =gTTS(text=texts,lang=language,slow=False)
obj.save("sample.mp3")