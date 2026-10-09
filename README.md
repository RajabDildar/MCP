# MCP - Model Context Protocol Learning Repository

This repository serves as a comprehensive learning resource and reference guide for understanding and implementing the **Model Context Protocol (MCP)**. It contains practical examples of local and remote MCP servers and clients built with FastMCP.

## 📚 About MCP

The Model Context Protocol (MCP) is a standardized protocol that enables large language models (LLMs) to interact with external tools, services, and data sources. This repository demonstrates how to build and integrate MCP servers and clients in Python.

## 📁 Project Structure

```
MCP/
├── local-mcp-fastmcp/          # Local MCP Server Implementation
│   └── Examples and code for running MCP servers locally
│       using the FastMCP framework
│
├── mcp-client/                  # MCP Client Implementation
│   └── Client code demonstrating how to connect to and
│       interact with MCP servers
│
└── remote-mcp-fastmcp/          # Remote MCP Server Implementation
    └── Examples for deploying and running MCP servers
        remotely with support for distributed access
```

## 🎯 Key Components

### 1. **local-mcp-fastmcp**
Contains examples and implementations of MCP servers that run locally on your machine. This is ideal for:
- Learning MCP fundamentals
- Local development and testing
- Single-machine deployments
- Quick prototyping

### 2. **mcp-client**
Implements MCP client code that demonstrates:
- Connecting to MCP servers
- Sending requests and handling responses
- Managing MCP protocol communication
- Client-side error handling and logging

### 3. **remote-mcp-fastmcp**
Covers remote MCP server setups with features for:
- Distributed MCP server deployments
- Remote access and communication
- Network-based server interactions
- Production-ready server implementations

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda for package management

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RajabDildar/MCP.git
   cd MCP
   ```

2. **Install dependencies:**
   Depending on which component you want to explore, install the required packages:
   ```bash
   # For FastMCP framework
   pip install fastmcp
   ```

### Usage

Explore each directory for specific examples:

- **Local Server**: Navigate to `local-mcp-fastmcp/` to see examples of running MCP servers locally
- **Client**: Check `mcp-client/` to understand how to build MCP clients
- **Remote Server**: Visit `remote-mcp-fastmcp/` for remote deployment examples

## 📖 How to Use This Repository

This repository is structured as a **learning reference**. Each directory contains:
- Working code examples
- Practical implementations
- Notes and comments for understanding MCP concepts

You can:
1. Study the code structure and patterns
2. Run the examples to see MCP in action
3. Adapt the code for your own MCP projects
4. Use it as a reference when working with MCP protocols

## 🔗 MCP Resources

For more information about the Model Context Protocol:
- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlopp/fastmcp)

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💡 Notes

This is a personal learning repository created while exploring MCP. The code serves as notes and reference material for MCP implementation patterns. Feel free to explore, learn, and adapt the examples for your own use cases.

---

**Happy Learning!** 🎓
