import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util
import torch


def get_ai_response(message):

    genai.configure(api_key="AIzaSyBWtBc6lLG7O4N1H-9oGgAOeJI3CYKodxw")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    embedder = SentenceTransformer('all-mpnet-base-v2')

    ongs_confiaveis = [
            {
                "name": "ONG UNIDOS E SOLIDÁRIOS",
                "website": "N/A",
                "rating": 5,
                "reviews": 26
            },
            {
                "name": "Instituto Curicaca",
                "website": "http://www.curicaca.org.br/",
                "rating": 5,
                "reviews": 9
            },
            {
                "name": "Associação dos Angolanos e Amigos do Rio Grande do Sul",
                "website": "https://www.associacaodosangolanos.ong.br/",
                "rating": 5,
                "reviews": 8
            },
            {
                "name": "Ong UMTOS 'Um por Todos e Todos por Um'",
                "website": "N/A",
                "rating": 5,
                "reviews": 2
            },
            {
                "name": "Ong Criança Sul Brasil",
                "website": "https://ong-crianca-sul-brasil.ueniweb.com/?utm_campaign=gmb",
                "rating": 5,
                "reviews": 1
            },
            {
                "name": "Ong UMTOS 'Um por Todos e Todos por Um'",
                "website": "N/A",
                "rating": 5,
                "reviews": 2
            },
            {
                "name": "Associação dos Angolanos e Amigos do Rio Grande do Sul",
                "website": "https://www.associacaodosangolanos.ong.br/",
                "rating": 5,
                "reviews": 8
            },
            {
                "name": "Ong Criança Sul Brasil",
                "website": "https://ong-crianca-sul-brasil.ueniweb.com/?utm_campaign=gmb",
                "rating": 5,
                "reviews": 1
            },
            {
                "name": "ONG Vale A Vida",
                "website": "N/A",
                "rating": 4.8,
                "reviews": 5
            },
            {
                "name": "Fundação de Proteção Especial do Rio Grande do Sul",
                "website": "N/A",
                "rating": 5,
                "reviews": 1
            },
            {
                "name": "Instituto Curicaca",
                "website": "http://www.curicaca.org.br/",
                "rating": 5,
                "reviews": 9
            },
            {
                "name": "Casa do Menor",
                "website": "https://www.casadomenor.com.br/",
                "rating": 4.6,
                "reviews": 7
            }
            ]

    banco_de_dados = [f"""Olá, sou a Maitê, uma inteligência artificial especializada em engenharia civil.\nEstou aqui para conscientizar você sobre os acontecimentos trágicos que atingiram o Rio Grande do Sul.\nAs recentes enchentes deixaram um rastro de destruição, afetando milhões de pessoas em diversos municípios.\nA situação é crítica, com vidas perdidas, desabrigados e uma infraestrutura severamente danificada. É essencial que todos estejam cientes da gravidade dessa situação e unam esforços para ajudar as vítimas e reconstruir o estado.\n\nVamos juntos entender a importância de ações como doações, voluntariado e a busca por soluções de longo prazo para evitar que tragédias como essa se repitam. A solidariedade e a conscientização são fundamentais nesse momento difícil.\n\nVamos conversar sobre como cada um de nós pode fazer a diferença e ajudar o Rio Grande do Sul a se recuperar dessa adversidade.\n\nEnchentes no Rio Grande do Sul: Uma Situação Crítica e Como Você Pode Ajudar\nO Rio Grande do Sul enfrenta um dos piores momentos de sua história recente, com inundações devastadoras que afetam mais de 1,9 milhão de pessoas em 437 municípios. Até o dia 10 de maio, 116 óbitos foram confirmados, com 143 pessoas ainda desaparecidas. As fortes chuvas causaram alagamentos, deslizamentos de terra e o colapso de infraestrutura, deixando cidades isoladas e milhares de pessoas desabrigadas ou desalojadas. A situação é particularmente crítica em regiões como o Litoral Norte e a Serra Gaúcha, onde o volume de água atingiu níveis históricos. Diante da tragédia, a população se une em esforços de resgate, apoio e solidariedade. Diversas iniciativas estão em curso para auxiliar as vítimas das enchentes, desde a doação de alimentos, roupas e itens de higiene até o envio de equipes de voluntários para auxiliar nas ações de salvamento e limpeza. Se você deseja contribuir para ajudar o Rio Grande do Sul neste momento difícil, diversas opções estão disponíveis:\n\nLista de ongs confiaveis para doar com nomes, sites, nota e avaliações: {ongs_confiaveis},\nDoe alimentos, roupas, colchões, cobertores, produtos de higiene pessoal e outros itens de necessidade básica. Diversos pontos de coleta estão espalhados pelo estado. Você pode encontrar uma lista atualizada no site do governo do Rio Grande do Sul (https://www.rs.gov.br/) ou em organizações de ajuda humanitária como a Cruz Vermelha (https://www.cruzvermelha.org.br/) e o Caritas (https://caritas.org.br/).\nFaça doações em dinheiro para instituições confiáveis. Diversas campanhas de arrecadação estão em andamento. Você pode encontrar uma lista de instituições no site do governo do Rio Grande do Sul (https://www.rs.gov.br/) ou em organizações de ajuda humanitária como a Ação da Cidadania (https://www.acaodacidadania.org.br/) e o Movimento pela Ética Contábil (https://www.unitins.br/RepositorioDigital/Publico/Home/BaixarPDF/377).\nSe você possui habilidades específicas, como medicina, engenharia ou logística, você pode se voluntariar para ajudar nas ações de resgate e reconstrução. Diversas organizações estão buscando voluntários para auxiliar nas mais diversas atividades. Você pode encontrar uma lista de oportunidades no site do governo do Rio Grande do Sul (https://www.rs.gov.br/) ou em organizações de ajuda humanitária como a Cáritas Brasileira (https://caritas.org.br/) e o Movimento pela Ética Contábil (https://www.unitins.br/RepositorioDigital/Publico/Home/BaixarPDF/377).\nToda ajuda é importante neste momento. A união e a solidariedade da população são fundamentais para auxiliar as vítimas das enchentes e reconstruir o Rio Grande do Sul. Além das ações de ajuda imediata, é importante também pensar em medidas a longo prazo para prevenir novas tragédias. É necessário investir em infraestrutura adequada, planejamento urbano sustentável e conscientização ambiental para evitar que eventos climáticos extremos como as enchentes se repitam no futuro. A situação no Rio Grande do Sul é crítica, mas a esperança não se apaga. A força e a resiliência do povo gaúcho, junto com a ajuda de todos, superarão este momento difícil e reconstruirão um estado mais forte e próspero. Juntos, podemos fazer a diferença!\nAs inundações no Rio Grande do Sul causaram um enorme sofrimento e despertaram a solidariedade da população. Infelizmente, essa onda de generosidade também atraiu oportunistas que criam Pix falsos para se aproveitar da situação.\n\nPara combater essa prática e garantir que suas doações cheguem ao destino correto, siga estas dicas:\nImportante! Esse chat bot é feito para combater as fake news, atráves de uma conversa simples e educativa sobre os acontecimentos trágicos no rio grande do sul.\nVerifique a fonte da chave Pix:\n\n- Confirme se a chave Pix foi divulgada por canais oficiais do governo do Rio Grande do Sul ou por instituições de renome.\n- Desconfie de solicitações em redes sociais, grupos de mensagens ou sites não confiáveis.\n- Acesse os sites oficiais do governo do Rio Grande do Sul (https://www.rs.gov.br/) e de instituições confiáveis como a Cruz Vermelha (https://www.cruzvermelha.org.br/) e o Caritas (https://caritas.org.br/) para encontrar as chaves Pix oficiais.\n\nAnalise as informações da chave Pix:\n\n- O nome do destinatário deve ser exatamente o mesmo da instituição oficial.\n- Evite chaves Pix com nomes genéricos ou que não façam sentido.\n- Fique atento a erros ortográficos ou inconsistências na chave Pix.\n\nConfirme a transação antesde finalizar:
                        Ao digitar a chave Pix no seu aplicativo bancário, verifique se os dados da instituição beneficiária correspondem    aos da fonte oficial que você consultou.
                        - Em caso de dúvidas, não finalize a transação.
                        - Entre em contato com a instituição oficial para confirmar a chave Pix antes de realizar a doação.

                        Denuncie Pix falsos:
                        - Se você identificar uma chave Pix falsa, denuncie-a para as autoridades.
                        - Você pode fazer a denúncia no site da Polícia Civil do Rio Grande do Sul (https://www.pc.rs.gov.br/) ou no site do Banco Central do Brasil ([URL inválido removido]).
                        Lembre-se: sua doação é importante para ajudar as vítimas das enchentes no Rio Grande do Sul. Seja cauteloso e tome as medidas necessárias para garantir que seus recursos cheguem ao destino correto.

                        Juntos, podemos combater a fraude e garantir que a solidariedade chegue a quem realmente precisa!"""]

    embeddings_banco_de_dados = embedder.encode(banco_de_dados, convert_to_tensor=True)
    
    # Gerar embedding da pergunta
    embedding_pergunta = embedder.encode(message, convert_to_tensor=True)

    # Encontrar o documento mais similar
    similaridades = util.pytorch_cos_sim(embedding_pergunta, embeddings_banco_de_dados)[0]
    indice_documento_similar = torch.argmax(similaridades).item()
    documento_relevante = banco_de_dados[indice_documento_similar]

    # Construir prompt com o documento relevante como contexto
    prompt = f"Contexto: {documento_relevante}\n\nPergunta do usuário: {message}"
    response = chat.send_message(prompt)
    response_formatada = converter_negrito(response.text)

    if '*' in response_formatada:
        response_formatada = substituir_asteriscos_por_br(response_formatada)

    print(response.text)
    return response_formatada

        
