# NagaAI

Use chat models from many vendors in Dify through [NagaAI](https://naga.ac) with one API key.

NagaAI's primary API is the OpenAI Responses API at `https://api.naga.ac/v1`; it also serves Chat Completions. Dify's plugin SDK talks to OpenAI-compatible providers through Chat Completions only (`OAICompatLargeLanguageModel`), so this plugin uses Chat Completions. It points Dify at NagaAI, so you do not have to set up a generic OpenAI-compatible provider and enter each model's context size and tool support by hand.

## Setup

1. Create an account at [naga.ac](https://naga.ac) and create an API key on the [API keys](https://naga.ac/dashboard/api-keys) page.
2. Add credits on the [Credits](https://naga.ac/dashboard/credits) page.
3. In Dify, install **NagaAI** from the Marketplace.
4. Open **Settings → Model Provider → NagaAI**, paste the API key and save. Dify checks the key with a request to the model list, which is not billed.

## Usage

The models below appear in every LLM model picker: LLM nodes, chatflows and agents. Each supports tool calling (including streamed tool calls), image input, structured output (JSON Schema) and a *Reasoning effort* setting from `none` to `max`; NagaAI runs the nearest level the model supports.

| Model | Context (tokens) | Max output (tokens) |
|---|---|---|
| `anthropic/claude-opus-5.5` | 1,000,000 | 128,000 |
| `anthropic/claude-sonnet-5.5` | 1,000,000 | 128,000 |
| `openai/gpt-6.1-sol` | 1,050,000 | 128,000 |
| `deepseek/deepseek-v4.1-flash` | 1,048,576 | 32,768 |

**Other models:** choose **Add Model**, enter the id exactly as [`GET https://api.naga.ac/v1/models`](https://api.naga.ac/v1/models) lists it, and set its context size, tool calling and vision options from the same list. The list needs no key.

Prices are on [naga.ac/models](https://naga.ac/models) and in the same model list.

## Credentials

One NagaAI API key. Dify stores it as an encrypted credential and the plugin sends it only in the `Authorization` header to `api.naga.ac`.

## Connection requirements

Your Dify instance needs outbound HTTPS access to `api.naga.ac` (port 443). The plugin calls no other host.

## Source and support

- Source repository: https://github.com/naga-ai-hub/dify-plugin-nagaai
- Issues: https://github.com/naga-ai-hub/dify-plugin-nagaai/issues
- Documentation: https://docs.naga.ac
- Contact: support@naga.ac
- Privacy: [PRIVACY.md](PRIVACY.md)
