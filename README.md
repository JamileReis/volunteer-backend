# Volunteer Management Backend

Backend da plataforma de gerenciamento de voluntários desenvolvido com FastAPI, utilizando arquitetura modular e foco em escalabilidade, desacoplamento e manutenção.

## Sobre o Projeto

O sistema foi criado para gerenciar:
- voluntários
- eventos
- autenticação de usuários
- cadastro e gerenciamento de atividades
- controle de participação
- APIs REST para integração com frontend React

A aplicação segue princípios de:
- Clean Architecture
- SOLID
- DRY
- KISS

---

# Arquitetura

## Clean Architecture

A arquitetura foi escolhida para garantir:
- separação de responsabilidades
- baixo acoplamento
- facilidade de manutenção
- escalabilidade
- facilidade para testes
- evolução para microsserviços futuramente

Estrutura baseada em camadas:

```bash
app/
├── main.py
├── routes/
├── schemas/
├── services/
├── models/
├── repositories/
├── core/
└── database/
