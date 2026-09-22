# Práctica 1: Operaciones Básicas sobre Lenguajes

**Instituto Politécnico Nacional**  
**Escuela Superior de Cómputo (ESCOM)**  
**Unidad de Aprendizaje:** Teoría de la Computación  
**Plan de Estudios:** Ingeniería en Sistemas Computacionales (2020)  

---

### Datos del Alumno
- **Nombre:** Oscar Orlando Hernández Alcántara  
- **Boleta:** [2024630611]  
- **Grupo:** [4CV4]  
- **Profesor:** [Gabriel Hurtado Avilés]  
- **Fecha de Entrega:** 22 de septiembre de 2026  

---

### Índice de la Práctica
1. [Ejercicio 1: Entorno de Trabajo (docs/01-entorno.md)](docs/01-entorno.md)
   - Parte A: Investigación teórica (VCS, Git vs GitHub, Docker, Entornos virtuales)
   - Parte B: Repositorio y control de versiones
   - Parte C: Tres entornos de Python (3.11, 3.12 y 3.13)
2. [Ejercicio 2: Investigación Teórica de la Unidad I (docs/02-investigacion.md)](docs/02-investigacion.md)
3. [Ejercicio 3: Estado del Arte - Cinco Artículos (docs/03-estado-del-arte.md)](docs/03-estado-del-arte.md)
4. [Ejercicio 4: Autómatas Finitos en JFLAP (docs/04-jflap.md)](docs/04-jflap.md)
5. [Ejercicio 5: Aplicación con Interfaz Gráfica en Flet (docs/05-aplicacion.md)](docs/05-aplicacion.md)
6. [Conclusiones](docs/conclusiones.md)
7. [Bibliografía en Formato APA](docs/bibliografia.md)

---

### Instrucciones de Ejecución
```bash
# Construir las imágenes de Docker
docker compose -f entorno/compose.yml build

# Ejecutar pruebas unitarias en las tres versiones
docker compose -f entorno/compose.yml run --rm py311 pytest -q
docker compose -f entorno/compose.yml run --rm py312 pytest -q
docker compose -f entorno/compose.yml run --rm py313 pytest -q

# Levantar la aplicación con interfaz gráfica (Flet)
docker compose -f entorno/compose.yml up py312
# Abrir en el navegador: http://localhost:8550
