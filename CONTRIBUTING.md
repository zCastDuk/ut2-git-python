# Guía de contribución para nuevas incorporaciones 

## Distribución de las ramas
Por convención de los colaboradores de este proyecto, se ha determinado que el trabajo sobre la rama 'main' queda reservado exclusivamente para cambios testeados y finalizados. 
El resto de trabajos se repartira en las diferentes ramas ya existentes o por medio de la creación y DOCUMENTACIÓN de ramas nuevas.

# Ramas actuales
 - Main
 - Mejora - rama

# ¿Cómo cambiar de rama?
Crear una rama y moverse a ella: `git switch -c nombre-descriptivo`
Cambiar de rama `git switch nombre-rama`

## Mensajes de commit
Se sigue el formato `tipo: descripción´ 
Los tipos son los siguientes:
 `feat`: para nuevas caracteristicas en la base del código
 `fix`: para arreglos en la base del código 
 `docs`: para modificaciones en la documentación
 `style`: para modificaciones en el estilo
 `refactor`: para la mejora de la infraestructura interna sin "cambios aparentes"
 `chore`: para tareas de mantenimiento
 

## Cómo proponer un cambio
1. Crea una rama desde `main`.
2. Haz tus commits en ella.
3. Sube la rama: `git push -u origin nombre-de-la-rama`.
4. Abre una Pull Request en GitHub describiendo el cambio.
5. Espera la revisión antes de fusionar.

## Cómo clonar y ejecutar este proyecto
git clone git@github.com:USUARIO/ut2-git-python.git
cd ut2-git-python
python3 ej01_par_impar.py # (python en Windows)
