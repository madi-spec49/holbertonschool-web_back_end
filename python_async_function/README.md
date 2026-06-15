# Python Asyncio - Guide et Exemples 🚀

Bienvenue dans ce dépôt dédié à la programmation asynchrone en Python. Ce projet rassemble des explications, des concepts clés et des exemples de code pour comprendre et maîtriser le module de base `asyncio`.

---

## 📌 Qu'est-ce que la programmation asynchrone ?

La programmation asynchrone permet à un programme d'exécuter d'autres tâches en attendant la fin d'une opération lente (comme une requête réseau, une lecture de fichier ou une requête de base de données), au lieu de bloquer tout le script.

> **Note :** L'asynchronisme en Python utilise un **Event Loop** (boucle d'événements) unique. Ce n'est pas du multi-threading ou du multi-processing, mais de la **coopération** entre les tâches (cooperative multitasking).

---

## 🛠️ Concepts Clés

* **`async def` (Coroutine) :** Permet de définir une fonction asynchrone. Lorsqu'on l'appelle, elle ne s'exécute pas immédiatement, mais retourne un objet "coroutine".
* **`await` :** Met en pause l'exécution de la coroutine actuelle pour attendre le résultat d'une autre tâche asynchrone, laissant la boucle d'événements exécuter d'autres choses pendant ce temps.
* **Task (Tâche) :** Une coroutine enveloppée par `asyncio.create_task()`, ce qui permet de planifier son exécution immédiate en arrière-plan.
* **Event Loop :** Le chef d'orchestre qui gère et distribue l'exécution des différentes tâches.

---

## 💻 Exemples de Code

### 1. Le traditionnel "Hello World" Asynchrone
Un exemple simple pour comprendre la syntaxe de base.

```python
import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(1)  # Simule une attente asynchrone (ex: requête API)
    print("...World!")

# Lancement de la boucle d'événements et de la fonction principale
asyncio.run(main())