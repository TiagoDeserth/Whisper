# 🎙️Transcrição de Áudio com Whisper

Este projeto utiliza o modelo [Whisper](https://github.com/openai/whisper) da Open AI para transcrever arquivos de áudio `.mp3`, `.m4a`, `.wav`, etc.

Ideal para transcrição de músicas, podcasts, entrevistas e outros tipos de áudio.

---

## ✅ Requisitos

- 🐍 Python 3.7 ou superior;
- ⬇ pip;
- 📂 FFmpeg (para leitura de áudio);
   - Download: [FFmpeg](https://ffmpeg.org/download.html);
   - Extraia a pasta e adicione o caminho da pasta `bin` nas variáveis de ambiente do sistema.
- (Opcional) GPU com CUDA para acelerar o processo.

---

## ⚙️ Instalação

### 1. Clone este repositório ou crie seu próprio script

```
pip install -U openai-whisper
pip install ffmpeg-python
 ```

#### Certifique-se que o FFmpeg foi instalado corretamente.

```
ffmpeg -version
```

---

Observações importantes

⏳ O modelo ``large`` é mais lento que os menores, mas muito mais preciso.

⚡ É possível alterar o modelo, basta alterar:

```
model = whisper.load_model("base")
```

``
tiny
base
small
medium
large
``

🌍 Não é necessário informar o idioma, pois o Whisper detecta automaticamente, mas é possível espeficiar para aumentar a precisão.