import pdfkit
from jinja2 import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Caminhos dos arquivos
template_path = 'templates/template.html'
output_pdf_path = 'output/relatorio.pdf'

# Caminho para o executável wkhtmltopdf (substitua pelo caminho real)
path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Carregar o template
with open(template_path) as file:
    template = Template(file.read())

# Dados para preencher o template
data = {
    'titulo': 'Relatório de Vendas',
    'conteudo': 'As vendas aumentaram 20% em relação ao mês anterior.'
}

# Preencher o template com os dados
html_filled = template.render(data)

# Converter HTML para PDF e salvar em 'output/relatorio.pdf'
pdfkit.from_string(html_filled, output_pdf_path, configuration=config)

# Configuração do servidor SMTP
from_addr = 'user@gmail.com'
to_addr = 'user@gmail.com'
password = ''

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Relatório'

# Corpo do e-mail
body = 'Segue em anexo o relatório solicitado.'
msg.attach(MIMEText(body, 'plain'))

# Anexar o PDF
filename = os.path.basename(output_pdf_path)
attachment = open(output_pdf_path, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {filename}')

msg.attach(part)

# Enviar o e-mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_addr, password)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()

print("E-mail enviado com sucesso!")