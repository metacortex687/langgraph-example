# LangGraph Cloud Example

![](static/agent_ui.png)

This is an example agent to deploy with LangGraph Cloud.

> [!TIP]
> If you would rather use `pyproject.toml` for managing dependencies in your LangGraph Cloud project, please check out [this repository](https://github.com/langchain-ai/langgraph-example-pyproject).

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications with LLMs. The main use cases for LangGraph are conversational agents, and long-running, multi-step LLM applications or any LLM application that would benefit from built-in support for persistent checkpoints, cycles and human-in-the-loop interactions (ie. LLM and human collaboration).

LangGraph shortens the time-to-market for developers using LangGraph, with a one-liner command to start a production-ready HTTP microservice for your LangGraph applications, with built-in persistence. This lets you focus on the logic of your LangGraph graph, and leave the scaling and API design to us. The API is inspired by the OpenAI assistants API, and is designed to fit in alongside your existing services.

In order to deploy this agent to LangGraph Cloud you will want to first fork this repo. After that, you can follow the instructions [here](https://langchain-ai.github.io/langgraph/cloud/) to deploy to LangGraph Cloud.

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/metacortex687/langgraph-example.git
cd langgraph-example
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file and add your API keys:
- `TAVILY_API_KEY`
- `XAI_API_KEY`

### Running the Application

1. Start the development server:
```bash
langgraph dev
```

2. Open the LangSmith interface in your browser:
```
https://smith.langchain.com/studio/thread?baseUrl=http%3A%2F%2F127.0.0.1%3A2024
```

The application will be available at `http://127.0.0.1:2024`.

---

# Пример LangGraph Cloud

![](static/agent_ui.png)

Это пример агента для развертывания в LangGraph Cloud.

> [!СОВЕТ]
> Если вы предпочитаете использовать `pyproject.toml` для управления зависимостями в вашем проекте LangGraph Cloud, ознакомьтесь с [этим репозиторием](https://github.com/langchain-ai/langgraph-example-pyproject).

[LangGraph](https://github.com/langchain-ai/langgraph) - это библиотека для создания приложений с сохранением состояния и множеством участников, использующих языковые модели (LLM). Основные случаи использования LangGraph включают разговорных агентов и многошаговые LLM-приложения, или любые LLM-приложения, которым необходима встроенная поддержка постоянных контрольных точек, циклов и взаимодействия с человеком (т.е. совместная работа LLM и человека).

LangGraph сокращает время выхода на рынок для разработчиков, предоставляя однострочную команду для запуска готового к производству HTTP-микросервиса для ваших приложений LangGraph со встроенным сохранением состояния. Это позволяет вам сосредоточиться на логике вашего графа LangGraph и оставить масштабирование и дизайн API нам. API вдохновлен OpenAI assistants API и разработан так, чтобы органично встраиваться в ваши существующие сервисы.

Чтобы развернуть этого агента в LangGraph Cloud, вам нужно сначала сделать форк этого репозитория. После этого вы можете следовать инструкциям [здесь](https://langchain-ai.github.io/langgraph/cloud/) для развертывания в LangGraph Cloud.

## Локальная Разработка

### Предварительные требования
- Python 3.8 или выше
- Git

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/metacortex687/langgraph-example.git
cd langgraph-example
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate  # Для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
cp .env.example .env
```
Отредактируйте файл `.env` и добавьте ваши API ключи:
- `TAVILY_API_KEY`
- `XAI_API_KEY`

### Запуск приложения

1. Запустите сервер разработки:
```bash
langgraph dev
```

2. Откройте интерфейс LangSmith в браузере:
```
https://smith.langchain.com/studio/thread?baseUrl=http%3A%2F%2F127.0.0.1%3A2024
```

Приложение будет доступно по адресу `http://127.0.0.1:2024`.
