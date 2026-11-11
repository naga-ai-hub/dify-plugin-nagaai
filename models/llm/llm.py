from collections.abc import Generator

from dify_plugin import OAICompatLargeLanguageModel
from dify_plugin.entities.model import AIModelEntity, ModelFeature
from dify_plugin.entities.model.llm import LLMResult
from dify_plugin.entities.model.message import PromptMessage, PromptMessageTool

ENDPOINT_URL = "https://api.naga.ac/v1"


def _prepare_credentials(credentials: dict) -> None:
    credentials["endpoint_url"] = ENDPOINT_URL
    credentials["mode"] = "chat"


class NagaAILargeLanguageModel(OAICompatLargeLanguageModel):
    def _invoke(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: list[PromptMessageTool] | None = None,
        stop: list[str] | None = None,
        stream: bool = True,
        user: str | None = None,
    ) -> LLMResult | Generator:
        _prepare_credentials(credentials)
        # The base class sends `tools` only when function_calling_type is "tool_call".
        # Customizable models set it in their credential form; predefined models
        # declare tool support in their YAML features.
        if "function_calling_type" not in credentials:
            schema = self.get_model_schema(model, credentials)
            if schema and ModelFeature.MULTI_TOOL_CALL in (schema.features or []):
                credentials["function_calling_type"] = "tool_call"
        # NagaAI reports usage in a stream only when asked to.
        if stream:
            model_parameters = {**model_parameters, "stream_options": {"include_usage": True}}
        return super()._invoke(model, credentials, prompt_messages, model_parameters, tools, stop, stream, user)

    def _wrap_thinking_by_reasoning_content(self, delta: dict, is_reasoning: bool) -> tuple[str, bool]:
        # NagaAI streams reasoning as `reasoning_content` and repeats it in
        # `reasoning_details`, sometimes in a chunk of its own. Such a chunk has no
        # answer text, so it continues the reasoning block instead of closing it.
        if (
            is_reasoning
            and delta.get("reasoning_details")
            and not (delta.get("content") or delta.get("reasoning_content") or delta.get("tool_calls"))
        ):
            return "", True
        return super()._wrap_thinking_by_reasoning_content(delta, is_reasoning)

    def validate_credentials(self, model: str, credentials: dict) -> None:
        _prepare_credentials(credentials)
        super().validate_credentials(model, credentials)

    def get_customizable_model_schema(self, model: str, credentials: dict) -> AIModelEntity:
        _prepare_credentials(credentials)
        return super().get_customizable_model_schema(model, credentials)
