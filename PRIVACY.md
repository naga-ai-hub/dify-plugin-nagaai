# Privacy Policy

This plugin connects Dify to the NagaAI API (`https://api.naga.ac/v1`).

## What the plugin sends

When a Dify app uses a NagaAI model, the plugin sends the request content to NagaAI so the model can answer: prompts, conversation messages, tool definitions and tool results, images attached for a vision model, and the model parameters. It authenticates with the NagaAI API key you enter in Dify.

## What the plugin stores

The plugin itself stores nothing: no logs, analytics or copies of your content. Dify stores your API key as an encrypted credential, as it does for every model provider.

## How NagaAI handles the data

- NagaAI forwards each request to a model provider that serves the model.
- For paid models, request content is used to answer the request and is not used for training, unless you enable training for paid models on the Privacy page of your NagaAI dashboard. All models predefined in this plugin are paid models.
- For free models, request content may be used by NagaAI and its partners for training.
- Cloudflare receives every request to NagaAI to deliver it and protect the service. Operational and security logs that contain IP addresses are kept for up to 30 days.

The full policy is at https://naga.ac/legal/privacy.

## Contact

Questions about this plugin or about data handling: support@naga.ac
