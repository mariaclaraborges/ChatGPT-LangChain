from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    """
    Print the arguments in a boxen style.
    """
    print(boxen(*args, **kwargs))


class ChatModelStartHandler(BaseCallbackHandler):
    """A callback handler that prints the start of a chat model run."""

    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("\n\n\n\n============ Sending Messages ============\n\n")

        for message in messages[0]:
            if message.type == "system":
                boxen_print(message.content, title=message.type, color="blue")
            elif message.type == "human":
                boxen_print(message.content, title=message.type, color="green")
            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(
                    f"Running tool {call['name']} with arguments {call['arguments']}",
                    title=message.type, 
                    color="yellow"
                )
            elif message.type == "ai":
                boxen_print(message.content, title=message.type, color="red")
            elif message.type == "function":
                boxen_print(
                    message.content, title=message.type, color="magenta"
                )
            else:
                boxen_print(
                    message.content, title=message.type, color="cyan"
                )