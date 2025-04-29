import streamlit as st

# Configuration
st.set_page_config(page_title="LocaQuizz 🌍", page_icon="🥕", layout="centered")
st.title("🎯 LocaQuizz : Le quiz des circuits courts !")
st.markdown("Découvre comment manger local peut aider la planète 🌱")
st.markdown("---")

# Questions
questions = [
    {
        "question": "Que veut dire “manger local” ?",
        "options": ["Manger des légumes du supermarché en hiver", "Manger des aliments produits près de chez toi", "Manger en regardant une carte"],
        "answer": 1
    },
    {
        "question": "Quel est le moyen de transport le plus écologique pour les fruits ?",
        "options": ["La fusée", "Le vélo", "Le camion réfrigéré"],
        "answer": 1
    },
    {
        "question": "Quelle fraise est la plus “locale” ?",
        "options": ["Une fraise de ton jardin", "Une fraise qui vient d’Espagne", "Une fraise en bonbon"],
        "answer": 0
    },
    {
        "question": "Je pousse dans la terre, je suis orange, qui suis-je ?",
        "options": ["Une pizza", "Une carotte", "Un smartphone"],
        "answer": 1
    },
    {
        "question": "Pourquoi acheter aux petits producteurs ?",
        "options": ["Pour aider les voisins et la planète", "Parce que c’est plus rigolo", "Pour devenir célèbre"],
        "answer": 0
    },
    {
        "question": "Les circuits courts, c’est comme...",
        "options": ["Une grande boucle autour du monde", "Un raccourci pour que les aliments aillent vite dans ton assiette", "Une ligne de métro"],
        "answer": 1
    },
    {
        "question": "Quel fruit pousse en été et peut être acheté localement ?",
        "options": ["La pastèque", "La banane", "Le kiwi"],
        "answer": 0
    },
    {
        "question": "Que fait un marché local ?",
        "options": ["Il vend des produits faits loin", "Il vend des jeux vidéos", "Il vend les légumes des producteurs proches"],
        "answer": 2
    },
    {
        "question": "Quel est le super-pouvoir des légumes locaux ?",
        "options": ["Ils dansent la salsa", "Ils polluent moins et sont plus frais", "Ils brillent dans le noir"],
        "answer": 1
    },
    {
        "question": "Si tu veux aider la planète en mangeant, tu choisis ?",
        "options": ["Des tomates venues en avion", "Des chips arc-en-ciel", "Des tomates du jardin de papi"],
        "answer": 2
    }
]

# Initialisation des états
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "responses" not in st.session_state:
    st.session_state.responses = [None] * len(questions)
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

index = st.session_state.question_index
question = questions[index]

# Affichage question
st.subheader(f"❓ Question {index + 1}")
key_radio = f"radio_{index}"

# Si la réponse n’a pas encore été donnée
if st.session_state.responses[index] is None:
    choix = st.radio(question["question"], question["options"], key=key_radio, index=None)
    if st.button("✅ Valider ma réponse"):
        st.session_state.responses[index] = choix
        if question["options"].index(choix) == question["answer"]:
            st.session_state.score += 1
        st.rerun()
else:
    # Affiche la réponse donnée
    reponse = st.session_state.responses[index]
    bonne = question["options"][question["answer"]]
    st.markdown(f"**Ta réponse :** {reponse}")
    if reponse == bonne:
        st.success("✅ Bonne réponse !")
    else:
        st.error(f"❌ Mauvaise réponse. La bonne réponse était : **{bonne}**")

    # Bouton pour passer à la question suivante ou voir les résultats
    if index < len(questions) - 1:
        if st.button("➡️ Question suivante"):
            st.session_state.question_index += 1
            st.rerun()
    else:
        if st.button("📊 Voir mon score"):
            st.session_state.quiz_finished = True
            st.rerun()

