# Escritorio Advocacia API

Uma API RESTful desenvolvida em Django REST Framework para gerenciar advogados, clientes, processos e agendas de um escritório de advocacia.

---

## 📋 Funcionalidades

- **Gerenciamento de Advogados**:
  - CRUD completo para advogados.
  - Endpoint para listar advogados com mais clientes.

- **Gerenciamento de Clientes**:
  - CRUD completo para clientes.
  - Filtro por faixa de idade.

- **Gerenciamento de Processos**:
  - CRUD completo para processos.
  - Busca de processos por número.
  - Atualização de status de processos (Aberto, Em andamento, Finalizado).

- **Gerenciamento de Agendas**:
  - CRUD completo para compromissos na agenda.
  - Filtro para compromissos de advogados em uma data específica.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - Django 4.1
  - Django REST Framework

- **Banco de Dados**:
  - SQLite (pode ser substituído por PostgreSQL ou outro)

- **Gerenciamento de Ambiente**:
  - Python-dotenv para variáveis de ambiente.

---

## 📂 Estrutura do Projeto


```plaintext
escritorio-advocacia-api/
├── escritorio/              # App principal
│   ├── models.py            # Modelos de dados (Advogado, Cliente, Processo, Agenda)
│   ├── views.py             # Lógica dos endpoints
│   ├── serializers.py       # Serializadores dos modelos
│   └── admin.py             # Configurações do Django Admin
├── setup/                   # Configurações do projeto Django
│   ├── settings.py          # Configurações gerais
│   ├── urls.py              # Rotas principais
│   └── wsgi.py              # Configuração WSGI
└── manage.py                # Script de gerenciamento Django
```

---

## 🔗 Endpoints

### **Advogados**
- `GET /advogados/`: Lista todos os advogados.
- `GET /advogados/populares/`: Lista advogados ordenados pelo número de clientes.
- `POST /advogados/`: Cria um advogado.
- `PATCH /advogados/{id}/`: Atualiza um advogado.
- `DELETE /advogados/{id}/`: Remove um advogado.

### **Clientes**
- `GET /clientes/`: Lista todos os clientes.
- `GET /clientes/idade/<idade_min>/<idade_max>/`: Lista clientes em uma faixa de idade.
- `POST /clientes/`: Cria um cliente.
- `PATCH /clientes/{id}/`: Atualiza um cliente.
- `DELETE /clientes/{id}/`: Remove um cliente.

### **Processos**
- `GET /processos/`: Lista todos os processos.
- `GET /processos/numero/<numero>/`: Busca um processo pelo número.
- `PATCH /processos/{id}/atualizar_status/`: Atualiza o status de um processo.
- `POST /processos/`: Cria um processo.
- `DELETE /processos/{id}/`: Remove um processo.

### **Agenda**
- `GET /agenda/`: Lista todos os compromissos.
- `GET /agenda/advogado/<advogado_id>/data/<data>/`: Lista compromissos de um advogado em uma data específica.
- `POST /agenda/`: Cria um compromisso.
- `PATCH /agenda/{id}/`: Atualiza um compromisso.
- `DELETE /agenda/{id}/`: Remove um compromisso.
