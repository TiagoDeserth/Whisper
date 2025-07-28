import whisper

model = whisper.load_model("base")

result = model.transcribe(r"C:\Users\tiago\Desktop\Áudio do WhatsApp de 2025-07-25 à(s) 20.48.54_290464ce.waptt.opus",
 language="pt", 
 task = "transcribe",
 fp16 = False,
 verbose = True)

print("Transcrição:")
print(result["text"])