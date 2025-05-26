import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Meu Site em Python", page_icon="🌐", layout="centered")

# Título
st.title("🌐 Meu Site em Python com Streamlit")

# Subtítulo
st.subheader("🚀 Bem-vindo ao meu site!")

# Texto de introdução
st.write("""
Este é um site simples feito em Python com **Streamlit**.

Aqui você encontra:
- Formulários interativos
- Gráficos dinâmicos
- Opções de download
- Muito mais!
""")

# Imagem (opcional, pode trocar pela sua)
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=300)

# Input de texto
nome = st.text_input("Digite seu nome:")

# Botão de saudação
if st.button("Enviar"):
    st.success(f"Olá, {nome}! Seja bem-vindo ao meu site.")

# Checkbox
if st.checkbox("Mostrar mais informações"):
    st.info("Streamlit é uma ótima ferramenta para criar aplicações web interativas de forma rápida e simples.")

# Gráfico interativo
st.subheader("📊 Gráfico de Exemplo")

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(data)

# Formulário
st.subheader("📥 Formulário de Contato")

with st.form("contact_form"):
    nome_form = st.text_input("Nome")
    email = st.text_input("Email")
    mensagem = st.text_area("Mensagem")
    enviado = st.form_submit_button("Enviar")

    if enviado:
        st.success("Mensagem enviada com sucesso!")

# Download de arquivo
st.subheader("📄 Baixe um exemplo de arquivo:")

csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    "Baixar CSV",
    data=csv,
    file_name='dados_exemplo.csv',
    mime='text/csv'
)

# Sidebar
st.sidebar.title("📂 Menu")
st.sidebar.write("Aqui é a barra lateral!")

st.sidebar.header("🔗 Links úteis")
st.sidebar.markdown("[Documentação do Streamlit](https://docs.streamlit.io/)")

st.sidebar.header("⚙️ Ajustes")
option = st.sidebar.selectbox(
    'Escolha uma opção:',
    ('Página inicial', 'Sobre', 'Contato')
)

# Exibição conforme a opção
if option == 'Sobre':
    st.write("Este site foi criado para demonstrar o uso do Streamlit.")
elif option == 'Contato':
    st.write("Entre em contato pelo email: exemplo@site.com")

