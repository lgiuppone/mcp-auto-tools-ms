# 🧠 MCP Server Helm Chart

This Helm chart dynamically deploys an [MCP (Model Context Protocol)](https://github.com/mem-brain-labs/mcp) server, accessible remotely via **Server-Sent Events (SSE)**. It allows you to **easily expose any existing REST API** from your application as tools within the MCP environment, enabling intelligent agents or external clients to query and use them.

---

## 🚀 Features

- Deploy an MCP server in a Kubernetes cluster
- Enable remote interaction via SSE
- Dynamically register and expose API endpoints as `tools`
- Lightweight configuration via `values.yaml`
- Compatible with FastAPI, Express, Flask, and any REST service

---

## 📦 Chart Structure

```text
mcp-server/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingressroute.yaml
    └── configmap.yaml
```

---

## ⚙️ Dynamic Configuration

You can define which APIs to expose directly in your `values.yaml` file using the `config.tools` section. Here's an example configuration:

```yaml

config:
  tools: |
    tools:
      get_api_status:
        endpoint: https://api-users.dev.example.com/
        description: Get root message to verify the API is running.

      fetch_user_by_id:
        endpoint: https://api-users.dev.example.com/users/1
        description: Fetch a specific user by ID from the API.

      get_random_user:
        endpoint: https://api-users.dev.example.com/users/random
        description: Retrieve a randomly selected user (for testing/demo).
```

> 🔒 Make sure to replace `*.dev.example.com` with your actual domains.

---

## 🧪 Install the Chart

```bash
helm install mcp-server ./mcp-server \
  --values values.yaml
```

---

## 🔌 MCP Client Configuration

Once deployed, clients can connect to your MCP server using the following configuration:

```json
{
  "mcp": {
    "servers": {
      "users-api": {
        "url": "https://mcp-server.dev.example.com/sse"
      }
    }
  }
}
```

> 🔁 The MCP server uses SSE (`/sse`) to stream messages in real-time.

---

## 🧹 Uninstall

```bash
helm uninstall mcp-server
```

---

## 🧠 About MCP

MCP (Model Context Protocol) is a lightweight interaction layer that enables intelligent agents or applications to access domain-specific tools using natural language interfaces or direct API querying.

---

## 📬 Questions / Contributions

Feel free to open an issue or submit a pull request. Contributions are welcome!