def converter_negrito(texto):
    partes = texto.split("**")
    
    # Concatenar as partes com as tags HTML de negrito
    mensagem_formatada = ""
    for i, parte in enumerate(partes):
        if i % 2 == 0:
            mensagem_formatada += parte
        else:
            mensagem_formatada += f"<strong>{parte}</strong>"
    
    return mensagem_formatada

def substituir_asteriscos_por_br(texto):
    return texto.replace('*', '<br>')

#Código para rodar o chat no terminal:
    #    while True:
    #   texto = input("Escreva sua mensagem (ou 'sair'): ")
    #    if texto.lower() == "sair":
    #        break
    #   # Gerar embedding da pergunta
    #   embedding_pergunta = embedder.encode(texto, convert_to_tensor=True)

        # Encontrar o documento mais similar
    #    similaridades = util.pytorch_cos_sim(embedding_pergunta, embeddings_banco_de_dados)[0]
    #    indice_documento_similar = torch.argmax(similaridades).item()
    #    documento_relevante = banco_de_dados[indice_documento_similar]
    #    # Construir prompt com o documento relevante como contexto
    #    prompt = f"Contexto: {documento_relevante}\n\nPergunta do usuário: {message}"
    #    response = chat.send_message(prompt)

    #   print(response.text, "\n")

    # print("Encerrando Chat")]