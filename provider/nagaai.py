import requests
from dify_plugin import ModelProvider
from dify_plugin.errors.model import CredentialsValidateFailedError

ENDPOINT_URL = "https://api.naga.ac/v1"


class NagaAIProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        # The model list answers 401 to a key NagaAI does not accept and costs
        # nothing, so the key is checked without a paid chat request.
        try:
            response = requests.get(
                f"{ENDPOINT_URL}/models",
                headers={"Authorization": f"Bearer {credentials['api_key']}"},
                timeout=(10, 60),
            )
        except requests.RequestException as e:
            raise CredentialsValidateFailedError(f"Could not reach NagaAI: {e}") from e
        if response.status_code != 200:
            raise CredentialsValidateFailedError(
                f"NagaAI rejected the key: {response.status_code} {response.text[:200]}"
            )
