# Envio de Relatório por E-mail com PDF

Este projeto demonstra como gerar um PDF a partir de um template HTML e enviá-lo como anexo em um e-mail utilizando Python. Utiliza as bibliotecas `pdfkit`, `jinja2`, e `smtplib` para criar e enviar o relatório.

## Como rodar esse projeto?

1. Clone o repositório:
```bash
https://github.com/lorenzouriel/generate-template-and-send-email.git
cd generate-template-and-send-email
```

2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Instale as dependência: 
```bash
pip install -r requirements.txt
```

4. Além disso, você deve ter o executável wkhtmltopdf instalado no seu sistema. Baixe o [wkhtmltopdf](https://wkhtmltopdf.org/) e atualize o caminho do executável no código.


## Estrutura do Projeto
```bash
project/
│
├── templates/
│   └── template.html
├── output/
│   └── relatorio.pdf
└── main.py
```

- `templates/template.html`: Arquivo HTML utilizado como template para o PDF.
- `output/relatorio.pdf`: PDF gerado a partir do template.
- `main.py`: Script Python que gera o PDF e envia o e-mail.


## Configuração
1. Atualize o caminho para o executável wkhtmltopdf no seu sistema:
```python
path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
```

2. Atualize as configurações do servidor SMTP com suas informações:
```python
from_addr = 'user@gmail.com'
to_addr = 'user@gmail.com'
password = 'your_password'
```

## Uso
1. Crie um arquivo `template.html` na pasta `templates/` com o conteúdo HTML desejado.

2. Execute o script Python para gerar o PDF e enviar o e-mail:
```bash
python main.py
```

---
---
---

# Send Report by E-mail with PDF

This project demonstrates how to generate a PDF from an HTML template and send it as an attachment in an email using Python. Use the `pdfkit`, `jinja2`, and `smtplib` libraries to create and send the report.

## How to run this project?

1. Clone the repository:
```bash
https://github.com/lorenzouriel/generate-template-and-send-email.git
cd generate model and send email
```

2. Configure the correct Python version with `pyenv`:
```bash
pyenv 3.11.5 installation
pyenv local 3.11.5
```

3. Install dependencies: 
```bash
pip install -r requirements.txt
```

4. Also, you must have the new wkhtmltopdf installed on your system. Download [wkhtmltopdf](https://wkhtmltopdf.org/) and update the path of the following in the code.


## Project Structure
```bash
project/
│
├── models/
│ └── template.html
├── exit/
│ └── report.pdf
└── main.py
```

- `templates/template.html`: HTML file used as a template for the PDF.
- `output/relatorio.pdf`: PDF generated from the template.
- `main.py`: Python script that generates the PDF and sends the email.


## Settings
1. Update the path to the new wkhtmltopdf on your system:
```python
path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
```

2. Update the SMTP server settings with your information:
```python
from_addr = 'usuario@gmail.com'
to_addr = 'usuario@gmail.com'
password = 'your_password'
```

## Usage
1. Create a `template.html` file in the `templates/` folder with the desired HTML content.

2. Run the Python script to generate the PDF and send the email:
```bash
python main.py
```
