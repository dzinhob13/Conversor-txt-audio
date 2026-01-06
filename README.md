# 🎙️ Conversor de Texto para Áudio Pro (TTS & Translator)

Uma aplicação desktop potente e elegante que transforma textos (digitados ou importados) em áudios de alta fidelidade. O sistema conta com tradução automática integrada e suporte para diversos formatos de documentos.

---

## ✨ Funcionalidades Principais

* **Conversão Inteligente:** Utilize múltiplos motores de voz (`Edge-TTS`, `gTTS`, `Azure`) para obter a melhor qualidade sonora.
* **Tradução Automática:** Converta o texto para outro idioma antes de gerar o áudio de forma transparente.
* **Leitura de Documentos:** Suporte nativo para processar arquivos **.pdf** e **.docx** diretamente na interface.
* **Interface Moderna:** GUI desenvolvida com `CustomTkinter` em modo escuro (Dark Mode) nativo, otimizada para 600x600.
* **Exportação Flexível:** Ouça o áudio instantaneamente via player integrado ou faça o download em formato MP3.
* **Ferramentas de Automação:** Integração com `PyAutoGUI` e `Clipboard` para facilitar o fluxo de trabalho.

---

## 🛠️ Tecnologias e Dependências

O projeto utiliza um conjunto robusto de bibliotecas para garantir performance e compatibilidade:

### **Interface e Gráficos**
* `CustomTkinter`: Interface moderna e responsiva.
* `Darkdetect`: Detecção automática do tema do sistema.
* `Pygame`: Motor para reprodução de áudio em tempo real.

### **Motores de Voz (TTS)**
* `Edge-TTS`: Vozes neurais de alta qualidade da Microsoft.
* `gTTS`: Google Text-to-Speech para conversão rápida.
* `Pyttsx3`: Suporte offline para vozes do sistema operacional.

### **Processamento de Dados**
* `PyPDF2` & `python-docx`: Extração de texto de documentos.
* `Requests` & `Aiohttp`: Comunicação com APIs de tradução e serviços web.
* `Selenium`: Automação para coleta de dados ou serviços web adicionais.

---

## 🚀 Como Instalar e Rodar

### 1. Requisitos
Certifique-se de ter o **Python 3.10+** instalado.

### 2. Instalação das Dependências
Com o terminal aberto na pasta do projeto, execute:
```bash
pip install -r requirements.txt
