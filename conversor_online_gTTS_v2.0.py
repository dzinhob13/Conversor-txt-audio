import customtkinter as ctk
from gtts import gTTS
import io
from pygame import mixer
from tkinter import messagebox, filedialog
from datetime import datetime  # Importado para pegar data e hora

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("TTS Pro - CONVERSOR DE TXT/AUDIO")
        self.geometry("600x600")
        ctk.set_appearance_mode("dark")
        
        # Inicialização do Mixer
        mixer.init()
        self.pausado = False

        # --- UI ---
        self.label = ctk.CTkLabel(self, text="Conversor de Texto em Áudio", font=("Arial", 20, "bold"))
        self.label.pack(pady=15)

        self.label_voz = ctk.CTkLabel(self, text="Escolha a Voz/Idioma:")
        self.label_voz.pack()
        
        self.opcoes_vozes = {
            "Português (Brasil)": "pt",
            "Português (Portugal)": "pt-pt",
            "Inglês (EUA)": "en",
            "Espanhol": "es",
            "Francês": "fr",
            "Japonês": "ja"
        }
        self.combo_vozes = ctk.CTkOptionMenu(self, values=list(self.opcoes_vozes.keys()))
        self.combo_vozes.pack(pady=5)
        self.combo_vozes.set("Português (Brasil)")

        self.txt_input = ctk.CTkTextbox(self, width=500, height=180)
        self.txt_input.pack(pady=15)
        self.txt_input.insert("2.0", "Digite o texto aqui ...")

        self.frame_controles = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_controles.pack(pady=10)

        self.btn_play = ctk.CTkButton(self.frame_controles, text="▶ Play", width=120, command=self.ouvir_direto)
        self.btn_play.grid(row=0, column=0, padx=5)

        self.btn_pause = ctk.CTkButton(self.frame_controles, text="⏸ Pause", width=100, command=self.pausar_audio, fg_color="orange", hover_color="#cc8400")
        self.btn_pause.grid(row=0, column=1, padx=5)

        self.btn_stop = ctk.CTkButton(self.frame_controles, text="⏹ Stop", width=100, command=self.parar_audio, fg_color="red", hover_color="#a10000")
        self.btn_stop.grid(row=0, column=2, padx=5)

        # Botão Download
        self.btn_download = ctk.CTkButton(self, text="💾 Baixar Áudio (.mp3)", width=250, command=self.baixar_audio, fg_color="#27ae60", hover_color="#1e8449")
        self.btn_download.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Status: Pronto", text_color="gray")
        self.status_label.pack(pady=10)

    def ouvir_direto(self):
        if self.pausado:
            mixer.music.unpause()
            self.pausado = False
            self.status_label.configure(text="Status: Reproduzindo...", text_color="#2ecc71")
            return

        texto = self.txt_input.get("1.0", "end-1c")
        if not texto.strip():
            messagebox.showwarning("Aviso", "Digite um texto para converter!")
            return

        try:
            self.status_label.configure(text="Status: Gerando áudio...", text_color="orange")
            self.update()

            idioma_selecionado = self.opcoes_vozes[self.combo_vozes.get()]
            tts = gTTS(text=texto, lang=idioma_selecionado, slow=False)
            
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            
            mixer.music.load(fp)
            mixer.music.play()
            self.status_label.configure(text="Status: Reproduzindo...", text_color="#2ecc71")
            self.pausado = False
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")
            self.status_label.configure(text="Status: Erro", text_color="red")

    def pausar_audio(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.pausado = True
            self.status_label.configure(text="Status: Pausado", text_color="yellow")

    def parar_audio(self):
        mixer.music.stop()
        self.pausado = False
        self.status_label.configure(text="Status: Parado (Início)", text_color="gray")

    def baixar_audio(self):
        texto = self.txt_input.get("1.0", "end-1c")
        if not texto.strip():
            messagebox.showwarning("Aviso", "Digite um texto para baixar!")
            return

        # --- Lógica de Data e Hora ---
        # Formato: audio_DD-MM-YYYY_HH-MM-SS.mp3
        agora = datetime.now()
        nome_sugerido = agora.strftime("audio_%d-%m-%Y_%H-%M-%S.mp3")

        caminho_arquivo = filedialog.asksaveasfilename(
            initialfile=nome_sugerido, # Define o nome padrão na janela
            defaultextension=".mp3",
            filetypes=[("Arquivos de Áudio", "*.mp3")],
            title="Salvar Áudio como"
        )

        if caminho_arquivo:
            try:
                self.status_label.configure(text="Status: Salvando arquivo...", text_color="orange")
                self.update()

                idioma_selecionado = self.opcoes_vozes[self.combo_vozes.get()]
                tts = gTTS(text=texto, lang=idioma_selecionado, slow=False)
                tts.save(caminho_arquivo)

                self.status_label.configure(text="Status: Download concluído!", text_color="#2ecc71")
                messagebox.showinfo("Sucesso", f"Áudio salvo como:\n{nome_sugerido}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")
                self.status_label.configure(text="Status: Erro no download", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()