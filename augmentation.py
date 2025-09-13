from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


ODS_GOALS = {
    1: "Temas de reducción de la pobreza: carencia de recursos, apoyo económico, inclusión social, programas de ayuda, desarrollo comunitario, acceso a vivienda y alimentación.",
    3: "Temas de salud y bienestar: acceso a servicios de salud, prevención de enfermedades, salud mental, promoción de hábitos saludables, atención médica de calidad, vacunación, reducción de mortalidad.",
    4: "Temas de educación de calidad: acceso equitativo a educación, formación de docentes, becas, infraestructura escolar, inclusión educativa, alfabetización, reducción del abandono escolar.",
}


PROMPT_TEMPLATE = ChatPromptTemplate.from_template("""
Genera un texto breve (alrededor de 100 palabras) que trate sobre el siguiente tema, sin decir que está relacionado con un objetivo global ni mencionarlo por nombre o número:
- {goal}
El texto debe ser natural, como si lo hubiera escrito una persona para un artículo, un comentario o una publicación, sin palabras clave técnicas. Varía los estilos (formal, informal, narrativo, descriptivo, etc.) y el tono para aumentar la diversidad.
""")


if __name__ == "__main__":
    goal = int(
        input("Ingresse el número del objetivo de desarrollo sostenible (1, 3 o 4): ")
    )
    llm = init_chat_model(
        model="",  # TODO: Host LLM model or use a service
        temperature=0.4,
    )
    chain = LLMChain(llm=llm, prompt=PROMPT_TEMPLATE)

    response = chain.run(goal=ODS_GOALS[goal])
    print("\nTexto generado:\n")
    print(response)
