import abc
from langchain_openrouter import ChatOpenRouter
from app.services.retry import llm_retry


class ModelProvider(abc.ABC):
    def __init__(self, api_key: str, model_name: str):
        self.api_key = api_key
        self.model_name = model_name

    @abc.abstractmethod
    async def ainvoke(self, messages: list, tools=None, schema=None):
        raise NotImplementedError


class LangchainOpenRouter(ModelProvider):

    def __init__(self, api_key: str, model_name: str):
        super().__init__(api_key, model_name)
        self._llm = ChatOpenRouter(model= model_name, api_key=api_key, max_retries=3)

    @llm_retry
    async def ainvoke(self, messages: list, tools=None, schema=None):
        return await self._call_llm(self._llm, messages, tools, schema)

    async def _call_llm(self, llm, messages: list, tools=None, schema=None):
        if tools:
            llm = llm.bind_tools(tools)
        if schema:
            llm = llm.with_structured_output(schema)
        return await llm.ainvoke(messages)
    
