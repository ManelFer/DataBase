from InquirerPy import prompt

def main() -> None:
    perguntas = [
    {
        "type": "list",
        "message" : "=======Qual seu conhecimento?=======",
        "choices" : ["Iniciante", "intermediario", "profissional"],
        
    },
    {"type": "confirm", "message": "confirm?"},
]

    resultado = prompt(perguntas)
    name = resultado[""]

if __name__ == "__main__":
    main()