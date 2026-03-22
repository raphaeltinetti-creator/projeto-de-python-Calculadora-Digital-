from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_resultado(n1, n2, op):

    if op == "1":
        return n1 + n2
    elif op == "2":
        return n1 - n2
    elif op == "3":
        return n1 * n2
    elif op == "4":

        if n2 == 0:
            return "Erro: Divisão por zero não permitida."
        return n1 / n2
    elif op == "5":
        return n1 ** n2

    return "Erro: Operação Inválida."


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:

            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            op = request.form.get("operacao")

            resultado = calcular_resultado(num1, num2, op)

            if isinstance(resultado, float):
                resultado = round(resultado, 4)

        except ValueError:
            resultado = "Por favor, preencha os dois números corretamente."

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
