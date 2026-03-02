import re
from typing import Dict, List, Tuple

class BotEnglishChatbot:
    def __init__(self):
        self.knowledge_base = {
            "dados_corporativos": {
                "razao_social": "BotEnglish Soluções Educacionais Ltda. (fictícia)",
                "nome_fantasia": "BotEnglish",
                "cnpj": "25.987.654/0001-32",
                "fundacao": "10 de maio de 2023",
                "sede": "Avenida Paulista, 1500, Conjunto 801 - Bela Vista, São Paulo/SP - CEP 01310-100",
                "unidade_presencial": "Rua Oscar Freire, 1200 - Jardins, São Paulo/SP"
            },
            "contatos": {
                "telefone": "(11) 3333-4444",
                "whatsapp": "(11) 99111-2222",
                "email_geral": "contato@botenglish.com.br",
                "suporte": "suporte@botenglish.com.br",
                "comercial": "matriculas@botenglish.com.br",
                "site": "www.botenglish.com.br",
                "linkedin": "/company/botenglish",
                "instagram": "@botenglish",
                "tiktok": "@botenglish_oficial",
                "youtube": "BotEnglish Official"
            },
            "proposta_valor": {
                "slogan": "BotEnglish: Fluência em Inglês Acelerada pela Inteligência Artificial.",
                "slogan_curto": "O seu inglês, reinventado pela IA.",
                "missao": "Democratizar o aprendizado de inglês, tornando-o mais eficiente, acessível e personalizado através do uso inovador da inteligência artificial.",
                "visao": "Ser a plataforma líder global em ensino de inglês, reconhecida pela eficácia de sua metodologia adaptativa e pela fluência comprovada de seus alunos.",
                "valores": ["Inovação no Ensino", "Personalização", "Eficiência e Resultados", "Acessibilidade", "Comunidade e Interação"]
            },
            "equipe": {
                "ceo": {
                    "nome": "Dra. Ana Paula Costa",
                    "cargo": "CEO & Co-fundadora",
                    "formacao": "Doutora em Linguística Aplicada (USP)",
                    "experiencia": "Ex-diretora de inovação pedagógica na Cengage Learning"
                },
                "cto": {
                    "nome": "Eng. Gabriel Medeiros",
                    "cargo": "CTO & Co-fundador",
                    "formacao": "Engenheiro de Software (ITA)",
                    "experiencia": "Ex-arquiteto de soluções na IBM Watson"
                },
                "diretora_marketing": {
                    "nome": "Juliana Pereira de Lima",
                    "cargo": "Diretora de Marketing",
                    "formacao": "Mestre em Marketing Digital (ESPM)",
                    "experiencia": "Ex-gerente de marketing na Duolingo Brasil"
                }
            },
            "planos": {
                "basic": {
                    "preco_mensal": "R$ 59",
                    "beneficios": "Acesso ilimitado ao AI Tutor, exercícios interativos, relatórios de progresso semanais"
                },
                "premium": {
                    "preco_mensal": "R$ 99",
                    "preco_anual": "R$ 999",
                    "beneficios": "Tudo do Basic + biblioteca de conteúdo dinâmica, simulados de exames, 2 créditos de aula em grupo por mês"
                },
                "vip": {
                    "preco_mensal": "R$ 199",
                    "beneficios": "Tudo do Premium + 4 créditos de aula em grupo por mês + 1 aula particular por mês"
                }
            },
            "aulas_adicionais": {
                "pacote_4_aulas": "R$ 180",
                "pacote_10_aulas": "R$ 400",
                "aula_particular": "R$ 120 (50 min)"
            },
            "dados_financeiros": {
                "faturamento_previsto_2026": "R$ 3,5 milhões",
                "alunos_ativos": "4.500",
                "colaboradores": "25",
                "investimento_captado": "R$ 2,5 milhões (Rodada Anjo - 2023)",
                "mercado_alvo": "Jovens adultos (18-35 anos), profissionais, estudantes universitários",
                "potencial_mercado": "15 milhões de brasileiros"
            },
            "tecnologia": {
                "frontend": "React",
                "backend": "Python",
                "ia_ml": "Modelos de PLN (Processamento de Linguagem Natural)",
                "cloud": "AWS (Amazon Web Services)"
            }
        }
        
        self.patterns = self._create_patterns()
    
    def _create_patterns(self) -> List[Tuple[str, str]]:
        """Define padrões de perguntas e suas respostas"""
        return [
            (r"(qual|quais).*(contato|telefone|email|whatsapp)", "contatos"),
            (r"(qual|onde).*(endereço|sede|localiza|fica)", "endereco"),
            (r"(qual|quais).*(plano|planos|preço|preços|valor|valores|custo)", "planos"),
            (r"(missão|missao|proposito|propósito)", "missao"),
            (r"(visão|visao|futuro)", "visao"),
            (r"(valores|principios|princípios)", "valores"),
            (r"(slogan|frase)", "slogan"),
            (r"(equipe|fundador|fundadores|ceo|cto|diretor)", "equipe"),
            (r"(cnpj|razão social|razao social)", "dados_corporativos"),
            (r"(faturamento|receita|financeiro|investimento|alunos)", "dados_financeiros"),
            (r"(tecnologia|plataforma|ia|inteligencia artificial)", "tecnologia"),
            (r"(diferencial|destaque|vantagem)", "diferenciais"),
            (r"(aula|professor|nativo)", "aulas"),
            (r"(empresa|b2b|corporativo)", "b2b"),
        ]
    
    def _responder_contatos(self) -> str:
        c = self.knowledge_base["contatos"]
        return f"""📞 **Contatos da BotEnglish:**

• Telefone: {c['telefone']}
• WhatsApp: {c['whatsapp']}
• E-mail geral: {c['email_geral']}
• Suporte técnico: {c['suporte']}
• Comercial: {c['comercial']}
• Site: {c['site']}

**Redes Sociais:**
• LinkedIn: {c['linkedin']}
• Instagram: {c['instagram']}
• TikTok: {c['tiktok']}
• YouTube: {c['youtube']}"""
    
    def _responder_endereco(self) -> str:
        d = self.knowledge_base["dados_corporativos"]
        return f"""📍 **Localização da BotEnglish:**

**Sede:** {d['sede']}

**Unidade Presencial (aulas híbridas/premium):**
{d['unidade_presencial']}"""
    
    def _responder_planos(self) -> str:
        p = self.knowledge_base["planos"]
        a = self.knowledge_base["aulas_adicionais"]
        return f"""💳 **Planos BotEnglish:**

**Plano Basic:** {p['basic']['preco_mensal']}/mês
{p['basic']['beneficios']}

**Plano Premium:** {p['premium']['preco_mensal']}/mês ou {p['premium']['preco_anual']}/ano
{p['premium']['beneficios']}

**Plano VIP:** {p['vip']['preco_mensal']}/mês
{p['vip']['beneficios']}

**Créditos Adicionais:**
• Pacote 4 aulas em grupo: {a['pacote_4_aulas']}
• Pacote 10 aulas em grupo: {a['pacote_10_aulas']}
• Aula particular: {a['aula_particular']}"""
    
    def _responder_missao(self) -> str:
        return f"🎯 **Missão:** {self.knowledge_base['proposta_valor']['missao']}"
    
    def _responder_visao(self) -> str:
        return f"🚀 **Visão:** {self.knowledge_base['proposta_valor']['visao']}"
    
    def _responder_valores(self) -> str:
        valores = "\n• ".join(self.knowledge_base['proposta_valor']['valores'])
        return f"⭐ **Valores da BotEnglish:**\n• {valores}"
    
    def _responder_slogan(self) -> str:
        p = self.knowledge_base["proposta_valor"]
        return f"""💬 **Slogans da BotEnglish:**

**Principal:** {p['slogan']}

**Curto:** {p['slogan_curto']}"""
    
    def _responder_equipe(self) -> str:
        e = self.knowledge_base["equipe"]
        return f"""👥 **Equipe Executiva:**

**{e['ceo']['cargo']}**
{e['ceo']['nome']}
• {e['ceo']['formacao']}
• Especialista em EdTech e gamificação
• {e['ceo']['experiencia']}

**{e['cto']['cargo']}**
{e['cto']['nome']}
• {e['cto']['formacao']}
• Especialista em IA conversacional e Machine Learning
• {e['cto']['experiencia']}

**{e['diretora_marketing']['cargo']}**
{e['diretora_marketing']['nome']}
• {e['diretora_marketing']['formacao']}
• {e['diretora_marketing']['experiencia']}"""
    
    def _responder_dados_corporativos(self) -> str:
        d = self.knowledge_base["dados_corporativos"]
        return f"""🏢 **Dados Corporativos:**

• Razão Social: {d['razao_social']}
• Nome Fantasia: {d['nome_fantasia']}
• CNPJ: {d['cnpj']}
• Fundação: {d['fundacao']}
• Sede: {d['sede']}"""
    
    def _responder_dados_financeiros(self) -> str:
        d = self.knowledge_base["dados_financeiros"]
        return f"""💰 **Dados Financeiros e Mercado:**

• Faturamento Previsto (2026): {d['faturamento_previsto_2026']}
• Alunos Ativos: {d['alunos_ativos']}
• Colaboradores: {d['colaboradores']}
• Investimento Captado: {d['investimento_captado']}
• Mercado-Alvo: {d['mercado_alvo']}
• Potencial de Mercado: {d['potencial_mercado']}"""
    
    def _responder_tecnologia(self) -> str:
        t = self.knowledge_base["tecnologia"]
        return f"""🤖 **Tecnologia e Infraestrutura:**

• Frontend: {t['frontend']}
• Backend: {t['backend']}
• IA/ML: {t['ia_ml']} para conversação, reconhecimento de fala e análise de texto
• Cloud: {t['cloud']} para escalabilidade e segurança
• Parceria com universidades para P&D em novas funcionalidades"""
    
    def _responder_diferenciais(self) -> str:
        return """✨ **Diferenciais da BotEnglish:**

**AI Tutor Personalizado:** Bot de conversação avançado que simula interações humanas, corrige pronúncia e gramática em tempo real

**Percursos Adaptativos:** A IA analisa o desempenho e sugere aulas específicas para suas dificuldades

**Análise de Fluência por IA:** Avaliação contínua da fala, escrita e compreensão com relatórios detalhados

**Biblioteca de Conteúdo Dinâmica:** Artigos, vídeos, podcasts e simulados de exames (TOEFL, IELTS, Cambridge) adaptados ao seu nível"""
    
    def _responder_aulas(self) -> str:
        return """👨‍🏫 **Aulas com Professores Nativos:**

**Grupos Pequenos Online:** Aulas virtuais com professores nativos, focadas em conversação e debates

**Aulas Particulares:** Online ou presenciais, com foco em necessidades específicas (preparação para entrevistas, viagens, exames)

Disponíveis como complemento aos planos ou por pacotes de créditos!"""
    
    def _responder_b2b(self) -> str:
        return """🏢 **BotEnglish for Business (B2B):**

Soluções personalizadas para empresas que buscam capacitar seus colaboradores

**Formato:**
• Plataforma customizada
• Relatórios de progresso para RH
• Aulas em grupo exclusivas para a empresa

**Modelo:** Contratos anuais com valor por aluno/licença

Entre em contato: matriculas@botenglish.com.br"""
    
    def processar_pergunta(self, pergunta: str) -> str:
        """Processa a pergunta e retorna a resposta apropriada"""
        pergunta_lower = pergunta.lower()
        
        # Verifica padrões
        for pattern, tipo in self.patterns:
            if re.search(pattern, pergunta_lower):
                metodo = f"_responder_{tipo}"
                if hasattr(self, metodo):
                    return getattr(self, metodo)()
        
        # Resposta padrão
        return """Desculpe, não encontrei informações específicas sobre isso. 

Posso ajudar com:
• Contatos e localização
• Planos e preços
• Missão, visão e valores
• Equipe executiva
• Dados financeiros
• Tecnologia utilizada
• Diferenciais da plataforma
• Informações sobre aulas

Digite sua pergunta ou 'sair' para encerrar."""
    
    def saudacao(self) -> str:
        """Mensagem de boas-vindas"""
        return """🤖 Olá! Sou o assistente virtual da BotEnglish!

BotEnglish: Fluência em Inglês Acelerada pela Inteligência Artificial.

Como posso ajudar você hoje? Pergunte sobre:
• Planos e preços
• Contatos
• Nossa equipe
• Tecnologia e diferenciais
• Informações corporativas

Digite 'sair' para encerrar."""
    
    def iniciar(self):
        """Inicia o chatbot"""
        print(self.saudacao())
        print("\n" + "="*60 + "\n")
        
        while True:
            try:
                pergunta = input("Você: ").strip()
                
                if not pergunta:
                    continue
                
                if pergunta.lower() in ['sair', 'exit', 'quit', 'tchau', 'bye']:
                    print("\n🤖 Obrigado por conhecer a BotEnglish! Até logo! 👋")
                    print("Visite: www.botenglish.com.br")
                    break
                
                resposta = self.processar_pergunta(pergunta)
                print(f"\n🤖 BotEnglish:\n{resposta}\n")
                print("="*60 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Até logo! 👋")
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}\n")


if __name__ == "__main__":
    bot = BotEnglishChatbot()
    bot.iniciar()
