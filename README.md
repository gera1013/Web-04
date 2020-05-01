## API BEBES
# Gerardo Méndez Alvarez 18239

El api cuenta con medidas de autenticación.
También permite crear papás, bebés y eventos, y visualizarlos según permisos otorgados. 

Para iniciar hay que hacer login en la dirección url api/v1/token-auth/
Hay dos usuarios predeterminados con los nombres de usuario 'Gerardo' y 'Fernando'
Las contraseñas para ambos son 'password123' 
**En caso de no encontrarse estos usuarios, crear usuario propio y luego crear un papá asignandolo a ese usuario**

Luego de verificarse se utiliza el token para hacer todas las otras operaciones sobre el api

Cada papá debe asociarse a un usuario existente utilizando su nombre de usuario.
Cada papá puede crear cuantos bebés quiera, siempre y cuando los asocie a él cómo papá.
Los papás NO PUEDEN:
  - Ver bebés que no sean suyos
  - Crear eventos a bebés que no sean suyos
  
Los papás SÍ PUEDEN:
  - Crear bebés asociados a él
  - Ver bebés que son sus hijos
  - Crear eventos a bebés hijos
  - Ver eventos de bebés hijos
  
Las relaciones entre papás y usuarios se hacen mediante el nombre de usuario, y se le agregan en un campo con ese nombre a los papás.
Las relaciones entre papás y bebés se hacen mediante el pk del papá, agregándolo a un campo con ese nombre en los bebés.
Y los eventos se relacionan con los bebés por medio de la pk del bebé, poniéndola en un campo de los eventos.
