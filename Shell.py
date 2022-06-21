import MASIC

while True:
    text = input("MASIC > ")
    result, error = MASIC.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)

