from pathlib import Path
import os


class MCPServer:
    def __init__(self, base_docs: Path):
        self.base_docs = base_docs
        self.enabled = False
        try:
            # try to import fastmcp (if installed)
            import fastmcp
            self.fastmcp = fastmcp
            self.enabled = True
        except Exception:
            self.fastmcp = None
            self.enabled = False

    def start(self):
        if not self.enabled:
            print("fastmcp not installed — running in HTTP-only mock mode")
            return
        # Example of registering a tool with fastmcp — concrete API depends on fastmcp
        # This is a suggested pattern; install fastmcp and adjust as per its docs.
        try:
            server = self.fastmcp.Server(tool_name="runtribe-docs")
            # register a simple read tool
            @server.register("read_doc")
            def read_doc(params):
                name = params.get("name")
                p = (self.base_docs / name)
                if not p.exists():
                    return {"error": "not found"}
                return {"content": p.read_text(encoding="utf-8")}

            server.start()
        except Exception as e:
            print("fastmcp start failed:", e)

    # helper local methods
    def list_docs(self):
        return [p.name for p in self.base_docs.glob("**/*") if p.is_file()]
