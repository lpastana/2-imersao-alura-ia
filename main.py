import AI
import json
import os
import streamlit as st
import pandas as pd
import openpyxl







def display_recommendations(data):
    if data !="":
        st.session_state.recommendations = data    
      
    with st.expander("Ver Recomendações", expanded=True):
        st.markdown("### Análise do Usuário")
        st.markdown(st.session_state.recommendations['Analise_usuario'])

        st.markdown("### Recomendações de Séries")
        for rec in st.session_state.recommendations['recomendacoes']:
            # Usando container para agrupar informações em vez de um expander aninhado
            with st.container():
                st.markdown(f"#### {rec['Titulo_ano']} ({rec['plataforma']})")
                st.markdown(f"**Sinopse:** {rec['Sinopse']}")
                st.markdown(f"**Motivo da escolha:** {rec['Motivo da escolha']}")
                st.markdown(f"**Nota:** {rec['Nota']}")
                st.markdown(f"**Status:** {rec['Status']}")
                st.markdown(f"**Tempo médio por episódio:** {rec['Tempo_medio_episodio']}")
                st.markdown(f"**Quantidade de episódios:** {rec['Quantidade_episodio']}")

        st.markdown("### Recomendação Final")
        st.markdown(f"**{st.session_state.recommendations['recomendacao_final']['titulo']}**")
        st.markdown(st.session_state.recommendations['recomendacao_final']['motivo'])
        # Botões de feedback abaixo do expander
        
        st.session_state.feedback = st.text_area("Algum ajuste a fazer ou outra série preferida para nos contar?",key="text_feedback_"+str(st.session_state.count))
        if st.button("Enviar Ajustes",key="button_feedback_"+str(st.session_state.count)):
            st.session_state.count+=1  
            st.session_state.new_recommendation=True
            st.session_state.show_recommendations = False
def load_excel(file):
    if file:
        df = pd.read_excel(file,dtype=str)
        df['Motivo']=df['Motivo'].fillna("Sem motivo")
        df=df.loc[(~df['Serie'].isna()) & (~df['Nota'].isna())]
        return df
    return None 

def initialize_session_state():
    if 'FLAG_TABELA' not in st.session_state:
        st.session_state.FLAG_TABELA = True
    if 'feedback' not in st.session_state:
        st.session_state.feedback = None
    if 'count' not in st.session_state:
        st.session_state.count = 0
    if 'recommendations' not in st.session_state:   
        st.session_state.recommendations = None
    if 'show_recommendations' not in st.session_state:
        st.session_state.show_recommendations = False
    if 'new_recommendation' not in st.session_state:
        st.session_state.new_recommendation = True
    if 'chat' not in st.session_state:
        with open('config.json') as f:
            config = json.load(f)
        print(config)
        st.session_state.chat = AI.AIManager(config)
     
def main():
    data_json=""
    initialize_session_state()
    st.title('Sistema de Recomendação de Seriado - Google Gemini')

    excel_file = st.file_uploader("Carregue seu arquivo Excel com todas as séries, notas e motivos que você já assistiu! Iremos sugerir novas séries para você maratonar!", type=['xlsx'])
    if excel_file:
        data = load_excel(excel_file)
        if data is not None:
            st.write("Aqui estão as primeiras linhas do seu arquivo:")
            if st.session_state.FLAG_TABELA:
                st.session_state.feedback = data.to_markdown()
            markdown_table_head=data.head().to_markdown()
            st.write(markdown_table_head)
            st.write(f"Sua base possui {len(data)} séries. Estamos enviando para o Google Gemini. Aguarde!")
            if st.session_state.new_recommendation:
                while True:
                    try:
                        response=st.session_state.chat.send_message(st.session_state.feedback)
                        break
                    except:
                        continue
                st.session_state.FLAG_TABELA=False
                st.session_state.show_recommendations=True
                st.session_state.new_recommendation=False
                if st.session_state.show_recommendations:
                    while True:
                        try:
                            data_json = json.loads(response.text)
                            break
                        except Exception as e:
                            print(e)
                            while True:
                                try:
                                    response=st.session_state.chat.send_message(st.session_state.feedback)
                                    break
                                except:
                                    continue

            display_recommendations(data_json)
            
   


    
      
    

if __name__ == "__main__":
    main()
    




