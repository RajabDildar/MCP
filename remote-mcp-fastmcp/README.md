### Verify server
``` 
fastmcp inspect main.py
``` 

## Run normally
``` 
fastmcp run main.py
``` 

## Start Inspector -> connect with inspector, test the tools
``` 
fastmcp dev inspector main.py
``` 

## Run HTTP server
``` 
fastmcp run main.py --transport http
``` 

## Show version
``` 
fastmcp version
``` 

## To print the exact command an MCP host should use to start your server over STDIO.
``` 
fastmcp install stdio main.py
```
## sample integration json file
```
{
  "servers": {
    "demo": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "main.py"
      ]
    }
  }
} 
```

- deployment is straightforward. connect github with fastmcp cloud and deploy. get the url and add custom connector remote.
