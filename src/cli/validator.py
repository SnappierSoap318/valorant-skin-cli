from prompt_toolkit.validation import ValidationError, Validator
from .completer_generator import Completer

commands = Completer.generate_completer_dict()

class Command_Validator(Validator):
    def validate(self, document):
        command = document.text.split()[0].strip()
        args = document.text.split()[1:]
        if not command in list(commands.keys()):
            # validator for regular commands
            raise ValidationError(
                message="Invalid command",
                cursor_position=len(document.text)
            )
        else:
            # validator overrides for more complex commands
            if command == "set":
                completer_data = commands["set"]
                if len(args) < 2:
                    raise ValidationError(
                        message="Missing required arguments",
                        cursor_position=len(document.text)
                    )
                valid = False

                next_data = completer_data
                for index in range(0,len(args)):
                    if args[index] in next_data.keys():
                        next_data = next_data[args[index]]
                        valid = True 
                    else:
                        valid = False
                if valid:
                    return True

                
                raise ValidationError(
                    message="Syntax error, ensure you entered a valid weapon/skin",
                    cursor_position=len(document.text)
                )
