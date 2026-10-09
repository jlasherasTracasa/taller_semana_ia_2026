# Pasos para publicar en GitHub Pages

Guía para quien hace el último paso a mano (sin dar credenciales al agente).

## 1. Crear el repositorio en GitHub

1. Entra en <https://github.com/new> con tu cuenta.
2. Nombre del repositorio: por ejemplo `panaderia-pilar-azcona`.
3. Visibilidad: **Public** (necesario para Pages gratis en cuentas gratuitas).
4. NO marques ninguna opción de inicialización (ni README, ni .gitignore, ni licencia).
5. Pulsa **Create repository**.

## 2. Conectar este repositorio local

Desde esta carpeta, sustituyendo `<usuario>` por tu nombre de usuario de GitHub:

```bash
git remote add origin https://github.com/<usuario>/panaderia-pilar-azcona.git
git branch -M main
```

## 3. Subir los cambios (lo haces tú)

```bash
git push -u origin main
```

GitHub te pedirá usuario y contraseña: la contraseña **no es tu password**, es un
*token de acceso personal*.

> 🔐 Si necesitas crear un token: GitHub → Settings → Developer settings →
> Personal access tokens → **Fine-grained**. Permiso mínimo: acceso de escritura solo
> a ese repositorio (`Contents: Read and write`). Caducidad corta (7 días).

## 4. Activar GitHub Pages

1. En el repositorio: **Settings → Pages** (menú izquierdo).
2. En *Build and deployment*:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` y carpeta `/ (root)`
3. Pulsa **Save**.

## 5. Comprobar la URL pública

1. Espera 1–2 minutos.
2. La URL aparece arriba de Settings → Pages: `https://<usuario>.github.io/panaderia-pilar-azcona/`
3. Ábrela y compártela (¡ahora Pilar tiene su enlace para WhatsApp!).

## 6. Publicar cambios futuros

Tras editar `index.html`, en esta carpeta:

```bash
git add index.html
git commit -m "Actualiza la web"
git push            # Pages se actualiza solo en ~1 minuto
```
