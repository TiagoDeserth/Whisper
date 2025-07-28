import whisper

model = whisper.load_model("base")

result = model.transcribe(r"C:\Users\tiago\Nova Era.m4a",
 language="pt", 
 task = "transcribe",
 fp16 = False,
 verbose = True)

print("Transcrição:")
print(result["text"])