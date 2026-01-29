"""Mock Copilot Client for demo purposes"""

class ResponseData:
    def __init__(self, content):
        self.content = content

class Response:
    def __init__(self, content):
        self.data = ResponseData(content)

class Session:
    def __init__(self, config):
        self.config = config
    
    async def send_and_wait(self, request):
        # Mock response for demo
        prompt = request.get("prompt", "")
        return Response(f"Response to: {prompt}\n\nThis is a mock response. 2 + 2 = 4")

class CopilotClient:
    def __init__(self):
        self.session = None
    
    async def start(self):
        print("Copilot client started (mock)")
    
    async def create_session(self, config):
        model = config.get("model", "default")
        print(f"Created session with model: {model}")
        return Session(config)
    
    async def stop(self):
        print("Copilot client stopped")
