# Pasos para publicar la web en GitHub Pages

Guía numerada para llevar esta página (`index.html`) a una URL pública
de GitHub Pages.

## 1. Crear el repositorio en GitHub

1. Entra en <https://github.com> e inicia sesión.
2. Pulsa el botón **New** (o el signo `+` arriba a la derecha → *New repository*).
3. Pon un nombre al repositorio, por ejemplo `mi-pagina`.
   - Si quieres que la URL sea `usuario.github.io`, nómbralo exactamente así:
     `tuusuario.github.io`.
4. Deja el repositorio **público** (obligatorio para Pages en cuentas gratuitas).
5. No marques ninguna opción de inicialización (ni README, ni .gitignore…),
   porque ya tenemos commits locales.
6. Pulsa **Create repository**.

## 2. Conectar el repositorio local con GitHub

Añade el remoto (sustituye `tuusuario` y `mi-pagina` por los tuyos):

```bash
git remote add origin https://github.com/tuusuario/mi-pagina.git
```

Comprueba que se ha añadido bien:

```bash
git remote -v
```

## 3. Subir los cambios (push)

```bash
git push -u origin main
```

Si tu rama local se llama `master`, usa `git push -u origin master`,
o renómbrala antes con `git branch -M main`.

## 4. Activar GitHub Pages

1. En la página del repositorio en GitHub, ve a **Settings** (pestaña superior).
2. En el menú lateral izquierdo, pulsa **Pages**.
3. En **Build and deployment → Source**, selecciona **Deploy from a branch**.
4. En **Branch**, elige `main` y la carpeta `/ (root)`.
5. Pulsa **Save**.

## 5. Comprobar la publicación

1. Espera 1–2 minutos a que GitHub compile el sitio.
2. Recarga **Settings → Pages**: aparecerá un mensaje verde con la URL:
   `https://tuusuario.github.io/mi-pagina/`
3. Ábrela en el navegador y verifica que se ve la página.

## 6. Actualizar la web más adelante

Cada cambio que subas a la rama `main` se publicará automáticamente:

```bash
git add .
git commit -m "Actualizar contenido"
git push
```

> **Nota:** si al entrar ves un error 404, espera unos minutos o fuerza
> recarga (Ctrl+F5); la primera publicación tarda a veces un poco más.
