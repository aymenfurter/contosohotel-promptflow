# Chat Flow - Azure OpenAI and Dynamic SQL Synthesis

This demo showcases how to use **Azure OpenAI** for dynamic SQL query generation and natural language interactions with your data. It dynamically determines whether a user's input can be answered using an SQL query or requires an unstructured response. Based on this, the system either returns an SQL query or interacts with the data to provide a contextual answer, following the approach described in [Azure OpenAI - Use your data](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart).

## Setting Up Azure OpenAI Connection

To use this flow, you need to create an **Azure OpenAI** connection.

1. Create an Azure OpenAI service. Refer to the [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/) for details.
2. Create the connection using the command below:

```bash
# Azure OpenAI connection
pf connection create --file azure_openai.yaml --set api_key=<your_api_key> api_base=<your_api_base> --name open_ai_connection
```

3. In your `flow.dag.yaml`, reference the connection named `open_ai_connection`.

```bash
# Show registered connection
pf connection show --name open_ai_connection
```

For more information, refer to the official [Promptflow documentation](https://promptflow.azurewebsites.net/community/local/manage-connections.html).

## How It Works

This demo uses Azure OpenAI to:

- **Intent Detection**: It first determines if the user's question can be answered using SQL or requires an unstructured response.
- **Dynamic SQL Synthesis**: If the question can be answered with SQL, the system synthesizes the appropriate SQL query based on the user's input.
- **Chat on Your Data**: If the question requires unstructured data, Azure OpenAI interacts with the user's data (e.g., documents) via a data source to provide a contextual answer.

SQL queries are **not executed directly**. They are returned for potential execution, depending on the flow's requirements.

### Running an Interactive Chat Flow

You can start an interactive chat session for this flow with the following command:

```bash
pf flow test --flow <flow_folder> --interactive
```

During the session, the system will dynamically determine if the input should trigger SQL generation or chat-based data interaction.

### Sample Conversation

Here’s an example of a conversation demonstrating how the chat flow works:

```plaintext
================================
User: tell me about Basel
Bot: Basel is a city located in the northwestern part of Switzerland, situated on both sides of the Rhine River. It is one of the few areas in Switzerland that lies to the right of the High Rhine, along with parts of the canton of Zurich and the canton of Schaffhausen [doc5]...

================================
User: give me a list of all hotels
Bot: 
SELECT *
FROM hotels;
```