import json

# Generar 20 mensajes de "Hola"
messages = ["Hola" for _ in range(20)]

# Guardar los mensajes en un archivo JSON
output_file = "hello_messages.json"
with open(output_file, "w") as f:
    json.dump(messages, f)

print(f"Se generaron los mensajes de 'Hola' en {output_file}")