# Affichage du score final
if st.session_state.quiz_finished:
    st.success(f"👏 Tu as eu {st.session_state.score} bonnes réponses sur {len(questions)} !")
    if st.session_state.score == len(questions):
        st.balloons()
        st.info("Tu es un vrai champion du local 🌟 !")
    elif st.session_state.score >= 3:
        st.info("Bravo ! Tu connais déjà bien les circuits courts 💚")
    else:
        st.info("Pas mal ! Et maintenant, tu en sais encore plus 🌍")

    if st.button("🔁 Recommencer le quiz"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

st.markdown("---")
st.caption("© 2025 - Projet express pour sensibiliser les jeunes à l'alimentation locale.")








# import streamlit as st

# # Définition des questions du quiz
# questions = [
#     {
#         "question": "Que veut dire “manger local” ?",
#         "options": ["Manger des légumes du supermarché en hiver", "Manger des aliments produits près de chez toi", "Manger en regardant une carte"],
#         "answer": 1
#     },
#     {
#         "question": "Quel est le moyen de transport le plus écologique pour les fruits ?",
#         "options": ["La fusée", "Le vélo", "Le camion réfrigéré"],
#         "answer": 1
#     },
#     {
#         "question": "Quelle fraise est la plus “locale” ?",
#         "options": ["Une fraise de ton jardin", "Une fraise qui vient d’Espagne", "Une fraise en bonbon"],
#         "answer": 0
#     },
#     {
#         "question": "Je pousse dans la terre, je suis orange, qui suis-je ?",
#         "options": ["Une pizza", "Une carotte", "Un smartphone"],
#         "answer": 1
#     },
#     {
#         "question": "Pourquoi acheter aux petits producteurs ?",
#         "options": ["Pour aider les voisins et la planète", "Parce que c’est plus rigolo", "Pour devenir célèbre"],
#         "answer": 0
#     },
#     {
#         "question": "Les circuits courts, c’est comme...",
#         "options": ["Une grande boucle autour du monde", "Un raccourci pour que les aliments aillent vite dans ton assiette", "Une ligne de métro"],
#         "answer": 1
#     },
#     {
#         "question": "Quel fruit pousse en été et peut être acheté localement ?",
#         "options": ["La pastèque", "La banane", "Le kiwi"],
#         "answer": 0
#     },
#     {
#         "question": "Que fait un marché local ?",
#         "options": ["Il vend des produits faits loin", "Il vend des jeux vidéos", "Il vend les légumes des producteurs proches"],
#         "answer": 2
#     },
#     {
#         "question": "Quel est le super-pouvoir des légumes locaux ?",
#         "options": ["Ils dansent la salsa", "Ils polluent moins et sont plus frais", "Ils brillent dans le noir"],
#         "answer": 1
#     },
#     {
#         "question": "Si tu veux aider la planète en mangeant, tu choisis ?",
#         "options": ["Des tomates venues en avion", "Des chips arc-en-ciel", "Des tomates du jardin de papi"],
#         "answer": 2
#     }
# ]

# # Initialisation du score et de la session_state pour suivre les réponses
# if 'score' not in st.session_state:
#     st.session_state.score = 0
# if 'question_index' not in st.session_state:
#     st.session_state.question_index = 0

# # Fonction pour afficher chaque question
# def afficher_question(index):
#     question = questions[index]
#     st.subheader(f"❓ Question {index + 1}")
    
#     choix = st.radio(question["question"], question["options"], key=f"question_{index}", index=None)
    
#     if choix is not None:
#         # Si la réponse est correcte, on incrémente le score
#         if question["options"].index(choix) == question["answer"]:
#             st.session_state.score += 1
#             st.success("✅ Bonne réponse !")
#         else:
#             st.error("❌ Mauvaise réponse.")
        
#         # Avancer à la question suivante
#         st.session_state.question_index += 1

#         # Ajouter un bouton pour passer à la question suivante
#         if st.session_state.question_index < len(questions):
#             st.button("Suivant", on_click=afficher_question, args=(st.session_state.question_index,))
#         else:
#             st.button("Voir mon score", on_click=afficher_score)

# # Fonction pour afficher le score final
# def afficher_score():
#     st.subheader(f"Ton score final : {st.session_state.score}/{len(questions)}")
#     if st.session_state.score == len(questions):
#         st.balloons()
#         st.info("Tu es un vrai champion du local 🌟 !")
#     elif st.session_state.score >= 7:
#         st.info("Bravo ! Tu connais déjà bien les circuits courts 💚")
#     else:
#         st.info("Pas mal ! Et maintenant, tu en sais encore plus 🌍")

# # Afficher la première question si le quiz commence
# if st.session_state.question_index < len(questions):
#     afficher_question(st.session_state.question_index)
# else:
#     afficher_score()

















# import streamlit as st

# # Liste des questions
# questions = [
#     {
#         "question": "Que veut dire “manger local” ?",
#         "options": ["Manger des légumes du supermarché en hiver", "Manger des aliments produits près de chez toi", "Manger en regardant une carte"],
#         "answer": 1
#     },
#     {
#         "question": "Quel est le moyen de transport le plus écologique pour les fruits ?",
#         "options": ["La fusée", "Le vélo", "Le camion réfrigéré"],
#         "answer": 1
#     },
#     {
#         "question": "Quelle fraise est la plus “locale” ?",
#         "options": ["Une fraise de ton jardin", "Une fraise qui vient d’Espagne", "Une fraise en bonbon"],
#         "answer": 0
#     },
#     {
#         "question": "Je pousse dans la terre, je suis orange, qui suis-je ?",
#         "options": ["Une pizza", "Une carotte", "Un smartphone"],
#         "answer": 1
#     },
#     {
#         "question": "Pourquoi acheter aux petits producteurs ?",
#         "options": ["Pour aider les voisins et la planète", "Parce que c’est plus rigolo", "Pour devenir célèbre"],
#         "answer": 0
#     },
#     {
#         "question": "Les circuits courts, c’est comme...",
#         "options": ["Une grande boucle autour du monde", "Un raccourci pour que les aliments aillent vite dans ton assiette", "Une ligne de métro"],
#         "answer": 1
#     },
#     {
#         "question": "Quel fruit pousse en été et peut être acheté localement ?",
#         "options": ["La pastèque", "La banane", "Le kiwi"],
#         "answer": 0
#     },
#     {
#         "question": "Que fait un marché local ?",
#         "options": ["Il vend des produits faits loin", "Il vend des jeux vidéos", "Il vend les légumes des producteurs proches"],
#         "answer": 2
#     },
#     {
#         "question": "Quel est le super-pouvoir des légumes locaux ?",
#         "options": ["Ils dansent la salsa", "Ils polluent moins et sont plus frais", "Ils brillent dans le noir"],
#         "answer": 1
#     },
#     {
#         "question": "Si tu veux aider la planète en mangeant, tu choisis ?",
#         "options": ["Des tomates venues en avion", "Des chips arc-en-ciel", "Des tomates du jardin de papi"],
#         "answer": 2
#     }
# ]


# # Initialisation
# if "score" not in st.session_state:
#     st.session_state.score = 0
# if "question_index" not in st.session_state:
#     st.session_state.question_index = 0
# if "answered" not in st.session_state:
#     st.session_state.answered = False

# # Affiche la question actuelle
# index = st.session_state.question_index
# if index < len(questions):
#     q = questions[index]
#     st.subheader(f"❓ Question {index + 1}")
    
#     # Affiche les choix, sans pré-sélection
#     choix = st.radio(
#         q["question"],
#         q["options"],
#         key=f"question_{index}",
#         index=None
#     )

#     # Vérifie si réponse soumise
#     if choix and not st.session_state.answered:
#         if q["options"].index(choix) == q["answer"]:
#             st.session_state.score += 1
#             st.success("✅ Bonne réponse !")
#         else:
#             st.error("❌ Mauvaise réponse.")
#         st.session_state.answered = True

#     # Bouton suivant
#     if st.session_state.answered:
#         if st.button("➡️ Question suivante"):
#             st.session_state.question_index += 1
#             st.session_state.answered = False
#             st.rerun()

# else:
#     # Résultat final
#     st.subheader(f"Ton score final : {st.session_state.score}/{len(questions)}")
#     if st.session_state.score == len(questions):
#         st.balloons()
#         st.info("Tu es un vrai champion du local 🌟 !")
#     elif st.session_state.score >= 7:
#         st.info("Bravo ! Tu connais déjà bien les circuits courts 💚")
#     else:
#         st.info("Pas mal ! Et maintenant, tu en sais encore plus 🌍")

#     if st.button("🔁 Recommencer le quiz"):
#         st.session_state.score = 0
#         st.session_state.question_index = 0
#         st.session_state.answered = False
