# 🚀 Python Async Generators & Annotations

Ce projet est un guide pratique pour comprendre et implémenter les générateurs asynchrones, les compréhensions asynchrones et le typage strict en Python.

---

## 1. Écrire un Générateur Asynchrone
Un générateur asynchrone combine `async def` et `yield`. Il permet de produire un flux de données de manière itérative sans bloquer la boucle d'événements.

```python
import asyncio

async def async_data_stream(items: int):
    for i in range(items):
        await asyncio.sleep(0.5)  # Simulation d'une attente I/O
        yield f"Donnée {i}"

# Consommation du générateur
async def main():
    async for data in async_data_stream(3):
        print(data)

asyncio.run(main())