from openai import AsyncOpenAI


class Agent:
    def __init__(self, name, instructions=None, tools=None, handoffs=None):
        self.name = name
        self.instructions = instructions
        self.tools = tools or []
        self.handoffs = handoffs or []

    def run(self):
        print(f"Agent '{self.name}' is running.")
        if self.instructions:
            print(f"  Instructions: {self.instructions}")
        if self.tools:
            print(f"  Tools: {self.tools}")
        if self.handoffs:
            print(f"  Handoffs: {self.handoffs}")


class RunResult:
    def __init__(self, last_agent=None, final_output=None):
        self.last_agent = last_agent
        self.final_output = final_output


class Runner:
    def __init__(self, agent):
        self.agent = agent

    def start(self):
        print("Runner starting agent...")
        self.agent.run()

    @classmethod
    def run_sync(cls, starting_agent=None, input=None, run_config=None):
        print("Running agent synchronously...")

        if starting_agent:
            print(f"Starting agent: {starting_agent.name}")
            starting_agent.run()

        if input:
            print(f"Input: {input}")

        if run_config:
            print("RunConfig:")
            run_config.show()

        # simulate some final output
        final_output = f"Processed input: {input}" if input else "No input provided"
        return RunResult(last_agent=starting_agent, final_output=final_output)


class OpenAIChatCompletionsModel:
    def __init__(self, model="gpt-3.5-turbo", openai_client=None):
        self.model = model
        self.openai_client = openai_client

    def complete(self, prompt):
        if self.openai_client:
            print(f"[{self.model}] Completing via provided OpenAI client with prompt: {prompt}")
            # Example call:
            # return self.openai_client.chat.completions.create(...)
        else:
            print(f"[{self.model}] No OpenAI client provided; dummy completion for: {prompt}")
        return "This is a dummy completion."


class RunConfig:
    def __init__(self, model=None, model_provider=None, tracing_disabled=False, **kwargs):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled
        self.extra = kwargs

    def show(self):
        print(f"RunConfig:")
        print(f"  model: {self.model}")
        print(f"  model_provider: {self.model_provider}")
        print(f"  tracing_disabled: {self.tracing_disabled}")
        if self.extra:
            print(f"  extra: {self.extra}")


def handoff(agent, task=None, tool_name_override=None, tool_description_override=None):
    print(f"Handing off to agent '{agent.name}'")

    if task:
        print(f"  Task: {task}")

    if tool_name_override:
        print(f"  Tool Name Override: {tool_name_override}")

    if tool_description_override:
        print(f"  Tool Description Override: {tool_description_override}")

    print("Handoff complete.")


def function_tool(func):
    """Decorator to mark a function as a tool."""
    def wrapper(*args, **kwargs):
        print(f"Executing tool: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def enable_verbose_stdout_logging():
    print("Verbose stdout logging enabled.")
